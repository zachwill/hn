Usage I see for the CLI going forward.



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
hn -x username=zachwill
```


### ignore

```
hn pg -X type=comment
hn github -X username=zachwill type=submission
```


### facet

Has a default facet limit of 10.

```
hn -c domain

hn -c domain -n 50
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
