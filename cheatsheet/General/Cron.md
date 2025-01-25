# Format

```
Min  Hour Day  Mon  Weekday
*    *    *    *    *  command to be executed
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)
```

# Operators

|     |                            |
|-----|----------------------------|
| `*` | All values                 |
| `,` | Separate individual values |
| `-` | A range of values          |
| `/` | Divide a value into steps  |


# Crontab

```
# Adding tasks easily
echo "@reboot echo hi" | crontab

# Open in editor - optional for another user
crontab -e [-u user]

# List tasks - optional for another user
crontab -l [-u user]

# Delete crontab file - optional for another user
crontab -r [-u user]
```

# Special strings

|             |                                        |
|-------------|----------------------------------------|
| `@reboot`   | Every rebot                            |
| `@hourly`   | Once every hour - same as `0 * * * *`  |
| `@daily`    | Once every day - same as `0 0 * * *`   |
| `@midnight` | Once every midnight - same as `@daily` |
| `@weekly`   | Once every week - same as `0 0 * * 0`  |
| `@monthly`  | Once every month - same as `0 0 1 * *` |
| `@yearly`   | Once every year - same as `0 0 1 1 *`  |


# Examples

|                |                             |
|----------------|-----------------------------|
| `0 * * * *`    | Every hour                  |
| `*/15 * * * *` | Every 15 mins               |
| `0 */2 * * *`  | Every 2 hours               |
| `0 18 * * 0-6` | Every week Mon-Sat at 6pm   |
| `10 2 * * 6,7` | Every Sat and Sun on 2:10am |
| `0 0 * * 0`    | Every Sunday midnight       |
