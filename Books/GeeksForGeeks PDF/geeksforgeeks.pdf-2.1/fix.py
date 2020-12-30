import os
import re
import glob
import json
from collections import OrderedDict

root = "Topics"
root_html = "#HTML"
root_pdf = "#PDF"


def fix_headings(file):
    with open(file, 'r') as inp:
        src = inp.read()

    if '<h1 class="tabtitle"' in src:
        src = src.replace('<h1 class="tabtitle">C++</h1>', '<p><strong>C++</strong></p>')
        src = src.replace('<h1 class="tabtitle">C</h1>', '<p><strong>C</strong></p>')
        src = src.replace('<h1 class="tabtitle">C/C++</h1>', '<p><strong>C/C++</strong></p>')
        src = src.replace('<h1 class="tabtitle">Java</h1>', '<p><strong>Java</strong></p>')
        src = src.replace('<h1 class="tabtitle">Python</h1>', '<p><strong>Python</strong></p>')
        src = src.replace('<h1 class="tabtitle">Pyhton</h1>', '<p><strong>Python</strong></p>')

        with open(file, 'w') as out:
            print(file)
            out.write(src)


def fix_set_title(file):
    with open(file, 'r') as inp:
        src = inp.read()

    topic = os.path.basename(file).split(".")[0]
    if topic + ' | Set' in src:
        src = re.sub(topic + r"\s+\|\s+(Set\s+\d+\s+\(.*\))", r"\1", src)

        with open(file, 'w') as out:
            print(file)
            out.write(src)


def fix_missing_title():

    def _fix_missing_title(topic, folder):
        for title, url in topic.items():
            file = os.path.join(folder, url.split('/')[-2]+".html")

            if not os.path.isfile(file):
                print("UGHHHHH!!!")
                continue

            with open(file) as inp:
                content = inp.read()

            if "<body><h1>" not in content:
                print(file)
                content = content.replace("<body>", "<body><h1>" + title + "</h1>")
                with open(file, 'wb') as out:
                    out.write(content.encode('utf-8'))

    with open("JSON/DS.json") as inp:
        ds = json.load(inp, object_pairs_hook=OrderedDict)

    for topic in ds.keys():
        if topic in ['Advanced Data Structures']:
            for sub_topic in ds[topic]:
                _fix_missing_title(ds[topic][sub_topic], os.path.join(root, topic))
        else:
            _fix_missing_title(ds[topic], os.path.join(root, topic))

if __name__ == '__main__':
    fix_missing_title()
    map(fix_headings, glob.glob(root_html+"/*.html"))
    map(fix_set_title, glob.glob(root_html+"/*.html"))
