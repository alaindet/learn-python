class Utils:

    def override_me(self):
        print('Utils: override_me')

    def i_am_implicit(self):
        print('Utils: i_am_implicit')

    def alter_this(self):
        print('Utils: alter_this')


class Something:

    def __init__(self):
        self.utils = Utils()

    def override_me(self):
        print('Something: override_me')

    def i_am_implicit(self):
        self.utils.i_am_implicit()

    def alter_this(self):
        print('Something: alter_this before')
        self.utils.alter_this()
        print('Something: alter_this after')


smt = Something()
smt.override_me()
smt.i_am_implicit()
smt.alter_this()
