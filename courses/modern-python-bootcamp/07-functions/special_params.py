"""\
Special parameters
https://docs.python.org/3/tutorial/controlflow.html#special-parameters

In Python, you can use the special function parameters / and * to enforce
positional-only parameters and/or keyword-only parameters

From the docs
def fn(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
       -----------    ----------     ----------
         |             |                  |
         |             |- Positional or   |
         |                keyword         |- Keyword only
         |
         |-Positional only

If no special parameters are used, parameters can be passed either by position or
by keyword
"""


def with_standard_arg(arg):
    print(arg)


def with_position_only_arg(arg, /):
    print(arg)


def with_keyword_only_arg(*, arg):
    print(arg)


def use_all_special_params(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
