import random
import string

letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation
# my plan: make list of chars and pick them
# password_char_list = [letters, numbers, special_chars]
# best plan
password_char_list = letters + numbers + special_chars


def create_password(passNum):
    password = ""
    
    # password_length = passNum
    # while password_length > 0:
    #     password_char = random.choice(password_char_list)
    #     # print("password_char", password_char)
    #     password += random.choice(password_char)
    #     # print("password", password)
    #     password_length -= 1
    
    for i in range(passNum):
        password += random.choice(password_char_list)
        
    return password
    
    
input_number = int(input("Type the length of your password: "))
password = create_password(input_number)
print(f"Your new password is {password}")
