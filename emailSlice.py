email = input("Enter Your Email: ").strip()

while '@' not in email:
    email = input("Invalid email. Please include '@' in your email: ").strip()

print(f"Your username is {email.split('@')[0]} & domain is {email.split('@')[1]}")
print("Thank you for using our service")