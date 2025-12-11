"""
Part 1: Basic String Operations (No conditions needed)
Exercise 1: String Reversal
Write a function that takes a string and returns it reversed.
Input: "hello"
Output: "olleh"
Exercise 2: Count Vowels
Write a function that counts the number of vowels (a, e, i, o, u) in a string.
Input: "beautiful"
Output: 5
Exercise 3: Word Counter
Write a function that counts how many words are in a sentence.
Input: "Python is amazing"
Output: 3
Exercise 4: Remove Spaces
Write a function that removes all spaces from a string.
Input: "Hello World Python"
Output: "HelloWorldPython"
Exercise 5: First and Last
Write a function that returns the first and last character of a string concatenated.
Input: "Python"
Output: "Pn"
Exercise 6: Capitalize Every Word
Write a function that capitalizes the first letter of each word.
Input: "hello world python"
Output: "Hello World Python"
Exercise 7: Repeat Characters
Write a function that takes a string and a number, and repeats each character that many times.
Input: "abc", 3
Output: "aaabbbccc"
Exercise 8: Extract Digits
Write a function that extracts all digits from a string.
Input: "abc123def456"
Output: "123456"
Exercise 9: Middle Character
Write a function that returns the middle character(s) of a string.
Input: "hello" (odd length)
Output: "l"
Input: "test" (even length)
Output: "es"
Exercise 10: Swap Case
Write a function that swaps the case of all letters (upper to lower, lower to upper).
Input: "Hello World"
Output: "hELLO wORLD"

Part 2: String Operations with Conditionals (if/elif/else)
Exercise 11: Password Validator
Write a function that checks if a password is valid. A valid password must:

Be at least 8 characters long
Contain at least one digit
Contain at least one uppercase letter

Return "Valid" or a specific error message.
Input: "Pass123"
Output: "Password too short"
Input: "Password123"
Output: "Valid"
Exercise 12: Palindrome Checker
Write a function that checks if a string is a palindrome (reads same forwards and backwards). Ignore spaces and case.
Input: "racecar"
Output: "Palindrome"
Input: "A man a plan a canal Panama"
Output: "Palindrome"
Input: "hello"
Output: "Not a palindrome"

Exercise 13: Grade Calculator
Write a function that takes a student's name and score, and returns a formatted string with their grade:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

Input: "Alice", 85
Output: "Alice scored 85 and got grade B"

Exercise 14: Email Validator
Write a function that checks if an email is valid. It should:

Contain exactly one @ symbol
Have characters before and after @
Have a dot (.) after @
Return "Valid email" or "Invalid email"

Input: "test@example.com"
Output: "Valid email"
Input: "testexample.com"
Output: "Invalid email"


Exercise 15: String Comparator
Write a function that compares two strings and returns:

"Equal" if they're identical
"Equal (case insensitive)" if they're same ignoring case -- convert everthing to common format -- lowercase() .. uppercase()
"Different lengths" if lengths differ   len(str)
"Completely different" otherwise .. a != b

Input: "Hello", "hello"
Output: "Equal (case insensitive)"

Exercise 16: Vowel or Consonant Counter
Write a function that takes a character and tells if it's:

A vowel (uppercase or lowercase)
A consonant (uppercase or lowercase)
A digit
A special character

Input: "a"
Output: "Vowel"
Input: "B"
Output: "Consonant"
Input: "5"
Output: "Digit"


Exercise 17: String Strength Analyzer
Write a function that analyzes a string and categorizes it as:

"Weak" if length < 5
"Medium" if length 5-10 and contains only letters
"Strong" if length > 10 and contains letters and numbers
"Very Strong" if it has letters, numbers, and special characters


Input: "hi"
Output: "Weak"

Input: "Hello123!"
Output: "Very Strong"
Exercise 18: Sentence Type Detector
Write a function that determines the type of sentence:

"Question" if it ends with ?
"Exclamation" if it ends with !
"Statement" if it ends with .
"Invalid" if it doesn't end with punctuation

Input: "How are you?"
Output: "Question"

Exercise 19: Username Validator
Write a function that validates a username based on these rules:

Must be 5-15 characters long
Can only contain letters, numbers, and underscores
Must start with a letter
Return "Valid username" or specific error messages.

Input: "user_123"
Output: "Valid username"
Input: "123user"
Output: "Must start with a letter"

Exercise 20: Text Formatter

Write a function that takes a string and a format type ("upper", "lower", "title", "capitalize") and returns the formatted string. If the format type is invalid, return "Invalid format type".
Input: "hello world", "title"
Output: "Hello World"
Input: "hello world", "reverse"
Output: "Invalid format type"

Bonus Tips for Solving These:

Start by defining the function with a clear name
Think about what conditions you need to check
Use string methods like .isdigit(), .isalpha(), .upper(), .lower()
Test with multiple examples
Handle edge cases (empty strings, single characters, etc.)
"""

# Exercise 14: Email Validator
# Write a function that checks if an email is valid. It should:
def validate_email(mail_id: str):
    # Contain exactly one @ symbol
    if mail_id.count("@") != 1:
        print(f"mail should contain exactly 1 '@' symbol")
        return "invalid email"

    # Have characters before and after @
    before, after = mail_id.split('@')
    if not before or not after:
        print(f"mail must have characters before and after @")
        return "invalid email"

    # Have a dot (.) after @
    if "." not in after:
        print(f"mail must have dot (.) after @")
        return "invalid email"

    if  after[-1] == '.':
        print(f"mail must not end with dot (.) ")
        return "invalid email"

    return "valid email"



# Exercise 14: Email Validator

# Write a function that checks if an email is valid. It should:
def email_validator(email: str):
    valid = True # "Valid email"
    errors = []

    # Contain exactly one @ symbol
    if email.count("@") != 1:
        print(f"email id does not contain exactly 1 '@' symbol: {email}")
        errors.append("email id does not contain exactly 1 '@' symbol")
        # valid = "Invalid email"
        valid = False

        # Have characters before and after @
    before, after = email.split("@")
    if not before or not after:
        print(f"email id does not contain characters before and after '@' symbol: {email}")
        errors.append("email id does not contain characters before and after '@' symbol")
        # valid = "Invalid email"
        valid = False

    # Have a dot (.) after @
    if "." not in after:
        print(f"email id does not contain dot (.) after '@' symbol: {email}")
        errors.append("email id does not contain dot (.) after '@' symbol")
        # valid = "Invalid email"
        valid = False

    # should have word after .
    left, domain = after.split(".")
    if not domain or not left:
        print(f"email id does not contain character before and domain name after '.' symbol: {email}")
        errors.append("email id does not contain domain name after '.' symbol")
        # valid = "Invalid email"
        valid = False

    print(f"Errors found:\n{errors}")

    return valid

# print(email_validator("test@example.com"))
my_email = "test@.net"
print(my_email)
if not email_validator(my_email):
    print(f"Errors in mail. Please fix it.")
else:
    print("Email is valid. User registered!")

# Input: "test@example.com"
# Output: "Valid email"
# Input: "testexample.com"
# Output: "Invalid email"