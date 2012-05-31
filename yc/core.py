"""
Core functionality for interacting with the HNSearch API.
"""

import requests as req
import simplejson as json

from . import thriftdb
from .times import date_format


class News(object):

    def __init__(self):
        self.url = "http://api.thriftdb.com/api.hnsearch.com/items/_search"

    def get(self, **params):
        """Perform a GET request."""
        params = thriftdb.convert(params)
        data = req.get(self.url, params=params)
        self.request = data
        return json.loads(data.content)

    def date(self, day, **params):
        """Query a specific date."""
        params['day'] = date_format(day)
        return self.get(**params)

    def facet(self, term, **params):
        """Facets are almost like searching what can be searched."""
        params['facet'] = term
        return self.get(**params)

    def filter(self, condition, **params):
        """Filter the results to a specific condition."""
        params['filter'] = condition
        return self.get(**params)

    def search(self, term, **params):
        """Perform a search against the HNSearch API."""
        params['q'] = term
        return self.get(**params)
