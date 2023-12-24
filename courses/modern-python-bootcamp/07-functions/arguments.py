def exponentiate(n: int, power=2) -> int:
    return n ** power


# With positional-only arguments
print(exponentiate(2, 3))  # 8

# With positional and keyword arguments mixed
print(exponentiate(2, power=3))  # 8

# With keyword-only arguments
print(exponentiate(n=2, power=3))  # 8

# With keyword-only arguments (no positional arguments) no order is needed
print(exponentiate(power=3, n=2))  # 8
