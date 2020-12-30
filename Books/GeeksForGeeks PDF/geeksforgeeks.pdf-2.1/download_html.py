#!/usr/bin/env python3

import os
import sys
import json

from collections import OrderedDict

import requests
import requests_cache

import glean

ROOT = "Topics"
ROOT_HTML = "HTML"


requests_cache.install_cache("geeks")


def mkdir(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


def download(urls, folder):
    mkdir(folder)

    cleaned_html = []

    for url in urls:

        file = os.path.join(folder, url.split('/')[-2] + ".html")

        if os.path.isfile(file):
            print(file)
            with open(file) as inp:
                cleaned = inp.read()
        else:
            print(url, file)

            r = requests.get(url)
            cleaned = glean.clean(r.content)

            with open(file, 'w') as out:
                out.write(cleaned)

        cleaned_html.append(cleaned)

    cleaned_file = os.path.join(
        ROOT_HTML,
        folder.split('/')[-1] + ".html"
    )

    with open(cleaned_file, 'w') as out:
        out.write("\n".join(cleaned_html))


def download_from_json_with_topic_keys(ds):

    # Only download these topics
    # some_topics = [
    #     'Graphs',
    #     'Binary Trees',
    # ]

    for topic in ds.keys():
        # for topic in some_topics:
        if topic in ['Advanced Data Structures']:
            urls = []
            for sub_topic in ds[topic]:
                urls += ds[topic][sub_topic].values()
            download(urls, os.path.join(ROOT, topic))
        else:
            download(ds[topic].values(), os.path.join(ROOT, topic))


def download_from_json(ds, topic):
    download(ds.values(), os.path.join(ROOT, topic))


if __name__ == '__main__':
    fpath = sys.argv[1]
    fname = os.path.split(fpath)[1]
    topic = os.path.splitext(fname)[0]

    with open(fpath) as inp:
        ds = json.load(inp, object_pairs_hook=OrderedDict)

    # download_from_json_with_topic_keys(ds)
    download_from_json(ds, topic)
