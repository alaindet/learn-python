from typing import Any, Dict


print(f'----- Start of module: {__name__} -----')

def pprint_dict(header: str, d: Dict[str, Any]):
    print('\n\n----------')
    print(f'# {header}')

    for key, value in d.items():
        print(key, value)

    print('----------\n\n')


# pprint_dict('module1.globals', globals())
print(f'----- End of module: {__name__} -----')