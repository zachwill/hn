from .core import News
from .date import Date


def get(**params):
    """Perform a GET request against the HNSearch API."""
    return News().get(**params)


def search(term, **params):
    """Query the HNSearch API."""
    return News().search(term, **params)
