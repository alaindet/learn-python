print(f'Running {__name__}')

import os.path
import types
import sys

def main() -> None:
    """
    This function manually loads a module from a Python file to demonstrate how
    Python roughly does it
    """
    mod_name = 'bar' # The module name *SHOULD* be the same as the file name, this is different for example's sake
    mod_file = 'foo.py'
    mod_path = '.'
    mod_rel_path = os.path.join(mod_path, mod_file)
    mod_abs_path = os.path.abspath(mod_rel_path)
    source_code = ''

    with open(mod_rel_path, 'r') as code_file:
        source_code = code_file.read()

    mod = types.ModuleType(mod_name)
    mod.__file__ = mod_abs_path
    sys.modules[mod_name] = mod

    code: types.CodeType = compile(source_code, filename=mod_abs_path, mode='exec')
    exec(code, mod.__dict__)

    # Run code from the external module
    print(mod.foo())

if __name__ == '__main__':
    main()