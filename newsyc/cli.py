"""
Command line goodness.
"""

from argparse import ArgumentParser

def create_parser():
    """Create the Hacker News command line parser."""
    description = 'A simple and easy-to-use CLI for the HNSearch API.'
    parser = ArgumentParser(prog='hn', description=description)
    parser.add_argument('search', metavar='S', type=str, nargs='*',
                        help="A search term to query for.")
    return parser
