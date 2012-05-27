"""
Command line goodness.
"""

import sys
from argparse import ArgumentParser
import simplejson as json
from .core import YCombinator

try:
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter as Term256
    from pygments.lexers import JavascriptLexer
    has_pygments = True
except ImportError:
    has_pygments = False


def create_parser():
    """Create the Hacker News command line parser."""
    description = 'A simple and easy-to-use CLI for the HNSearch API.'
    parser = ArgumentParser(prog='hn', description=description)
    parser.add_argument('search', metavar='S', type=str, nargs='*',
                        help="A search term to query for.")
    return parser


def search(options):
    """Perform a search against the HNSearch API."""
    if options.search:
        term = ' '.join(options.search)
        data = YCombinator().search(term)
        return decorate(data)


def decorate(stream, indent=2):
    """Turn JSON into something readable."""
    print_formatted_json(sys.stdout, stream, indent)
    sys.stdout.write('\n')


def print_formatted_json(stream, json_data, indentation):
    """Format and print JSON."""
    formatted = json.dumps(json_data, indent=indentation)
    if has_pygments:
        formatter = Term256()
        lexer = JavascriptLexer()
        formatted = highlight(formatted, formatter=formatter, lexer=lexer)
    print >> stream, formatted.rstrip()
