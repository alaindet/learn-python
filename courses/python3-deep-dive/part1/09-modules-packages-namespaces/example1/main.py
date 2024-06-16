print('This runs before the content of module1.py')

# import module1
import sys
import module1
import module1 # <-- This does not run module1.py again
del globals()['module1'] # <-- This soft-removes the loaded module
import module1 # <-- This does not complain, but DOESN'T re-run the module

def main() -> None:
    print('main.py')
    module1.pprint_dict('Header', {
        'foo': 1,
        'bar': 2,
        'baz': 3,
    })

if __name__ == '__main__':
    main()