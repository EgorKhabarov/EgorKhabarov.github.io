copied from [https://www.sqlite.org/lang_datefunc.html](https://www.sqlite.org/lang_datefunc.html)

## Overview
SQLite supports seven scalar date and time functions as follows:

1. `date(time-value, modifier, modifier, ...)`  `YYYY-MM-DD`
2. `time(time-value, modifier, modifier, ...)`  `HH:MM:SS` or as `HH:MM:SS.SSS`
3. `datetime(time-value, modifier, modifier, ...)`  `YYYY-MM-DD HH:MM:SS` or as `YYYY-MM-DD HH:MM:SS.SSS`
4. `julianday(time-value, modifier, modifier, ...)`  - the fractional number of days since noon in Greenwich on November 24, 4714 B.C.
5. `unixepoch(time-value, modifier, modifier, ...)`  unix timestamp
6. `strftime(format, time-value, modifier, modifier, ...)`
7. `timediff(time-value, time-value)`

|      |                                                             |
|------|-------------------------------------------------------------|
| `%d` | day of month: `01-31`                                       |
| `%e` | day of month without leading zero: `1-31`                   |
| `%f` | fractional seconds: SS.SSS                                  |
| `%F` | ISO 8601 date: `YYYY-MM-DD`                                 |
| `%G` | ISO 8601 year corresponding to `%V`                         |
| `%g` | 2-digit ISO 8601 year corresponding to `%V`                 |
| `%H` | hour: `00-24`                                               |
| `%I` | hour for 12-hour clock: `01-12`                             |
| `%j` | day of year: `001-366`                                      |
| `%J` | Julian day number (fractional)                              |
| `%k` | hour without leading zero: `0-24`                           |
| `%l` | %I without leading zero: `1-12`                             |
| `%m` | month: `01-12`                                              |
| `%M` | minute: `00-59`                                             |
| `%p` | `AM` or `PM` depending on the hour                          |
| `%P` | `am` or `pm` depending on the hour                          |
| `%R` | ISO 8601 time: `HH:MM`                                      |
| `%s` | seconds since `1970-01-01`                                  |
| `%S` | seconds: `00-59`                                            |
| `%T` | ISO 8601 time: `HH:MM:SS`                                   |
| `%U` | week of year (`00-53`) - week 01 starts on the first Sunday |
| `%u` | day of week `1-7` with Monday==1                            |
| `%V` | ISO 8601 week of year                                       |
| `%w` | day of week `0-6` with Sunday==0                            |
| `%W` | week of year (`00-53`) - week 01 starts on the first Monday |
| `%Y` | year: `0000-9999`                                           |
| `%%` | `%`                                                         |

| Function         | Equivalent `strftime()`             |
|------------------|-------------------------------------|
| `date(...)`      | `strftime('%F', ...)`               |
| `time(...)`      | `strftime('%T', ...)`               |
| `datetime(...)`  | `strftime('%F %T', ...)`            |
| `julianday(...)` | `CAST(strftime('%J', ...) as REAL)` |
| `unixepoch(...)` | `CAST(strftime('%s', ...) as INT)`  |

```sql
SELECT timediff('2023-02-15', '2023-03-15');
```

## Time Values
A time-value can be in any of the following formats shown below.
The value is usually a string, though it can be an integer or floating point number in the case of format 12.

1. `YYYY-MM-DD`
2. `YYYY-MM-DD HH:MM`
3. `YYYY-MM-DD HH:MM:SS`
4. `YYYY-MM-DD HH:MM:SS.SSS`
5. `YYYY-MM-DDTHH:MM`
6. `YYYY-MM-DDTHH:MM:SS`
7. `YYYY-MM-DDTHH:MM:SS.SSS`
8. `HH:MM`
9. `HH:MM:SS`
10. `HH:MM:SS.SSS`
11. `now`
12. `DDDDDDDDDD`


## Modifiers
For all date/time functions other than `timediff()`, the time-value argument can be followed by zero or more modifiers that alter date and/or time.
Each modifier is a transformation that is applied to the time-value to its left.
Modifiers are applied from left to right; order is important.
The available modifiers are as follows.

1. `NNN days`
2. `NNN hours`
3. `NNN minutes`
4. `NNN seconds`
5. `NNN months`
6. `NNN years`
7. `±HH:MM`
8. `±HH:MM:SS`
9. `±HH:MM:SS.SSS`
10. `±YYYY-MM-DD`
11. `±YYYY-MM-DD HH:MM`
12. `±YYYY-MM-DD HH:MM:SS`
13. `±YYYY-MM-DD HH:MM:SS.SSS`
14. `ceiling`
15. `floor`
16. `start of month`
17. `start of year`
18. `start of day`
19. `weekday N`
20. `unixepoch`
21. `julianday`
22. `auto`
23. `localtime`
24. `utc`
25. `subsec`
26. `subsecond`
