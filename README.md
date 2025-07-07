...

## 10. Modules & Packages

| Concept   | Example                          | Key Points                                   |
|-----------|----------------------------------|----------------------------------------------|
| Module    | `import math`                    | A .py file with Python code (functions, etc) |
| Importing | `from os import path`            | Use `import` or `from ... import ...`        |
| Custom    | `import mymodule`                | Place mymodule.py in the same folder         |
| Package   | Folder with `__init__.py`        | Organizes modules; can be nested             |
| Use Case  | `from pkg.subpkg import mod`     | Import from sub-packages                     |
| Aliasing  | `import numpy as np`             | Shorten module/package name                  |
| `dir()`   | `dir(math)`                      | Lists module attributes                      |
| `as`      | `import pandas as pd`            | Alias for easier access                      |

### Quick Example

**Directory Structure:**
```
myproject/
├── main.py
├── utils/
│   ├── __init__.py
│   └── helper.py
```

**In main.py**
```python
from utils import helper
helper.some_function()
```

**In utils/helper.py**
```python
def some_function():
    print("Hello from helper!")
```

---

Add this section to your README to keep your ShortNote book comprehensive!
