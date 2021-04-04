class Parent:

    def override_me(self):
        print('Parent: override_me')

    def i_am_implicit(self):
        print('Parent: i_am_implicit')

    def alter_this(self):
        print('Parent: alter_this')


class Child(Parent):

    def override_me(self):
        print('Child: override_me')

    def alter_this(self):
        print('Child: alter_this before')
        super(Child, self).alter_this()
        print('Child: alter_this after')


dad = Parent()
son = Child()

dad.i_am_implicit()
son.i_am_implicit()

dad.override_me()
son.override_me()

dad.alter_this()
son.alter_this()
