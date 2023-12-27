import pdb

foo = 'foo'
bar = 'bar'
baz = foo + bar

pdb.set_trace() # <-- This line starts the debugger

"""\
PDB common commands
l   list
n   next line
p   print
c   continue/exit
"""

print(baz)