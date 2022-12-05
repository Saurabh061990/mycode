# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=int(input("Enter the third number"))
# a,b,c=input("enter 3 numbers by comma seperated ").split(",")
# print(f"Average of three number is {(int(a)+int(b)+int(c))/3}")


#Guess Number Game Program code..............
import random
win_num=random.randint(1,100)
guess=1
number= int(input("guess a number between 1 to 100 : "))
game_over= False

while not game_over:
    if number ==win_num:
        print(f"You Win!!!!!! and you guess the number in {guess} number....")
        game_over= True
    else:
        if number< win_num:
            print("too low.....")
        else:
             print("too high.....")

        guess +=1
        number=int(input("Guess Again :"))
