import random

def get_random_index(length, num_index):
  ri = []
  while len(ri) < num_index:
    n = random.randint(0, length)
    if not n in ri:
      ri.append(n)
  return ri

def get_question():
    word_list = ["apple", "banana", "melon", "kiwi", "pineapple"]
    answer = random.choice(word_list)
    print(answer)

    random_index = get_random_index(len(answer) - 1, 2)
    print(random_index)
    
    question = ""
    for i in range(0, len(answer)):
        if i in random_index:
            question += "_"
        else:
            question += answer[i]
    return question

def check_answer(hint, word):
    if len(hint) != len(word): return "You Lose!!! Length"
    for i in range(len(hint)):
        if hint[i] == "_": continue
        if hint[i] != word[i]: return "You Lose!!! Letter"
    return "You Win!!!"
        
def word_completion():
    print("Welcome to Word Completion")
    hint = get_question()
    print("Hind: " + hint)
    input_word = input("Type your word from the hint: ")
    print(check_answer(hint, input_word))
    
word_completion()
