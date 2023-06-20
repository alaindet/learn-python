# Strings

- Python allows both single quotes and double quotes to encase string literals
- However, most standards favor single quotes
  - PEP8 (https://peps.python.org/pep-0008/)
  - Google Python Style Guide (https://google.github.io/styleguide/pyguide.html)
- Triple quotes can be used for multi-line strings if you assign them to a variable
- However, unassigned triple quotes are conventionally defined **DOCSTRINGS** and it's picked up by IDEs and documentaion tools
- The docstring is attached to its scope (a module, a function etc.) and can be accessed via the dunder variable `__doc__`

## Indexing

- Strings are just lists of characters
- A single character is STILL a string in Python, there's no concept of character types
