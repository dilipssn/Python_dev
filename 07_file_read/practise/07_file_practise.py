"""
Excellent idea! Here are 10 practical exercises to help you practice file reading operations:

## Exercise 1: Read and Count Lines
Create a text file with some content. Write a program that reads the file and prints the total number of lines.

## Exercise 2: Find Longest Line
Read a text file and find the longest line. Print both the line and its length.

## Exercise 3: Word Counter
Read a text file and count how many times a specific word appears (case-insensitive).

## Exercise 4: JSON Student Records
Create a JSON file with student records (name, age, grade). Read it and print only students with grade above 80.

## Exercise 5: CSV Salary Analysis
Create a CSV file with employee names and salaries. Read it and calculate:
- Average salary
- Highest paid employee
- Lowest paid employee

## Exercise 6: File Content Reverser
Read a text file line by line and print all lines in reverse order (last line first).

## Exercise 7: JSON to CSV Converter
Read data from a JSON file and write it to a CSV file. For example, convert a list of products with name and price.

## Exercise 8: CSV Filter
Read a CSV file with product data (name, category, price). Create a new CSV file containing only products from a specific category.

## Exercise 9: Multiple File Reader
Create 3-4 small text files. Write a program that reads all of them and combines their content into a single output file.

## Exercise 10: Data Validator
Create a JSON file with user data (name, email, age). Read it and check:
- If email contains '@'
- If age is between 18 and 100
- Print validation results for each user

---

**Tips for Practice:**
- Start with exercises 1-3 (basic text files)
- Move to exercises 4, 7, 10 (JSON)
- Then try exercises 5, 6, 8 (CSV)
- Finish with exercise 9 (multiple files)

**Sample Files to Create:**

For text exercises, create `sample.txt`:
```
Hello World
Python is awesome
File reading is fun
Practice makes perfect
```

For JSON, create `students.json`:
```json
[
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 75},
    {"name": "Charlie", "age": 21, "grade": 90}
]
```

For CSV, create `employees.csv`:
```
Name,Salary
Alice,75000
Bob,60000
Charlie,80000
```

Would you like me to provide solution hints for any specific exercise, or would you prefer to try them on your own first?
"""

## Exercise 1: Read and Count Lines
# Create a text file with some content. 
# Write a program that reads the file and prints the total number of lines.


with open ('sample_text_file.txt', 'r') as file:
    counter = 0

    for employee in file:
        counter += 1
    print (f"The Total number of lines that are found at the given file are :{counter}\n")

# The number of lines that are found at the given file are :128

## Exercise 2: Find Longest Line
# Read a text file and find the longest line. Print both the line and its length.


with open ("sample_text_file.txt", 'r') as file:
    line_length_dict = {}

    for line in file:
        line_length = len(line)
        line_length_dict[line_length] = line

    max_line_length = max(line_length_dict.keys())
    print (f'The logest line number is "{max_line_length}" and the line displayed as below \n{line_length_dict[max_line_length]}\n')

# The logest line number is "51" and the line displayed as below
# --------------------------------------------------

## Exercise 3: Word Counter
# Read a text file and count how many times a specific word appears (case-insensitive).

with open("sample_text_file.txt", 'r') as file:
    counter = 0

    for lines in file:
        for word in lines.split(" "):
            if "employee" == word.lower():
                counter += 1
    print (f"I found the word 'employee', {counter} many times in the given file\n")

# I found the word 'employee', 13 many times in the given file

## Exercise 4: JSON Student Records
# Create a JSON file with student records (name, age, grade). Read it and print only students with grade above 80.
import json

with open ('student_records.json', 'r') as file:
    student_details = json.load(file)
    for student in student_details:
#        print (type(student_details[student]["grade"]))
        if int(student_details[student]["grade"]) > 80:
            print (json.dumps(student_details[student], indent=4))

            
## Exercise 5: CSV Salary Analysis
# Create a CSV file with employee names and salaries. Read it and calculate:
# - Average salary
# - Highest paid employee
# - Lowest paid employee
import csv

with open('employee_details.csv', 'r') as file:
    employee_csv_reader = csv.DictReader(file, delimiter=",")
    
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')
    print(highest, lowest)
    
    for line in employee_csv_reader:
        salary = int(line['Salary'])
        total += salary
        count += 1
        highest = max(highest, salary)
        lowest = min(lowest, salary)
    
    if count > 0:
        avg_emp_salary = total / count
        print(f"\nAverage salary of employee is : {avg_emp_salary}")
        print(f"Highly paid employee's salary is : {highest}")    
        print(f"Least paid employee's salary is : {lowest}\n")


## Exercise 6: File Content Reverser
# Read a text file line by line and print all lines in reverse order (last line first).

with open('sample_text_file.txt', 'r') as file:
    for line in file:
        print(f'{line[::-1]}')

## Exercise 7: JSON to CSV Converter
# Read data from a JSON file and write it to a CSV file. For example, convert a list of products with name and price.


