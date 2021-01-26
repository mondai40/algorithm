import random

def bulls_and_cows():
    answer = str(random.randint(1000, 9999))
    # print("Correct Number: " + answer)
    print("Welcome to Bulls and Cows")
    
    life = 5
    while life > 0:
        input_number = input("Guess a 4 digits number: ")
        bulls = 0
        cows = 0
        if input_number == answer:
            print("You Win!!!")
            break
        for i in range(len(input_number)):
            if input_number[i] == answer[i]:
                bulls += 1
                continue
            if input_number[i] in answer:
                cows += 1
                continue
        print("Bulls: " + str(bulls) + ", Cows: " + str(cows))
        
        life -= 1
        if life == 0:
            print("You Lose!!!")
            break

bulls_and_cows()
