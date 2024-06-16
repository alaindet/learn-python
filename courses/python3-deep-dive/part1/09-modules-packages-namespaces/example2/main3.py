print(f'Running {__name__}')

import importer

def main() -> None:
    """
    This function manually loads a module from a Python file to demonstrate how
    Python roughly does it
    """
    mod = importer.import_module('bar', 'foo.py', '.')
    print(mod.foo())

if __name__ == '__main__':
    main()