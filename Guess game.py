Max_turn = 0
while (True):
    print("type ur number:")
    i = int(input())

    if i==18:
        print("correct")
        print("No. of turns:",Max_turn)
    elif Max_turn == 9 :
        print("you are out of turns")
        break

    else:
        print("try again")
        Max_turn = Max_turn + 1
