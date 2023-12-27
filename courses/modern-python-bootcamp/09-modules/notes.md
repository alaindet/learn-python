# Modules

- A module is any Python file
- Usually, modules have definitions (functions, variables) you can use in other modules
- A "script" is just a runnable file with statements that should not be imported
- Python ships with more than 200 built-in standard modules  (298 as of Python 3.12 on Windows 11)
- Golden rule: never import stuff you don't need!
- The **main** module is just the module you're running
- Any Python module takes its name from the file name (apart from the *main* module) without the `.py` extension
- Any Python modules has a `__name__` special attribute holding its name
- It's a common practice to use this bit of code on modules you run directly
  ```py
  if __name__ == 'main':
      # Run the scripting part of this file
  ```
- Executable code from modules should be treated as initialization code only
- A Python module has its own private **namespace** containing all its definitions
- Using the `import` statement, you can import other modules' namespaces into the
importing module
- A naked import statement, ex.: `import math`, makes all definitions from the `math` module available in the importing module through the `math` variable, so no external definition "leaks" into the importing module's namespace, since they're attributes of the `math` variable
- Import statements can declare as alias to shorten a module's name or avoid conflicts, ex.: `import math as m`
- A full import statement, ex.: `from math import fsum`, imports the `fsum` functions directly into the importing module's namespace. It is recommended as it's more explicit and light compared to loading every definition from an external module, even if you're "polluting" the importing module's namespace
- An alternate import statement allows you to have **all** definitions from the imported module into the importing module's namespace, "polluting" it with everything defined into the imported module. Syntax is `from math import *`
- **NOTE**: `from mymodule import *` imports every definition **except** those starting with `_`

## Packages

- Packages are a collection of modules used to organize related modules
- Packages can contain other packages infinitely
- Packages (or infinitely nested sub-packages) can then contain modules
- A package is just a directory containing a (usually empty) `__init__.py` file
- `__init__.py` tells Python that dir is a package
- `__init__.py` can contain common initialization code for the whole package, tests or documentaion

## Module searching algorithm
- When importing a module `foo`, Python follows this algorithm
  1. Search for an existing buil-in package named `foo`
  2. Search for a file named `foo.py` in the main module's directory
  3. Search for module or package named `foo` from the `PYTHONPATH` environment variable
  4. Search for module or package named `foo` from installation-dependent defaults

## Intra-package relative imports

- Modules can import other modules from the same package via relative imports
- Ex.:
  ```py
  from . import echo # Imports echo module from the same dir
  from .. import formats # Imports formats package from sibling dir formats
  from ..filters import equalizer # Imports equalizer module from sibling dir filters
  ```
- Intra-package relative imports work based on the importing module's name
- For this reason, when running a module directly, you **CANNOT** use relative imports since `__name__ == 'main'` is always true

## Example

```
# Filesystem tree of a package with sub-packages

my_orm/
    __init__.py         # The init file for the whole my_orm package
    drivers/            # The 'drivers' sub-package
        __init__.py
        postgresql.py   # my_orm.drivers.postgresql module   
        mysql.py
        sqlite.py
        ...
    core/
        __init__.py
        connect.py
        query.py
    models/
        __init__.py
        ...
```

```py
from my_orm.core import connect

connect()
```

## References
- https://docs.python.org/3/tutorial/modules.html
- https://docs.python.org/3/py-modindex.html
- https://docs.python.org/3/tutorial/modules.html#packages
