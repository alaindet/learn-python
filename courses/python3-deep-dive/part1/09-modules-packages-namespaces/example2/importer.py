print(f'Running {__name__}')

import os.path
import types
import sys

def import_module(mod_name: str, mod_file: str, mod_path: str):
    if mod_name in sys.modules:
        return sys.modules[mod_name]

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
    return sys.modules[mod_name]