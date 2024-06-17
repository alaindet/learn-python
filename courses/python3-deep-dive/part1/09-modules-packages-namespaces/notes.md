# Modules, Packages and Namespaces

- Modules spawn from Python files (not only) that become objects of type `ModuleType` at runtime
- A namespace is just a dictionary containing non-conflicting names for variables
- Once a module is loaded, it gets loaded in the system cache and only referenced
in files, meaning all files are pointing to the same module in memory and subsequent
loadings (or re-loadings) just hit the cache
- `sys.path` should contain the `__main__` script's containing directory as its
first loading path

The module loading algorithm looks like this
- Check the `sys.modules` for cached modules
- Locates the file (Checks all paths in the `sys.path` list, then fails)
- Creates a new `types.ModuleType` if needed
- Loads the source code from the file
- Adds an entry into `sys.modules` to avoid loading it again
- Compiles and executes any source contained in the module
- **NOTE**: Any imported module runs its code at least once!

## Importer
- An importer in Python is the combination of
  - a **finder**: a piece of code which searches for a given file based on some conventions
  - a **loader**: a piece of code loading the source code from the file system into the runtime
- For example, finders could extract source code from a `.zip` files

### Finder
- A finder returns a "module specification" of type `ModuleSpec`, accessible on existing modules via the `__spec__` property
- The spec contains the specifics on how the Python runtime should load the found module, including the name, what loader to use and the absolute path of the file containing the source code

```py
import fractions

print(fractions.__spec__)
# ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001D3A7BB60F0>, origin="<MY_INSTALLATION_PATH>\\Lib\\fractions.py")
```