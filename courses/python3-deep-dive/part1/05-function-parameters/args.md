# `*args`

- Functions can use extended unpacking to achieve variadic functions in other
languages
- The extended unpacking works very similarly to the "spread operator" in JavaScript
- Conventionally, the unpacking variable is called `args`
- `*args` returns a _TUPLE_, while normal unpacking with assignments returns a _LIST_
- The `*args` exhausts all *positional* arguments, but does not interact with keyword arguments

```py
def sum(*args):
    result = 0
    for n in args:
        result += n
    return result
```

The JS equivalent is

```js
function sum(...args) {
    let result = 0;
    for (const n of args) {
        result += n;
    }
    return result;
}