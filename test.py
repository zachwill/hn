"""
Tests and such.
"""

from unittest import TestCase, main
from mock import Mock

from yc import cli
from yc import core


class CLI(TestCase):

    def setUp(self):
        core.req = Mock()
        self.parser = cli.create_parser()

    def test_empy_parser(self):
        args = []
        options = self.parser.parse_args(args)
        self.assertTrue(isinstance(options.search, list))

    def test_parser_can_handle_multiple_search_terms(self):
        args = 'one two three'.split(' ')
        options = self.parser.parse_args(args)
        self.assertEquals(options.search, args)

    def test_parser_recognizes_limit_and_start_options(self):
        args = 'term -n 50 -s 100'.split(' ')
        options = self.parser.parse_args(args)
        self.assertEquals(options.limit, 50)
        self.assertEquals(options.start, 100)

    def test_parser_can_recognize_dates(self):
        args = '-d 03-16-12'.split(' ')
        options = self.parser.parse_args(args)
        self.assertEquals(options.day, '03-16-12')
        args = '-d 2012-03-16'.split(' ')
        options = self.parser.parse_args(args)
        self.assertEquals(options.day, '2012-03-16')

    def test_parser_recognizes_hits_flag(self):
        args = 'github --hits'.split(' ')
        options = self.parser.parse_args(args)
        self.assertTrue(options.hits)


class Search(TestCase):

    def setUp(self):
        cli.News = Mock()
        core.req = Mock()
        core.json = Mock()
        cli.present = Mock()

    def create_cli(self, args):
        parser = cli.create_parser()
        options = parser.parse_args(args.split(' '))
        cli.search(options)

    def assertSearchParameters(self, **params):
        cli.News().get.assert_called_with(**params)

    def test_basic_search_term(self):
        self.create_cli('zachwill')
        self.assertSearchParameters(q='zachwill')

    def test_multiple_search_terms(self):
        self.create_cli('one two three')
        self.assertSearchParameters(q='one two three')

    def test_limit_and_start_options(self):
        self.create_cli('github -n 100 -s 200')
        self.assertSearchParameters(q='github', limit=100, start=200)

    def test_sortby_parameter(self):
        self.create_cli('pg -S points')
        self.assertSearchParameters(q='pg', sortby='points desc')


if __name__ == '__main__':
    main()
    # params = {"sortby": "points desc", "limit": 100, "start": 100}
    # params = {"filter[fields][create_ts]": "[2011-06-01T00:00:00.00Z TO 2011-06-02T23:59:00.00Z]"}
