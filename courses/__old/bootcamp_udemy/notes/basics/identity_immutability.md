# Identity and Immutability
- The `is` and `is not` operators compare the memory addresses, not values
- Types can be mutable (re-assignable) and immutable (cannot be re-assigned)
- Python has a number of immutable built-in types, so that if you try to change those you get a re-assignment instead (see example)
  ```py
  # Changing immutable values re-assigns them
  a = 1
  print(id(a)) # 140730738533160
  a += 1
  print(id(a)) # 140730738533192 (It's different!)
  ```

- Immutable built-in types are
  - `int`, `float`, `str`, `tuple` and `frozenset`
- Mutable built-in types are
  - `list`, `set`, `dict`
