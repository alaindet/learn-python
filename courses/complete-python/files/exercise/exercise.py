from addition import Addition
# You don't need to change the import statement
# now you can use Addition.add() function from the addition module like this:
# res = Addition.add(100, 150)
# the Addition.add() function takes in two parameters `num1` and `num2` and return the sum of `num1` and `num2`


# Please create and implement a Calculator class, which makes use of the `addition` module.
# Your Calculator should achieve these goals:
# - It should implement `Addition.add()`, `subtract()`, `multiply()` and `divide()` methods.
# - It cannot use addition, subtraction, multiplication and division operators (`+`, `-`, `*` and `/`) directly.
#   Instead, it should be only based on the `Addition.add()` function from the `addition` module.
# - To simplify the problem, you may expect input for the multiply() and divide() methods are all non-integers,
#   and will always be valid, i.e. all non-negative integers and no 0 as divisor.

# the class definition and a sample class method `Addition.add()` is provided below
class Calculator:

    # a sample add() method in our calculator is shown below
    # you may learn from it and implement the other methods
    @classmethod
    def add(cls, num1, num2):
        # make use of add() from addition module
        return Addition.add(num1, num2)

    # implement a class method `subtract()` that takes in num1 and num2 and return num1 - num2
    # your `subtract()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)

    # implement a class method `multiply()` that takes in num1 and num2 and return num1 * num2
    # your `multiply()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 and num2 are always non-negative integers
    @classmethod
    def multiply(cls, num1, num2):
        result = 0
        counter = num2
        while (counter > 0):
            result = cls.add(result, num1)
            counter = cls.subtract(counter, 1)
        return result


    # implement a class method `divide()` that takes in num1 and num2 and return num1 // num2
    # your `divide()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 is always a non-negative integer, and num2 is always a positive integer
    @classmethod
    def divide(cls, num1, num2):
        result = 0
        rest = num1
        while (rest >= num2):
            result = cls.add(result, 1)
            rest = cls.subtract(rest, num2)
        return f'Result = {result}, rest = {rest}'


print(Calculator.add(1, 3))
print(Calculator.subtract(10, 3))
print(Calculator.multiply(6, 7))
print(Calculator.divide(64, 3))
