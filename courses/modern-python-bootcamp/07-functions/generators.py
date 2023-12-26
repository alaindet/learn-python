from sys import getsizeof

list_comp_exp = [n*10 for n in range(1000)]
list_comp_mem = getsizeof(list_comp_exp)

# vvv This is a generator expression!
generator_exp = (n*10 for n in range(1000))
generator_mem = getsizeof(generator_exp)

max_memory = list_comp_mem
if generator_mem > list_comp_mem:
    max_memory = generator_mem

list_comp_perc = 100 * list_comp_mem / max_memory
generator_perc = 100 * generator_mem / max_memory

print(f'List Comprehension: {list_comp_mem} bytes ({list_comp_perc:.2f}%)')
# List Comprehension: 8856 bytes (100.00%)

print(f'Generator Expression: {generator_mem} bytes ({generator_perc:.2f}%)')
# Generator Expression: 208 bytes (2.35%)

# TL;DR
# - If storing, use list comprehension
# - Otherwise, use generators as much as possible
