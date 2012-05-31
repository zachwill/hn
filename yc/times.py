"""
Abstractions for dealing with dates. I don't know if you knew this, but dealing
with dates and times in Python kind of blows.
"""

import datetime
from collections import Iterable


class Date(object):

    def __init__(self, date):
        self._d = date
        self._date = self._convert_date(date)

    def _convert_date(self, date):
        """Convert the given input to a date."""
        if isinstance(date, str):
            date = self._convert_string(date)
        elif isinstance(date, Iterable):
            date = '-'.join(str(n) for n in date)
        else:
            # it's a datetime
            print date
        return date

    def _convert_string(self, date):
        """Convert a string to the right format."""
        if '-' not in date:
            # It has no separating dashes.
            print "No dashes"
        elif len(date) == 8:
            # Then it's in MM-DD-YY format.
            month, day, year = date.split('-')
            date = '20%s-%s-%s' % (year, month, day)
        return date

    def __str__(self):
        return self._date

    def __repr__(self):
        return self.__str__()


def hour_format(hour):
    """Turn an string into the correct HNSearch API format."""
    hour = hour.lower()
    length = len(hour)
    if length == 1:
        formatted = "0%s:00:00" % hour
    elif length == 2:
        formatted = "%s:00:00" % hour
    else:
        time = hour[-2:]
        hour = hour[:-2]
        if length == 3:
            if time == 'am':
                formatted = "0%s:00:00" % hour
            else:
                hour = str(int(hour) + 12)
                formatted = "%s:00:00" % hour
        else:
            if time == 'am' and hour == '12':
                hour = '00'
            elif time == 'pm' and hour.startswith('0'):
                hour = str(int(hour) + 12)
            formatted = "%s:00:00" % hour
    return formatted
