"""
Here are **10 basic, beginner-friendly practice questions** focused *only* on **CSV read/write** and **JSON read/write** in Python. These are simple and perfect for hands-on practice.

---

## 1. Read a CSV File

Read a CSV file named `students.csv` containing:

```
id,name,marks
1,Alice,85
2,Bob,78
```

Print each row.

---

## 2. Write to a CSV File

Create a CSV file named `employees.csv` with the columns:

```
id,name,department
```

Add at least 3 employee records.

---

## 3. Copy CSV File

Read data from `input.csv` and write the same data to `output.csv`.

---

## 4. Filter CSV Data

Read a CSV file with `name,age`.
Write a new CSV file containing only people whose age is **greater than 18**.

---

## 5. Read JSON File

Read a JSON file `users.json` containing a list of users and print each user's name.

---

## 6. Write JSON File

Create a dictionary with student details and write it to a JSON file called `student.json`.

---

## 7. Update JSON Data

Read `products.json`, increase the price of all products by **10%**, and save the updated data back to the file.

---

## 8. Convert CSV to JSON

Read a CSV file with columns `id,name,email` and convert it into a JSON file.

---

## 9. Convert JSON to CSV

Read a JSON file containing employee data and write it to a CSV file with headers.

---

## 10. Count Records

Read a CSV or JSON file and print the **total number of records** in the file.

---

### Tips While Practicing

* Use `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`
* Use `json.load()` and `json.dump()`
* Always open files using `with open(...)`

---

If you want:

* **Sample files**
* **Answers/solutions**
* **Slightly harder versions**
* **Interview-style variations**

Just tell me 🙂

"""


"""
Perfect 👍
Below are **sample CSV and JSON files in plain text format** that you can copy-paste into files and practice with.

---

## 📄 CSV SAMPLE FILES

### 1️⃣ `students.csv`

```
id,name,marks
1,Alice,85
2,Bob,78
3,Charlie,92
4,David,66
```

---

### 2️⃣ `employees.csv`

```
id,name,department
101,John,HR
102,Sarah,Engineering
103,Michael,Finance
104,Emma,Engineering
```

---

### 3️⃣ `people.csv`

```
name,age
Ravi,17
Anita,22
Kiran,18
Neha,25
```

---

### 4️⃣ `products.csv`

```
id,name,price
1,Laptop,75000
2,Phone,30000
3,Tablet,20000
```

---

## 📄 JSON SAMPLE FILES

### 5️⃣ `users.json`

```
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com"
  },
  {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com"
  }
]
```

---

### 6️⃣ `student.json`

```
{
  "id": 1,
  "name": "Rahul",
  "age": 20,
  "course": "Computer Science"
}
```

---

### 7️⃣ `products.json`

```
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 75000
  },
  {
    "id": 2,
    "name": "Phone",
    "price": 30000
  },
  {
    "id": 3,
    "name": "Tablet",
    "price": 20000
  }
]
```

---

### 8️⃣ `employees.json`

```
[
  {
    "id": 101,
    "name": "John",
    "department": "HR"
  },
  {
    "id": 102,
    "name": "Sarah",
    "department": "Engineering"
  },
  {
    "id": 103,
    "name": "Michael",
    "department": "Finance"
  }
]
```

---

## ✅ How to Use These

1. Create files with the exact names (e.g., `students.csv`)
2. Paste the corresponding text
3. Practice:

   * `csv.reader` / `DictReader`
   * `csv.writer` / `DictWriter`
   * `json.load()` / `json.dump()`

---

If you want next:

* ✔️ **Solutions for all 10 questions**
* ✔️ **One-file practice script**
* ✔️ **Interview-style questions**
* ✔️ **Step-by-step walkthroughs**

Just tell me what you want to do next 🚀

"""