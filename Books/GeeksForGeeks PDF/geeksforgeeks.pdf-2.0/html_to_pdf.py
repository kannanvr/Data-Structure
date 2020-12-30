#!/usr/bin/env python3.6
"""
Run Pandoc to convert an HTML to PDF.

Usage: html_to_pdf [options] <src>

Options:

    -t --tex         Convert to PDF instead of tex
    -f --force       Overwrite destination
"""

import os

from subprocess import call

from docopt import docopt


ROOT_PDF = "PDF"


def generate_pdf(src, dst, force=False):

    # If source doesn't exist or destination already does
    if not os.path.isfile(src):
        print("Source HTML doesn't exist")
        return

    if not force and os.path.isfile(dst):
        print("Destination already exists.")
        return

    title = os.path.basename(src)
    title = title[0:title.rfind(".")]

    command = [
        "/usr/bin/pandoc",
        "--quiet",

        "--pdf-engine", "xelatex",

        "--toc",

        "--template=template.tex",
        "-V", "geometry:margin=1.5in",
        "-V", "documentclass=report",
        # "-V" "geometry:papersize=a3paper",

        "-V", "urlcolor=blue",
        "-V", "linkcolor=blue",

        # "-V", "title="+title,

        src,
        "-o", dst,
    ]

    # Run in verbose mode when converting from a .tex to .pdf
    # because one would only do this when shit has gone wrong
    if src.endswith(".tex"):
        command[1] = "--verbose"
        print(" ".join(command))
    else:
        print(command[-1])

    # Do it!
    call(command)


if __name__ == '__main__':

    args = docopt(__doc__)

    src = os.path.basename(args['<src>'])

    if args['--tex']:
        dst = src.replace(".html", ".tex")
    else:
        dst = src.replace(".html", ".pdf").replace(".tex", ".pdf")

    generate_pdf(
        src=args['<src>'],
        dst=os.path.join(ROOT_PDF, dst),
        force=args["--force"],
    )
