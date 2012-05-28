hn
==

A CLI and Python library for [HNSearch's
API](http://www.hnsearch.com/api) that's easy-to-use.


Installation
------------

From the command line, run the following:

```bash
python setup.py install
```


Usage
-----

### Search

Basic search terms and querying. Allows for specifying number of results
with `n` flag (maximum is 100), and starting ordinal position of results
with the `s` flag.

```bash
hn search term
hn search term -n 100
hn search term -n 100 -s 100
```

### Date

The `d` flag allows for searchs filtered to a specific date (in
`YYYY-MM-DD` format).

```bash
hn -d 2012-03-16
hn github -d 2012-01-01
```

### Sorting

By default, sorting will be descending.

```bash
hn techcrunch -S points
hn -d 2012-03-16 -S username asc
```

### Type

The `T` flag allows filtering by specific types of items (comment or
submission).

```bash
hn zachwill -T comment
hn zachwill -T submission -S points
```

### Hits

Return the number of results encountered with the `--hits` flag.

```bash
hn pg --hits
hn zachwill --hits
```
