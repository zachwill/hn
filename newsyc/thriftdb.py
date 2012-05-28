"""
ThriftDB API:  http://www.thriftdb.com/documentation/rest-api/search-api

Turn a dictionary of sane key-value pairs to the somewhat crazy ThriftDB
key-value parameters.
"""


def convert(data):
    """Where the conversion magic happens."""
    if 'day' in data:
        # Should be in YYYY-MM-DD format
        key = 'filter[fields][create_ts]'
        date = data.pop('day')
        value = "[%sT00:00:00Z TO %sT23:59:59Z]" % (date, date)
        data[key] = value
    if 'type' in data:
        # The type can't be plural (i.e. comments, submissions).
        key = 'filter[fields][type]'
        data[key] = data.pop('type').rstrip('s')
    if 'username' in data:
        data['filter[fields][username]'] = data.pop('username')
    return data
