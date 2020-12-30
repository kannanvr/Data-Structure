"""Use boilerpipy + LXML to clean downloaded html files."""

import sys

from html import escape as html_escape

import lxml.etree
import lxml.html as html

from readability import Document


def clean(content):
    content = content.decode("utf-8")

    try:
        # Use Python Readability to clean up the HTML
        doc = Document(content)
        article = doc.get_clean_html()
    except:  # noqa
        print("Error cleaning up the html.")
        sys.exit(1)

    # LXML parsing is used to get title and meta head info from HTML
    html_doc = html.fromstring(content,
                               parser=html.HTMLParser(encoding="utf-8"))
    head_doc = html_doc.find('head')

    reconstructed_body = "<html><body>" + article + "</body></html>"

    # Get title so it can be added as an H1 tag, but remove it from
    # the html itself - so that Pandoc doesn't use it
    title = html_doc.find('.//title')
    title.getparent().remove(title)
    title = title.text_content()

    # Add in the title
    if "<body><h1>" not in reconstructed_body:
        reconstructed_body = reconstructed_body.replace(
            "<body>",
            "<body><h1>" +
            title[:title.rfind('-')] + "</h1>"
        )

    # Remove stuff that readability didn't remove
    body_doc = html.fromstring(reconstructed_body).find('body')

    bad_tags = (
        body_doc.xpath("//button") +
        body_doc.xpath("//nav") +
        body_doc.xpath("//footer") +
        body_doc.xpath("//div[@id='page']") +
        body_doc.xpath("//form[@id='interview_experience_form']") +
        body_doc.xpath("//div[@id='author']") +
        body_doc.xpath("//div[@id='share-buttons']") +
        body_doc.xpath("//div[@id='ide_link']") +
        body_doc.xpath("//div[@id='disqus_thread']") +
        body_doc.xpath("//div[@id='secondary']") +
        body_doc.xpath("//div[@id='personalNoteDiv']") +
        body_doc.xpath("//div[@id='practiceLinkDiv']") +
        body_doc.xpath("//div[@class='leftSideBarParent']") +
        body_doc.xpath("//div[@class='author_info_box']") +
        body_doc.xpath("//div[@class='plugins']") +
        body_doc.xpath("//div[@class='no-p-tag']") +
        body_doc.xpath("//div[@class='comments-main']") +
        body_doc.xpath("//ins[@class='adsbygoogle']") +
        body_doc.xpath("//h1[@class='entry-title']") +
        body_doc.xpath("//hr") +
        body_doc.xpath("//h3") +
        body_doc.xpath("//h2")
    )

    for tag in bad_tags:
        tag.getparent().remove(tag)

    # Remove tags that start with some text - along with their parent
    bad_tags = (
        body_doc.xpath('//h1[starts-with(text(),"Recommended")]')
    )
    for tag in bad_tags:
        parent = tag.getparent()
        parent.getparent().remove(parent)

    # Convert all H1 language tags to p tags
    for lang_h1 in body_doc.xpath("//h1[@class='tabtitle']"):
        lang_p = '<p><strong>%s</strong></p>' % lang_h1.text_content()
        lang_h1.addnext(lxml.etree.XML(lang_p))
        lang_h1.getparent().remove(lang_h1)

    # Not too sure if this is needed - but at this point
    # I don't want to remove any code that works
    for pre_tag in body_doc.xpath("//pre"):
        if 'class' in pre_tag.attrib:
            pre_tag.attrib.pop('class')
        if 'title' in pre_tag.attrib:
            pre_tag.attrib.pop('title')

    try:
        # Add Source link to doc - this may fail for various reasons
        src_url = head_doc.cssselect('meta[property="og:url"]')[0].get('content')  # noqa
        src_link = "<p><a href='" + src_url + "' rel='tag'>" + src_url + "</a></p>"  # noqa
        post_content_doc = body_doc.xpath("//div[@class='entry-content']")[0]
        post_content_doc.append(lxml.etree.XML("<h3>Source</h3>"))
        post_content_doc.append(lxml.etree.XML(src_link))
    except:  # noqa
        pass

    # Code in the HTML is in the form of a table
    # We convert the table into a single pre / code tag
    for code_tag in body_doc.xpath('//div[starts-with(@id,"highlighter")]'):
        code = str(code_tag.text_content()).replace("\n\n", "")
        code = html_escape(code)
        code = "<pre> <code>" + code + "</code> </pre>"
        code_tag.addnext(lxml.etree.XML(code))
        code_tag.getparent().remove(code_tag)

    result = html.tostring(body_doc).decode("utf-8")

    return result


if __name__ == '__main__':
    import requests
    u = "https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/"
    r = requests.get(u)
    cleaned = clean(r.content)
    print(cleaned)
