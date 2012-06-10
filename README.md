hn
==

An easy-to-use CLI and Python library for [HNSearch's
API](http://www.hnsearch.com/api).


Installation
------------

There are two ways of installing the library:

```
pip install hn
```

Alternatively, run the following from the command line:

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

The `d` flag allows for searches filtered to a specific date (in
`YYYY-MM-DD` or `MM-DD-YY` format).

```bash
hn -d 03-16-12
hn -d 2012-03-16

hn github -d 2012-03-16
hn techcrunch -d 03-16-12
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

### Time

In addition to filtering by date creation, you can specify the hours to
search within on the specific day.

```bash
hn -d 03-16-12 -t 0 12
hn -d 03-16-12 -t 13 23

hn -d 03-16-12 -t 12am 12pm
hn -d 03-16-12 -t 1pm 11pm
```

### Type

The `T` flag allows filtering by specific types of items (comment or
submission).

```bash
hn zachwill -T comment
hn zachwill -T submission -S points -n 100
```

### Username

The `u` or `U` flags allows filtering by a specific username.

```bash
hn -U zachwill
hn ycombinator -U pg

hn -U pg -T submission -S points
hn -U pg -T comment -S points asc
```
