# 0 = rock, 1 = paper, 2 = scissors"
def rock_paper_scissors(p1, p2):
    if (p1 < 0 or p1 > 2) or (p2 < 0 or p2 > 2): return "Wrong Hands"
    if p1 == p2: return "draw"
    if p1 == 0:
        if p2 == 1: return "p2 Win"
        if p2 == 2: return "p1 Win"
    elif p1 == 1:
        if p2 == 0: return "p1 Win"
        if p2 == 2: return "p2 Win"
    elif p1 == 2:
        if p2 == 0: return "p2 Win"
        if p2 == 1: return "p1 Win"
        
print("Choose your hands 0 = rock, 1 = paper, 2 = scissors")
p1_hand = int(input("P1 choose your hands: "))
p2_hand = int(input("P2 choose your hands: "))
print(rock_paper_scissors(p1_hand, p2_hand))
