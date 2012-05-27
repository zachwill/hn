Usage I see for the CLI going forward.

### search

Basic search terms and querying.

```
hn search term
hn search term -n 100
```


### dates

```
hn -d 03-16-12
hn -d 2012-03-16

hn -d 031612
hn -d 20120316

hn -d 03-16-12 -t 0 12
hn -d 03-16-12 -t 12am 12pm
```


### filter

```
hn -x color=black
```


### facet

Has a default facet limit of 10.

```
hn -c domain

hn -c domain -n 50
```


### sortby

By default, will be descending.

```
hn techcrunch -s points

hn -d 03-16-12 -s username asc
```


### all

Magic to make your life easier. Queries can only return 100 results at a
time, and a maximum limit of 1,000 results in total (although there may
be significantly more hits).

The `--all` flag goes about returning the results you want in the best
way possible.

```
hn -d 03-16-12 --all
```