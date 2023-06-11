# Type
- Python is dinamically typed, meaning type exists, but it's bound to runtime values
- Type is not enforced on variables, ex.: you can assign a string to a variable previously holding a number

## `type()`
- `type()` accepts a variable or a literal value and returns the data type associated to that value (not the variable)
- Custom types and classes have their own type
- Built-in types are
  - Text Type: `str`
  - Numeric Types: `int`, `float`, `complex`
  - Sequence Types:	`list`, `tuple`, `range`
  - Mapping Type:	`dict`
  - Set Types:`set`, `frozenset`
  - Boolean Type:	`bool` (`True` and `False`)
  - Binary Types:	`bytes`, `bytearray`, `memoryview`
  - None Type: `NoneType`

## `id()`
- `id()` accepts a variable or a literal value and returns its memory address as an integer
