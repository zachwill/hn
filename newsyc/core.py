"""
Core functionality for interacting with the HNSearch API.
"""

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

    def date(self, day):
        """Query a specific date."""
        day = Date(day)

    def hours(self, day, start, end):
        """Query a day by specific hours."""
        date = Date(day)
        start = date.hour(start)
        end = date.hour(end)

    def facet(self, term):
        """Facets are almost like searching what can be searched."""
        return "facet"

    def filter(self, condition):
        """Filter the results to a specific condition."""
        return "filter"
