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