import os
import sys

def add_numbers(a, b):
    result = a + b
    print("Result is: " + result)  # Type error: concatenating int with str
    return result


def unused_function():  # This function is never used
    return "I am not used"


def security_issue():
    user_input = input("Enter a command: ")
    os.system(user_input)  # Command injection vulnerability


class SampleClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __del__(self):
        print("Destructor called")  # Risky: relying on destructors for cleanup


if __name__ == "__main__":
    num1 = sys.argv[1]  # Potential IndexError if no args provided
    num2 = sys.argv[2]
    add_numbers(num1, num2)
