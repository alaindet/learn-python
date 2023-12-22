def take_just_two(*args):
    arg1, arg2, *the_rest = args
    print(f'arg1: {arg1}, arg2: {arg2}')


def take_only_two(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')


def too_many_arguments(
  arg1,
  arg2,
  arg3,
  arg4,
  arg5,
  arg6,
  arg7,
  arg8,
  arg9,
  arg10,
):
  print('You passed a lot of arguments')


take_just_two(1, 2, 3, 4)

# This raises a TypeError since it only accepts two arguments
# take_only_two(1, 2, 3, 4)

too_many_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
