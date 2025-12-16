from fastapi import FastAPI
import dictionaries
import myfile


# Create your app
app = FastAPI()

# Your first "endpoint" (like a menu item)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/student")
def get_student():
    return dictionaries.get_student_info()  

