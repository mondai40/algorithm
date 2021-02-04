from datetime import datetime

def get_birthday():
    question_flag = False
    birthday = None
    while not question_flag:
        input_data = input("When is your birthday? format should be DD/MM/YYYY: ")
        try:
            birthday = datetime.strptime(input_data, "%d/%m/%Y")
            question_flag = True
        except (ValueError, TypeError):
            print(f"Your data {input_data} is wrong. It should be DD/MM/YYYY")
    return birthday

def get_remain_days(birthday):
    now = datetime.now()
    this_birthday = datetime(now.year, birthday.month, birthday.day)
    remain_days = (this_birthday - now).days
    if remain_days < 0:
        next_birthday = datetime(now.year + 1, birthday.month, birthday.day)
        remain_days = (next_birthday - now).days
    return remain_days
  

birthday = get_birthday()
remain_days = get_remain_days(birthday)
print(f"You birthday is in {remain_days} days")


