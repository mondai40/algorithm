import time

hour = int(input("Type your hour: "))
minute = int(input("Type your minute: "))
second = int(input("Type your second: "))

def display_clock():
    print(f"{hour}:{minute}:{second}")
    print("")

def add_second():
    global hour
    global minute
    global second
    
    second += 1
    
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

# !!!This is infinite loop!!!
while True:
    time.sleep(1)
    add_second()
    display_clock()
