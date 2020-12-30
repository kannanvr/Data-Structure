"""Use boilerpipy + LXML to clean downloaded html files."""

from html import escape as html_escape

import lxml.etree
import lxml.html as html
from lxml.html.clean import Cleaner


def remove_xpaths(elem, xpaths, parent=False):
    for path in xpaths:
        for tag in elem.xpath(path):
            if parent:
                tag = tag.getparent()
            tag.getparent().remove(tag)


def clean(content, title=None):
    content = content.decode("utf-8")

    # We're parsing the content html twice!
    # TODO: This one can probably be removed
    # LXML parsing is used to get title and meta head info from HTML
    html_doc = html.fromstring(content,
                               parser=html.HTMLParser(encoding="utf-8"))
    head_doc = html_doc.find('head')

    reconstructed_body = "<html><body>" + content + "</body></html>"

    # Get title so it can be added as an H1 tag, but remove it from
    # the html itself - so that Pandoc doesn't use it
    if not title:
        title = html_doc.find('.//title')
        title.getparent().remove(title)
        title = title.text_content()
        title = title[:title.rfind('-')]

    # Add in the title
    if "<body><h1>" not in reconstructed_body:
        reconstructed_body = reconstructed_body.replace(
            "<body>", "<body><h1>" + title + "</h1>"
        )

    # Remove stuff that readability didn't remove
    doc = html.fromstring(reconstructed_body)

    # Use lxml's cleaner to remove all useless tags
    # (currently, this removes styles, even when not asked to)
    cleaner = Cleaner(
        scripts=True, javascript=True, comments=True,
        links=True, forms=True, annoying_tags=True,
        style=True, inline_style=False,
    )
    doc = cleaner.clean_html(doc)

    body_doc = doc.find('body')

    bad_body_xpaths = [
        "//nav",
        "//footer",
        "//button",

        "//form[@id='interview_experience_form']",

        "//div[@id='page']",
        "//div[@id='author']",
        "//div[@id='video']",
        "//div[@id='share-buttons']",
        "//div[@id='ide_link']",
        "//div[@id='disqus_thread']",
        "//div[@id='secondary']",
        "//div[@id='personalNoteDiv']",
        "//div[@id='practiceLinkDiv']",

        "//div[@class='leftSideBarParent']",
        "//div[@class='author_info_box']",
        "//div[@class='plugins']",
        "//div[@class='no-p-tag']",
        "//div[@class='comments-main']",

        "//ins[@class='adsbygoogle']",

        "//h3",
        "//h1[@class='entry-title']",
        "//h2[not(@class='tabtitle')]",

        "//hr",

        # This requires XPath 2.0
        # "//a[ends-with(@href, 'sudo-gate')]",
        "//a[contains(@href, 'sudo-gate')]",

        "//p[contains(., 'contribute@geeksforgeeks.org')]",
        "//p[starts-with(., 'Please write comments if you find')]",
    ]

    bad_parent_xpaths = [
        "//h2[starts-with(text(), 'Recommended')]",
    ]

    # This one has to be removed first, so h2's parent can die!
    remove_xpaths(body_doc, bad_parent_xpaths, parent=True)
    remove_xpaths(body_doc, bad_body_xpaths)

    # Convert all language tags to p tags
    # H1 is used only for post title
    for lang_h1 in body_doc.xpath("//h2[@class='tabtitle']"):
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
