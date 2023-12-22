movie = 'The Godfather'

# From index 0 up to but not including index 7
print(movie[0:7]) # 'The God'

# All but last character
print(movie[0:-1]) # 'The Godfathe'

# All but first charcater
print(movie[1:]) # 'he Godfather'

# The last char
print(movie[-1]) # 'r'
# Equivalent 1
print(movie[-1:len(movie)]) # 'r'
# Equivalent 2
print(movie[len(movie)-1]) # 'r'
# Equivalent 3
print(movie[len(movie)-1:len(movie)]) # 'r'

# Giving overflowing indices when slicing DOES NOT raise an IndexError!
print('100:', movie[100:]) # '100:'
print(':100', movie[:100]) # ':100 The Godfather'
print('100:0', movie[100:0]) # '100:0'
print('100:100', movie[100:100]) # '100:100'
print('0:-100', movie[0:-100]) # '0:-100'

# The third slicing value: the step
print(movie[0:10:1]) # 'The Godfat'

# Equivalent
print(movie[0:10]) # 'The Godfat'

# The Godfather
# 0123456789012
# x-x-x-x-x----
print(movie[0:10:2]) # 'TeGda'

print(movie[::]) # 'The Godfather'
print(movie[::-1]) # 'rehtafdoG ehT

print(movie[::-1][::-1] == movie) # True