email = "student@example.com"
password = "python123"

# Simple checks using assert
assert "@" in email, "Email must contain @"
assert len(password) >= 8, "Password must be at least 8 characters"

print("Email and password are valid")
