from fastapi import FastAPI
from helpers import (
    # Exercise 1: Email Tools
    is_valid_email,
    extract_username,
    extract_domain,
    mask_email
)

app = FastAPI(title="String Operations API", version="1.0.0")

# ==================== HOME ====================
@app.get("/")
def home():
    return {
        "message": "String Operations API",
        "exercises": {
            "1": "Email Tools - /email/*",
            "2": "Password Checker - /password/*",
            "3": "Text Formatter - /format/*",
            "4": "URL & Slug - /url/*",
            "5": "Name Formatter - /name/*"
        }
    }

# ==================== EXERCISE 1: EMAIL TOOLS ====================

@app.get("/email/validate")
def validate_email():
    """Validate if email is properly formatted"""
    ...

@app.get("/email/username")
def get_username():
    """Extract username from email (part before @)"""
    ...

@app.get("/email/domain")
def get_domain():
    """Extract domain from email (part after @)"""
    ...