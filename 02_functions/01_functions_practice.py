"""
Challenge 1: Temperature Converter
Create a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.

Formula: F = (C × 9/5) + 32
Example: celsius_to_fahrenheit(0) should return 32

Challenge 2: Odd or Even Checker
Create a function check_odd_even(number) that returns "Even" if the number is even and "Odd" if it's odd.

Example: check_odd_even(7) should return "Odd"

Challenge 3: Age Category
Create a function age_category(age) that returns:

"Child" if age is less than 13
"Teenager" if age is 13-19
"Adult" if age is 20 or above
Example: age_category(15) should return "Teenager"

Challenge 4: String Reverser
Create a function reverse_string(text) that returns the text reversed.

Hint: You can use slicing [::-1]
Example: reverse_string("hello") should return "olleh"

Challenge 5: Count Vowels
Create a function count_vowels(text) that counts how many vowels (a, e, i, o, u) are in a string.

Example: count_vowels("hello") should return 2

Challenge 6: Simple Password Validator
Create a function is_valid_password(password) that returns True if the password is at least 8 characters long, and False otherwise.

Example: is_valid_password("abc123") should return False
Example: is_valid_password("mypassword123") should return True

Challenge 7: List Average
Create a function calculate_average(numbers) that takes a list of numbers and returns their average.

Example: calculate_average([10, 20, 30]) should return 20

Challenge 8: Find Maximum
Create a function find_largest(numbers) that takes a list of numbers and returns the largest number.

Try to solve it WITHOUT using the built-in max() function
Example: find_largest([3, 7, 2, 9, 1]) should return 9

Challenge 9: Discount Calculator
Create a function apply_discount(price, discount_percent) that:

Takes an original price and a discount percentage
Returns the final price after discount
Example: apply_discount(100, 20) should return 80 (20% off 100)

Challenge 10: Factorial Calculator
Create a function factorial(n) that calculates the factorial of a number.

Factorial means: 5! = 5 × 4 × 3 × 2 × 1 = 120
Example: factorial(5) should return 120
Example: factorial(3) should return 6

"""

input_str = """
    Factorial means: 5! = 5 × 4 × 3 × 2 × 1 = 120
    Example: factorial(5) should return 120
    Example: factorial(3) should return 6
"""


# use regex to find all digtis -> re.findall() - \d (pattern matching) - return/print
# remove all the digits -> re.sub() - \d (pattern matching) - return / print
# find the no. of "factorial" in this str -> len(re.findall())

def count_occurrences():
    # find the re function to use
    ...

    # apply regular expression
    ...

    # return
    ...


def calc_factorial(n):
    return n * n
