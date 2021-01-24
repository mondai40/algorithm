import random 

print("Welcome to guessing number game")
print("Type q, when you want to quit")
score = 0

while True:
    random_num = random.randint(0, 10)
    input_num = input("Guess a number between 0 to 10, q is quit: ")
    if input_num == "q":
        print("Goodbye, Your score: " + str(score))
        break
    if random_num == int(input_num):
        score += 10
        print("Correct, your new score: " + str(score))
    else:
        print("Wrong, your score: " + str(score))
