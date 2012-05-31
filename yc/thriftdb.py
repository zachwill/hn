"""
ThriftDB API:  http://www.thriftdb.com/documentation/rest-api/search-api

Turn a dictionary of sane key-value pairs to the somewhat crazy ThriftDB
key-value parameters.
"""

from .times import hour_format


def convert(data):
    """Where the conversion magic happens."""
    if 'day' in data:
        key = 'filter[fields][create_ts]'
        date = data.pop('day')
        if 'time' in data:
            start, end = data['time']
            start = hour_format(start)
            end = hour_format(end)
        else:
            start = '00:00:00'
            end = '23:59:59'
        value = "[%sT%sZ TO %sT%sZ]" % (date, start, date, end)
        data[key] = value
    if 'type' in data:
        # The type can't be plural (i.e. comments, submissions).
        key = 'filter[fields][type]'
        data[key] = data.pop('type').rstrip('s')
    if 'username' in data:
        value = data.pop('username')
        data['filter[fields][username]'] = value
    return data
