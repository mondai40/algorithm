import random

def get_question():
    word_list = ["japan", "america", "cornerstone", "philadelphia"]
    answer = random.choice(word_list)
    hint = answer[0] + "_" * (len(answer) - 1)
    print('in funcf', answer, hint)
    return answer, hint
    
def hang_man():
    print("Welcome to Hang Man")
    answer, hint = get_question()
    print(f"Hint: {hint}")
    
    life = 5
    while life > 0:
        new_hint = ""
        input_word = input("Type your word: ")
        if answer == input_word:
            print("Your Win!!!")
            break
        else:
            if len(answer) != len(input_word):
                print("Wrong! Length")
            else:
                print(answer, len(answer))
                for i in range(0, len(answer)):
                    if answer[i] == input_word[i]:
                        new_hint += answer[i]
                    else:
                        new_hint += "_"
            
        life -= 1
        if life == 0:
            print("You Die!!!")
            break
        else:
            print(f"Close!!! New Hint: {new_hint}")
            continue
        
                

hang_man()
    
