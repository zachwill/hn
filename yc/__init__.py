from .core import News


def get(**params):
    """Perform a GET request against the HNSearch API."""
    return News().get(**params)


def day(date, **params):
    """Search a specific date."""
    return News().date(date, **params)


def date(date, **params):
    """Search a specific date."""
    return News().date(date, **params)


def between(self, start, finish, **params):
    """Search between two specific datetimes."""
    return News().between(start, finish, **params)


def search(term, **params):
    """Query the HNSearch API."""
    return News().search(term, **params)
