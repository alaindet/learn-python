x = 100


def outer():
    x = 'python'

    def inner1():
        nonlocal x
        x = 'monty'

        def inner2():
            global x
            x = 'hello'

        print('inner(before)', x)  # inner(before) monty
        inner2()
        print('inner(after)', x)  # inner(before) monty

    inner1()
    print('outer', x)  # outer monty


outer()
print(x)  # hello
