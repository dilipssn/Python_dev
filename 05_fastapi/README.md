# FastAPI String Operations API 🚀

A comprehensive FastAPI application demonstrating string manipulation operations through RESTful endpoints. Perfect for learning FastAPI basics and Python string operations!

## Quick Reference Card

```bash
# Installation
pip install fastapi "uvicorn[standard]"

# Run Server
python -m uvicorn main:app --reload

# Access Documentation
http://127.0.0.1:8000/docs

# Stop Server
Press CTRL+C

# Test Endpoint
http://127.0.0.1:8000/email/validate?email=test@example.com

## ✨ Features

This API provides **50+ endpoints** across 5 major categories:

1. **📧 Email Tools** - Validate, extract, and mask email addresses

---

## 📁 Project Structure

```
05_fastapi/
│
├── main.py              # FastAPI application with all endpoints
├── helpers.py           # Python functions for string operations
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Method 1: Direct Installation

```bash
# Install FastAPI
pip install fastapi

# Install Uvicorn (ASGI server)
pip install "uvicorn[standard]"
```

### Method 2: Install from requirements.txt (Recommended)

```bash
# Navigate to project directory
cd 05_fastapi/

# Install all dependencies
python -m pip install -r requirements.txt
```

### requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
```

---

## 🚀 Running the Application

### Start the Development Server

```bash
# Navigate to project directory
cd 05_fastapi/

# Start the server with auto-reload
python -m uvicorn main:app --reload
```

**What does this mean?**
- `main` = the filename (main.py)
- `app` = the FastAPI instance in your file
- `--reload` = automatically restart server when code changes

### Server Output
You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## 📚 API Documentation

Once the server is running, you can access:

### Interactive API Documentation (Swagger UI)
```
http://127.0.0.1:8000/docs
```
- **Try out endpoints** directly in your browser
- **See request/response examples**
- **Test without writing any code**

### Alternative Documentation (ReDoc)
```
http://127.0.0.1:8000/redoc
```
- Clean, organized documentation
- Great for reading and understanding the API

### Home Page
```
http://127.0.0.1:8000/
```
- Overview of all available categories

---

## 🎯 Available Endpoints

### 📧 Email Tools (`/email/*`)

| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /email/validate` | Check if email is valid | `?email=test@example.com` |
| `GET /email/username` | Extract username from email | `?email=john@gmail.com` |
| `GET /email/domain` | Extract domain from email | `?email=john@gmail.com` |
| `GET /email/mask` | Mask email for privacy | `?email=secret@company.com` |
| `GET /email/analyze` | Complete email analysis | `?email=test@example.com` |


## 💡 Usage Examples

### Using Browser

Simply paste URLs in your browser:

```
http://127.0.0.1:8000/email/validate?email=test@example.com
```

### Using curl (Command Line)

```bash
# Validate an email
curl "http://127.0.0.1:8000/email/validate?email=test@example.com"
```

### Using Python requests

```python
import requests

# Validate email
response = requests.get(
    "http://127.0.0.1:8000/email/validate",
    params={"email": "test@example.com"}
)
print(response.json())

# Check password strength
response = requests.get(
    "http://127.0.0.1:8000/password/strength",
    params={"password": "Pass123!"}
)
print(response.json())
```

### Using JavaScript (fetch)

```javascript
// Validate email
fetch('http://127.0.0.1:8000/email/validate?email=test@example.com')
    .then(response => response.json())
    .then(data => console.log(data));
```

---

## 📖 Learning Path

### For Beginners

1. **Start with the documentation**
   - Visit `http://127.0.0.1:8000/docs`
   - Try the email validation endpoint first

2. **Understand the code structure**
   - Look at `helpers.py` - pure Python functions
   - Look at `main.py` - FastAPI endpoints that call helper functions

3. **Experiment**
   - Modify existing endpoints
   - Add your own string operation functions
   - Create new endpoints

### Key Concepts Covered

- ✅ **FastAPI Basics** - Creating endpoints with `@app.get()`
- ✅ **Query Parameters** - Accepting input via URL parameters
- ✅ **Path Operations** - Different HTTP methods (GET, POST, etc.)
- ✅ **Error Handling** - Using `HTTPException`
- ✅ **Response Models** - Returning JSON data
- ✅ **Code Organization** - Separating logic from API layer

---

## 🔧 Troubleshooting

### Port Already in Use

**Error:** `[Errno 48] Address already in use`

**Solution:** Use a different port
```bash
python -m uvicorn main:app --reload --port 8001
```

### Module Not Found Error

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Import Error from helpers.py

**Error:** `ImportError: cannot import name 'is_valid_email' from 'helpers'`

**Solution:** Make sure all functions in `helpers.py` are implemented (not just `pass`)

### Auto-reload Not Working

**Solution:** Make sure you're using the `--reload` flag
```bash
python -m uvicorn main:app --reload
```

### Can't Access from Another Computer

**Solution:** Bind to all interfaces
```bash
python -m uvicorn main:app --reload --host 0.0.0.0
```
Then access via `http://YOUR_IP:8000`

---

## 🎓 Next Steps

After mastering this API, try:

1. **Add POST endpoints** - Accept JSON data in request body
2. **Add a database** - Store emails, passwords, or user data
3. **Add authentication** - Require API keys for certain endpoints
4. **Add rate limiting** - Prevent API abuse
5. **Deploy to cloud** - Host on Heroku, Railway, or AWS
6. **Add testing** - Write unit tests with pytest

---

## 📝 Notes

- **Development Server**: The `--reload` flag is for development only
- **Production**: Use proper ASGI servers like Gunicorn with Uvicorn workers
- **Security**: Never store passwords in plain text (use hashing)
- **CORS**: If accessing from frontend, you may need to enable CORS

---

## 🤝 Contributing

Feel free to:
- Add more string operation functions
- Improve existing functions
- Add new endpoint categories
- Write tests
- Improve documentation

---

## 📄 License

This project is for educational purposes. Feel free to use and modify!

---

## 🎉 Happy Coding!

Questions? Issues? Check the `/docs` endpoint or review the code comments!

**Author:** Your FastAPI Learning Journey  
**Version:** 1.0.0  
**Last Updated:** December 2024

---

