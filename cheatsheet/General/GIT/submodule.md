# Submodule

```bash
git submodule add <link> <path>
```

```bash
git submodule update --remote
```

Настройть на отслеживание ветки

```bash
git checkout mybranch
cd ..
git config -f .gitmodules submodule.<path>.branch mybranch
```

Обновить

```bash
git submodule update --remote --init
```
