"""
Abstractions for dealing with dates. I don't know if you knew this, but dealing
with dates and times in Python kind of blows.
"""

import datetime
from collections import Iterable


def date_format(date):
    """Convert the given input to a date."""
    if isinstance(date, str):
        if '-' not in date:
            if len(date) == 8:
                # It's a YYYYMMDD date.
                year = date[:4]
                month = date[4:6]
                day = date[6:]
                date = "%s-%s-%s" % (year, month, day)
            else:
                # Then it's MMDDYY.
                year = date[4:]
                month = date[:2]
                day = date[2:4]
                date = "20%s-%s-%s" % (year, month, day)
        elif len(date) == 8:
            # Then it's in MM-DD-YY format.
            month, day, year = date.split('-')
            date = "20%s-%s-%s" % (year, month, day)
    elif isinstance(date, Iterable):
        date = '-'.join(str(n) for n in date)
    else:
        date = date.strtime("%Y-%m-%d")
    return date


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
