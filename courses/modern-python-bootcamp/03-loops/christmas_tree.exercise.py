"""\
Given an integer N, draw a Christmas Tree in the console like the examples below

Example 1
=========

N = 1 outputs

  |
* | *


Example 2
=========

N = 3 outputs

    |    
  * | *  
 ** | ** 
*** | ***
"""


def christmas_tree(n: int) -> str:

    if n == 0:
        return ''

    lines = []
    air = ' '
    leaves = '*'
    stem = ' | '

    for i in range(n + 1):
        left_branch = air * (n - i) + leaves * i
        right_branch = leaves * i + air * (n - i)
        line = left_branch + stem + right_branch
        lines.append(line)

    return '\n'.join(lines)


for n in range(10):
    print(f'n = {n}')
    print(christmas_tree(n))
    print('\n')
