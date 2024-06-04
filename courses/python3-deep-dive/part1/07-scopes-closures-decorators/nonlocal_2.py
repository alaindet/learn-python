def outer():
    x = 'hello'

    def inner1():
        x = 'monty'

        def inner2():
            nonlocal x
            x = 'python'

        print('inner1(before)', x)  # inner1(before) monty
        inner2()
        print('inner1(after)', x)  # inner1(after) python

    inner1()
    print('outer', x)  # outer hello


outer()
