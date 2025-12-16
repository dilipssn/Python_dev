email = '...'   # define your email here

def is_valid_email():
    """
    Check if email is valid
    Rules: Must have exactly one @, must have a dot after @, no spaces
    
    Example: "test@example.com" -> True
             "invalid.email" -> False
    """
    # TODO:
    # 1. Check if '@' is in email (use 'in' operator)
    # 2. Check if email.count('@') == 1
    # 3. Split by '@' and check if second part has a '.'
    # 4. Check if no spaces (use ' ' in email)
    pass

def extract_username(email):
    """
    Extract username from email (part before @)
    
    Example: "john.doe@gmail.com" -> "john.doe"
    """
    # TODO: Use .split('@') and get first element
    pass

def extract_domain(email):
    """
    Extract domain from email (part after @)
    
    Example: "john.doe@gmail.com" -> "gmail.com"
    """
    # TODO: Use .split('@') and get second element
    pass

def mask_email(email):
    """
    Mask email for privacy: show first 2 chars of username, rest as ***
    
    Example: "john.doe@gmail.com" -> "jo*****@gmail.com"
    """
    # TODO:
    # 1. Split by '@'
    # 2. Take first 2 chars of username: username[:2]
    # 3. Add asterisks: username[:2] + '*****'
    # 4. Join back with @ and domain
    pass