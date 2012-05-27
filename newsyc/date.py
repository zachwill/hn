"""
Abstractions for dealing with dates. I don't know if you knew this, but dealing
with dates and times in Python kind of blows.
"""

import datetime
from collections import Iterable


class Date(object):

    def __init__(self, date):
        self._d = date

    def _convert_date(self):
        """Convert the given input to a date."""
        date = self._d
        if isinstance(date, str):
            # Check it's length -- YYYY-MM-DD vs MM-DD-YY
            print date
        elif isinstance(date, Iterable):
            # then it's an iterable
            print date
        else:
            # it's a datetime
            print date

    def __str__(self):
        return 'YYYY-MM-DD'

    def __repr__(self):
        return self.__str__()
