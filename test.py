"""
Tests and such.
"""

from unittest import TestCase, main
from mock import Mock

from yc import cli
from yc import core
from yc import times
from yc import thriftdb
from yc.times import date_format, hour_format


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
        cli.present = Mock()
        times.date_format = Mock()

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

    def test_date_filtering(self):
        self.create_cli('-d 2012-03-16')
        self.assertSearchParameters(day='2012-03-16')
        self.create_cli('-d 03-16-12')
        self.assertSearchParameters(day='2012-03-16')

    def test_date_and_hour_options(self):
        self.create_cli('-d 03-16-12 -t 0 12')
        self.assertSearchParameters(day='2012-03-16', time=['0', '12'])

    def test_sortby_parameter(self):
        self.create_cli('pg -S points')
        self.assertSearchParameters(q='pg', sortby='points desc')


class DateFormat(TestCase):

    def test_year_month_day(self):
        self.assertEquals(date_format('2012-03-16'), '2012-03-16')

    def test_month_day_year(self):
        self.assertEquals(date_format('03-16-12'), '2012-03-16')


class HourFormat(TestCase):

    def test_one_letter_string(self):
        self.assertEquals(hour_format('0'), '00:00:00')

    def test_two_letter_string(self):
        self.assertEquals(hour_format('12'), '12:00:00')

    def test_twelve_hour_clock_with_length_of_three(self):
        self.assertEquals(hour_format('1am'), '01:00:00')
        self.assertEquals(hour_format('1pm'), '13:00:00')

    def test_twelve_hour_clock_with_length_of_four(self):
        self.assertEquals(hour_format('12am'), '00:00:00')
        self.assertEquals(hour_format('12pm'), '12:00:00')
        self.assertEquals(hour_format('03pm'), '15:00:00')


if __name__ == '__main__':
    main()
