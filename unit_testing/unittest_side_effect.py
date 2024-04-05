# The side_effect parameter in the unittest.mock.patch decorator allows you
# to define a function or callable object that will be called instead of
# the original method or attribute. This provides a powerful mechanism for
# controlling the behavior of mock objects and capturing information during
# testing. Here's more information about side_effect, along with examples
# and use cases:


from unittest.mock import patch


class MyClass:
    @staticmethod
    def function(a, b, keyword):
        return a + b, keyword

    @staticmethod
    def function_2():
        pass

    @staticmethod
    def function_3():
        pass


# 1. Return Different Values:
# Define a function to be used as a side effect
def side_effect_func(*args, **kwargs):
    return len(args) + len(kwargs)


with patch('__main__.MyClass.function', side_effect=side_effect_func):
    result = MyClass.function(1, 2, 'value')
print(result)


# result will be 3 (len(args) + len(kwargs))


# 2. Raise Exceptions:
# Define a function to be used as a side effect
def side_effect_func_2():
    raise ValueError("Error!")


with patch('__main__.MyClass.function_2', side_effect=side_effect_func_2):
    try:
        MyClass.function_2()
    except ValueError as e:
        print(e)

# Use cases:
# Capturing Arguments:
# Use side_effect to capture arguments passed to a method and perform custom
# logic based on those arguments.
#
# Dynamic Return Values:
# Return different values or raise exceptions based on certain conditions
# or inputs during testing.
#
# Simulating External Dependencies:
# Simulate the behavior of external dependencies by providing mock responses
# or raising errors as needed.
#
# Testing Error Handling:
# Test error handling logic by causing functions to raise exceptions
# using side_effect.
#
# Mocking I/O Operations:
# Mock I/O operations such as file reads or network requests and control
# their behavior using side_effect.
