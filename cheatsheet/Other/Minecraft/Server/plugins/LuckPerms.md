`lp <user|group> <playername> permission <set|unset> <permission> <true|false>`
`lp <user|group> <playername> parent <add|remove|addtemp|removetemp> <permission> <true|false>`
`lp verbose command <playername> <command>`

# Placeholders
|                                                  |
|--------------------------------------------------|
| `%luckperms_prefix%`                             |
| `%luckperms_suffix%`                             |
| `%luckperms_meta_<metakey>%`                     |
| `%luckperms_prefix_element_<element>%`           |
| `%luckperms_suffix_element_<element>%`           |
| `%luckperms_context_<contextkey>%`               |
| `%luckperms_groups%`                             |
| `%luckperms_primary_group_name%`                 |
| `%luckperms_has_permission_<permission>%`        |
| `%luckperms_inherits_permission_<permission>%`   |
| `%luckperms_check_permission_<permission>%`      |
| `%luckperms_in_group_<group>%`                   |
| `%luckperms_inherits_group_<group>%`             |
| `%luckperms_on_track_<track>%`                   |
| `%luckperms_has_groups_on_track_<track>%`        |
| `%luckperms_highest_group_by_weight%`            |
| `%luckperms_lowest_group_by_weight%`             |
| `%luckperms_first_group_on_tracks_<tracks>%`     |
| `%luckperms_last_group_on_tracks_<tracks>%`      |
| `%luckperms_expiry_time_<permission>%`           |
| `%luckperms_inherited_expiry_time_<permission>%` |
| `%luckperms_group_expiry_time_<groupname>%`      |

# config
### server
Поставить `global` чтобы игнорировать контекст сервера
```yml
server: global
```
Чтобы учитывать контекст
```yml
server: servername
```
```yml
storage-method: MariaDB
```
