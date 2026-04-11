import string

def check_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    upper_criteria = any(char.isupper() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    score = sum([length_criteria, digit_criteria, upper_criteria, special_criteria])

    print(f"\nPassword: {password}")
    if score == 4:
        print("Strength: 💪 Strong (Perfect for CyberSec!)")
    elif score == 3:
        print("Strength: 👍 Good (But can be better)")
    else:
        print("Strength: ⚠️ Weak (IIT level ki security chahiye bhai!)")

if _name_ == "_main_":
    p = input("Check karne ke liye password daalein: ")
    check_password_strength(p)
