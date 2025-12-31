"""
## Exercise 1: Read and Count Lines
Create a text file with some content. 
Write a program that reads the file and prints the total number of lines.
"""
import os
import json


def read_and_count_lines(text_file = "./exercise1.txt"):
    if not os.path.exists(text_file):
        print(f"File {text_file} does not exist. Please create it with some content.")
        return

    line_count = 0

    with open(text_file, 'r') as file:
        for _ in file:
            line_count += 1
        print(f"Total number of lines: {line_count}")


read_and_count_lines()  # Total number of lines: 5
# File ./exercise2.txt does not exist. Please create it with some content.

"""
    ## Exercise 2: Find Longest Line
    Read a text file and find the longest line. Print both the line and its length.
"""
def read_and_find_longest_line(text_file = "./exercise1.txt"):
    if not os.path.exists(text_file):
        print(f"File {text_file} does not exist. Please create it with some content.")
        return

    longest_size = 0
    longest_line = None

    with open(text_file) as file:
        for line in file:
            # longest_size = max(len(line), longest_size)
            if len(line) > longest_size:
                longest_size = len(line)
                longest_line = line

    print(f"Longest line: {longest_line}")
    print(f"Longest line length: {longest_size}")

read_and_find_longest_line()

# Output:
# Longest line: Line 5: Good luck with your coding! This line is the new longest.
# Longest line length: 65

"""
## Exercise 3: Word Counter
Read a text file and count how many times a specific word appears (case-insensitive).
"""
def word_counter(word, text_file = "./exercise1.txt", ignore_case=False):
    if not os.path.exists(text_file):
        print(f"File {text_file} does not exist. Please create it with some content.")
        return

    occurrences = 0
    with open(text_file) as file:
        for line in file:
            line = line.lower() if ignore_case else line
            occurrences += line.count(word)

    print(f"The word: {word} appears {occurrences} times with ignorecase = {ignore_case}")


word_counter("line")    # The word: line appears 2 times with ignorecase = False
word_counter("line", ignore_case=True)    # The word: line appears 7 times with ignorecase = True
word_counter("to")    # The word: to appears 2 times with ignorecase = False

"""
## Exercise 4: 
    JSON Student Records
    Create a JSON file with student records (name, age, grade). 
    Read it and print only students with grade above 80.
"""
def find_students_by_grade(grade, json_file = "./students.json"):
    if not os.path.exists(json_file):
        print(f"File {json_file} does not exist. Please create it with some content.")
        return

    with open(json_file) as file:
        json_obj = json.load(file)
        for student in json_obj["students"]:
            if int(student["grade"]) >= grade:
                print(student)


find_students_by_grade(80)
# {'name': 'Diya Nair', 'age': 17, 'grade': 92}
# {'name': 'Rahul Menon', 'age': 15, 'grade': 84}
# {'name': 'Vikram Rao', 'age': 18, 'grade': 95}
# {'name': 'Ananya Gupta', 'age': 17, 'grade': 80}

find_students_by_grade(90)
# {'name': 'Diya Nair', 'age': 17, 'grade': 92}
# {'name': 'Vikram Rao', 'age': 18, 'grade': 95}


"""
## Exercise 5: CSV Salary Analysis
Create a CSV file with employee names and salaries. Read it and calculate:
- Average salary
- Highest paid employee
- Lowest paid employee
"""
import csv

def read_csv(csv_file):
    if not os.path.exists(csv_file):
        print(f"File {csv_file} does not exist. Please create it with some content.")
        return

    with open(csv_file) as file:
        # Iterate once and gather all data
        total_salary = highest_pay = lowest_pay = emp_count = 0

        for employee in csv.DictReader(file):
            emp_count += 1
            current_salary = int(employee["salary"])
            total_salary += current_salary
            highest_pay = max(current_salary, highest_pay)
            lowest_pay = min(current_salary, highest_pay)

        average_salary = float(total_salary / emp_count)
        print(f"""
Salary problem:
Total employee salary: {total_salary}
No. of employees: {emp_count}
Average salary: {average_salary:.2f}
Highest pay: {highest_pay}
Lowest pay: {lowest_pay}
""")

read_csv(csv_file = "./employees.csv")

# Salary problem:
# Total employee salary: 508000
# No. of employees: 6
# Average salary: 84666.67
# Highest pay: 120000
# Lowest pay: 70000