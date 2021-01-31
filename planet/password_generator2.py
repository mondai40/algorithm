import string
import copy
import random

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation
password_chars_list = [lower_letters, upper_letters, numbers, special_chars]


def create_password(num):
    password = ""
    password_length = num
    password_required_chars_list = copy.copy(password_chars_list)
    
    while password_length > 0:
        if (len(password_required_chars_list) == 0):
            password_chars = random.choice(password_chars_list)
            password += random.choice(password_chars)
        else:
            password_chars = random.choice(password_required_chars_list)
            password += random.choice(password_chars)
            password_required_chars_list.remove(password_chars)
        password_length -= 1
        
    return password
    
    
input_number = int(input("Type your the length of your passwordf(minimum is 4): "))
if input_number < 4:
    print("Too small number, it should be more than or equal to 4")
else:
    password = create_password(input_number)
    print(f"Your new password is {password}")
