
# open(file, 'r') as file:
#    file.read()
#    file.readlines() -> list of lines
# for line in lines # common usage

# open(file, 'w')
#    file.write(str)   <- accepts string only   # common usage  example: file.write("Hello World\n")
#    file.writelines(list_of_strings)  <- accepts list of strings only ["line1", "line2"]

# Generic usage
# with open('sample_write.txt', 'w') as file:
#     file.write("Hello World\n")
#     file.write("Second line\n")


import csv


lines_to_write = [
    "Python is awesome!",
    "File writing is fun.",
    "Practice makes perfect.",
    "Keep coding every day.",
    "Good luck with your coding!"
]

# usual approach
with open('sample_write.txt', 'w') as file:
    for line in lines_to_write:
        file.write(f"{line}\n")

# writelines approach - less common
# with open('sample_write.txt', 'w') as file:
#     file.writelines(f"{line}\n" for line in lines_to_write)

new_list = [f"{line}\n" for line in lines_to_write]  #1

#normal list create
new_list = []
for line in lines_to_write:
    new_list.append(f"{line}\n")
        
"""    
## Exercise 7: JSON to CSV Converter
Read data from a JSON file and write it to a CSV file. For example, 
convert a list of products with name and price.
"""
# read data - json.load()   -> dict
# write data - csv.writer() or csv.DictWriter(dict)

# write csv file
person = {
    "name": "Alice",
    "age": 30,
    "active": False,
    "city": "New York"
}

csv_file = 'person.csv'

# open json file and read data as dictionary -> list
with open(csv_file, 'w', newline='') as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=["name", "age", "active", "city"])
    
    # write header
    csv_dict_writer.writeheader()
    
    # for 
    # data
    csv_dict_writer.writerow(person)  # write header and row
    
    print(f"Data written to {csv_file} successfully.")


"""
## Exercise 8: CSV Filter
Read a CSV file with product data (name, category, price). 
Create a new CSV file containing only products from a specific category.

electronics.csv for electronic products
furniture.csv for furniture products

def create_category_file(category, input_csv, output_csv):
    ...
"""


"""
## Exercise 9: Multiple File Reader
Create 3-4 small text files.                           
Write a program that reads all of them and combines     
their content into a single output file.               
"""
# store in list
files = ["files.txt", "files1.txt", "files2.txt"]

# for file in file: 
# read file
# write to output file




















"""
## Exercise 10: Data Validator
Create a JSON file with user data (name, email, age). Read it and check:
- If email contains '@'
- If age is between 18 and 100
- Print validation results for each user

"""