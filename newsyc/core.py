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

    def dates(self, start, end):
        """Query between two dates."""
        start = Date(start)
        end = Date(end)

    def hours(self, day, start, end):
        """Query a day by specific hours."""
        date = Date(day)
        start = date.hour(start)
        end = date.hour(end)
