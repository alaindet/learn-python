# Scope

- The scope is just a registry where variables and definitions are stored and
accessible from other pieces of code in the same scope
- The scope is just the concept, while the **namespace** is the actual
implementation of said registry

## Global scope
- Also called *module scope*, it's the scope of an entire file (file == module)
- It's called "global" since Python used to be only used for scripting, so one
script equals one file equals there's only one "module scope", hence "global"
- There's no scope that encompasses multiple files

## Built-in scope
- It's a cross-file-ish scope where Python declares `True`, `False`, `None` and
such constants, as well as built-in functions like `print()` and `sum()`
- The global scopes of files are encapsulated inside the built-in scope
- Python *resolves* scopes from the closest up to the parents. Ex.:
  - Function scope
  - Module scope
  - Built-in scope
- If Python cannot find a definition/variable after this, it fails

## Local scope
- It's the current function's scope
- Every time a function is called, a local scope is created and then destroyed
- Any variable/definition declared in a local scope is bound to it
- Any parameter gets initially assigned the given arguments, and then those
parameters are bound to the local scope

For example
```py
def fn(a, b):
    c = a * b
    return c

fn(10, 20) # This creates a new local scope with a=10, b=20, c=200
fn('@', 5) # This creates a new local scope with a='@', b=5, c='@@@@@'
```

## Nonlocale scope

- Imagine a function declaring another function inside of it
- They both have a "local" scope, but the inner function has a somewhat "more local"
scope
- The scope of the outer function is **nonlocal** from the perspective of the inner function
- The `nonlocal` variable gets resolved recursively, so that Python looks for an
existing variable in the parent local scope and keeps looking up until it finds a
suiting variable otherwise it fails at runtime with a `SyntaxError`

## Scope resolution
- Python searches for declarations and definitions going from the innermost to
the outermost scope
- If it doesn't find said declaration/definition, it fails at runtime
- It searches
  - In the *local scope*
  - In the *module scope*
  - In the *built-in scope*

For example, running a script as simple as

```py
print(a)
```

raises an error like `NameError: name 'a' is not defined`, because the variable "a"
was not defined in any of the visited scopes