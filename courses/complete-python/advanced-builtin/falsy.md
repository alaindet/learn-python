# Falsy values in Python

```python
''
0
0.0
None
[]
()
{}
False
```

Your classes in Python can implement a magic method, __bool__ , which will tell bool() , if statements, and the sort, whether your object should evaluate to True  or False .

If you don't implement __bool__ , then __len__  will be used—if it returns 0  it will evaluate to False ; otherwise it will evaluate to True .

Finally, if you don't implement either __bool__  or __len__ , your object will always evaluate to True.

# References
- https://docs.python.org/3/library/stdtypes.html#truth-value-testing
