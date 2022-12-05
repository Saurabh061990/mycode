import random
win_num=43
guess=1
number= int(input("guess a number between 1 to 100 : "))
game_over= False

while not game_over:
    if number ==win_num:
        print("You Win!!!!!! and you guess right number....")
        game_over= True
    else:
        if number< win_num:
            print("too low.....")
            guess +=1
            number=int(input("Guess Again :"))
        else:
             print("too high.....")
             guess +=1
             number=int(input("Guess Again :"))
