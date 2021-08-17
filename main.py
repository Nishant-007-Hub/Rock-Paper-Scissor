# Rock Paper Scissor Game

print("let's play the Rock Paper Scissor Game")
total_turn = 10
your_score = 0
comp_score = 0
draw_count = 0
print("You have total", total_turn, "chances")

import random

list = ["rock", "paper", "scissor"]

while 1:
    a = input("For rock-press:: r\n"
              "For paper-press:: p\n"
              "For scissor-press:: s\n")
    a = a.lower()
    b = random.choice(list)
    print(a, "a")
    print(b, "b")
    print(type(b), "btype")

    # Wrong input handling Programme
    if a != "r" and a != "p" and a != "s":
        print("You Entered wrong input,Let's try again")

    # Tie handling Programme
    if a[0] == b[0]: # a is only one letter from alphabats whereas b is whole word so we r matching first word only to chk
        print("Game draw::plz try again")
        draw_count = draw_count+1

    # Regular handling Programme
    if a == "r" and b == "paper":
        print("\nYou Win... \nyour score is::", your_score + 1, "\ncomp score is::", comp_score)
        your_score = your_score + 1
    elif a == "r" and b == "scissor":
        print("\nYou Win... \nyour score is::", your_score + 1, "\ncomp score is::", comp_score)
        your_score = your_score + 1
    elif a == "p" and b == "rock":
        print("\ncomputer win... \nyour score is::", your_score, "\ncomp score is::", comp_score + 1)
        comp_score = comp_score + 1
    elif a == "p" and b == "scissor":
        print("\ncomputer win... \nyour score is::", your_score, "\ncomp score is::", comp_score + 1)
        comp_score = comp_score + 1
    elif a == "s" and b == "rock":
        print("\ncomputer win... \nyour score is::", your_score, "\ncomp score is::", comp_score + 1)
        comp_score = comp_score + 1
    elif a == "s" and b == "paper":
        print("\nYou Win... \nyour score is::", your_score + 1, "\ncomp score is::", comp_score)
        your_score = your_score + 1

    print("u left::", total_turn - 1, "chance")
    total_turn = total_turn - 1
    print()

    if total_turn == 0:
        print("Game Over")
        if your_score > comp_score:
            print("Hip Hip Hurray!! You Win")
        elif your_score < comp_score:
            print("Sorry!! Computer win")
        elif your_score == comp_score:
            print("Tie let's try again")
        print("your_score is::",your_score,"\n"
              "comp_score is::",comp_score,"\n"
              "draw_count is::",draw_count,"\n")
        break
