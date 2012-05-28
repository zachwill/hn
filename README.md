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


CLI
-----

Usage patterns for working with the `hn` CLI.

### Search

Basic search terms and querying. Allows for specifying number of results
with `n` flag (maximum is 100), and starting ordinal position of results
with the `s` flag.

```bash
hn term
hn multiple terms -n 100
hn multiple terms -n 100 -s 100
```

### Date

The `d` flag allows for searchs filtered to a specific date (in
`YYYY-MM-DD` or `MM-DD-YY` format).

```bash
hn -d 03-16-12
hn -d 2012-03-16
hn github -d 2012-03-16
```

### Hits

Return the number of results encountered with the `--hits` flag.

```bash
hn pg --hits
hn zachwill --hits
```

### Sorting

By default, sorting will be descending (though both `asc` and `desc` can
be used).

```bash
hn github -S points
hn github -S username desc
hn -d 03-16-12 -S username asc -n 100
```

### Type

The `T` flag allows filtering by specific types of items (comment or
submission).

```bash
hn zachwill -T comment
hn zachwill -T submission -S points -n 100
```

### Username

The `U` flag allows filtering by a specific username.

```bash
hn -U zachwill
hn -U pg -T submission -S points
hn -U pg -T comment -S points asc
```
