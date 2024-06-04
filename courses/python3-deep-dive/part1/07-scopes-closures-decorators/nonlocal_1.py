a = 1


def outer():
    """
    Runs an inner variable fiddling with scopes
    """
    b = 2

    def inner():
        """
        Changes both the global 'a' and the nonlocal 'b'
        """
        global a
        a = 10

        nonlocal b
        b = 20

    inner()
    print(a, b)  # 10 20


outer()
