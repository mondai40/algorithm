from datetime import datetime

def get_birthday():
    birthday = None
    question_flag = False
    while not question_flag:
        input_data = input("When is your birthday? Format should be MM/DD/YYYY: ")
        try:
            birthday = datetime.strptime(input_data, "%d/%m/%Y")
            question_flag = True
        except (TypeError, ValueError):
            print("Something Wrong")
    return birthday
    
def get_age(birthday):
    today = datetime.today()
    days = (today - birthday).days
    age = days // 365
    return age
    
birthday = get_birthday()
age = get_age(birthday)
print(f"Your age is {age}")
