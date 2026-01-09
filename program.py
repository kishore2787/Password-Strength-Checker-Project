def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*" for c in password):
        strength += 1

    if strength <= 2:
        print("Weak Password")
    elif strength == 3 or strength == 4:
        print("Medium Password")
    else:
        print("Strong Password")

pwd = input("Enter your password: ")
check_password_strength(pwd)