from validator_collection import validators
user_input = input("What's your email address? ")
try:
    email_address = validators.email(user_input)
    print("Valid")
except ValueError:
    print("Invalid")