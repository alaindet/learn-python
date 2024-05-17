# In this example we create a circular dependency and run garbage collection manually

import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return 'Object exists'
    return 'Object not found'


def addr(the_var) -> int:
    return id(the_var)


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self: {addr(self)}, b: {addr(self.b)}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'B: self: {addr(self)}, a: {addr(self.a)}')


def manual_garbage_collection_example():
    gc.disable()  # <-- Important bit here!

    my_a = A()
    a_id = addr(my_a)
    b_id = addr(my_a.b)
    print('a address:', a_id)
    print('b address:', b_id)
    print('a refcount:', ref_count(a_id))  # a refcount: 2
    print('b refcount:', ref_count(b_id))  # b refcount: 1
    print('a exists:', object_by_id(a_id))  # a exists: Object exists
    print('b exists:', object_by_id(b_id))  # b exists: Object exists

    # After removing my_a (assigning it to None), the garbage collector does not
    # release its memory address because of gc.disable() statement above
    my_a = None
    print('----- Removed the my_a variable -----')
    print('a refcount:', ref_count(a_id))  # a refcount: 1
    print('b refcount:', ref_count(b_id))  # b refcount: 1
    print('a exists:', object_by_id(a_id))  # a exists: Object exists
    print('b exists:', object_by_id(b_id))  # b exists: Object exists

    # Here, we're running the garbage collector manually and imperatively
    gc.collect()

    print('----- Run GC manually -----')
    print('a refcount:', ref_count(a_id))  # a refcount: 0
    print('b refcount:', ref_count(b_id))  # b refcount: 0
    print('a exists:', object_by_id(a_id))  # a exists: Object not found
    print('b exists:', object_by_id(b_id))  # b exists: Object not found


def main() -> None:
    manual_garbage_collection_example()


if __name__ == '__main__':
    main()
