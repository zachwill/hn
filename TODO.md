Usage I see for the CLI going forward.


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
