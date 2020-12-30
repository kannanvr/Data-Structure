#!/usr/bin/env python3.6
"""
Run Pandoc to convert an HTML to PDF.

Usage: html_to_pdf [options] <src>

Options:

    --tex       Convert to PDF instead of tex
"""

import os

from subprocess import call

from docopt import docopt


ROOT_PDF = "PDF"


def generate_pdf(src, dst):

    # If source doesn't exist or destination already does
    if not os.path.isfile(src):
        print("Source HTML doesn't exist")
        return

    if os.path.isfile(dst):
        print("Destination PDF already exists")
        return

    title = os.path.basename(src)
    title = title[0:title.rfind(".")]

    command = [
        "/usr/bin/pandoc",
        # "--template=template.tex",
        "--template=jgm.tex",
        "--toc",
        "--pdf-engine", "xelatex",
        "-V" "geometry:margin=1.5in",
        # "-V" "geometry:papersize=a3paper",
        "-V", "documentclass=report",
        "-V", "urlcolor=blue",
        "-V", "linkcolor=blue",
        # "-V", "title="+title,
        "-f", "html",
        src,
        "-o", dst,
    ]

    # print(" ".join(command))
    print(command[-1])
    call(command)


if __name__ == '__main__':

    args = docopt(__doc__)

    src = os.path.basename(args['<src>'])

    if args['--tex']:
        dst = src.replace(".html", ".tex")
    else:
        dst = src.replace(".html", ".pdf")

    generate_pdf(args['<src>'], os.path.join(ROOT_PDF, dst))
