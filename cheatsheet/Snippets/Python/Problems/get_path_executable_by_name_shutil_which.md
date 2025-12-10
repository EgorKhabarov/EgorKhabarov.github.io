```python
# SOURCE: https://docs.python.org/3.7/library/shutil.html#shutil.which


import shutil


for name in ("python", "java", "cmd", "git", "svn"):
    path = shutil.which(name)
    print(f"{name:10} {path}")
```
