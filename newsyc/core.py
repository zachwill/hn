"""
Core functionality for interacting with the HNSearch API.
"""

from collections import Iterable
import requests as req
import simplejson as json
from .date import Date


class YCombinator(object):

    def __init__(self):
        self.url = "http://api.thriftdb.com/api.hnsearch.com/items/_search"

    def get(self, params):
        data = req.get(self.url, params=params)
        self.request = data
        # Use json.loads
        return data.content

    def _convert_date(self, date):
        """Convert a given date to the proper format."""
        if isinstance(date, str):
            # Check it's length -- YYYY-MM-DD vs MM-DD-YY
            print date
        elif isinstance(date, Iterable):
            # then it's an iterable
            print date
        else:
            # it's a datetime
            print date
        return date

    def dates(self, start, end):
        """Query between two dates."""
        start = self._convert_date(start)
        end = self._convert_date(end)

    def hours(self, date, start, end):
        """Query a day by specific hours."""
        return "hours"
