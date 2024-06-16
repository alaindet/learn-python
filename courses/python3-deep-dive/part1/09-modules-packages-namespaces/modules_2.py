"""
Let's hack the modules cache by loading a fake module1 into the cache, thus
preventing Python's runtime to correctly import the real module1 from module1.py

Without the modules cache hack, a regular ModuleNotFoundError: No module named 'foo'
would be raised
"""

import sys
sys.modules['foo'] = lambda: 'Testing module caching'
import foo # <-- Python finds it in the cache and never attempts to load from a file!
print(foo) # <function <lambda> at 0x00000217A92C9B20>