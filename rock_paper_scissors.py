'''
1 for rock
0 for paper
-1 for scissors
'''

import random

computer = random.choice([1,-1,0])

you_dict = {"r":1, "p":0, "s":-1} # short form where i can input string in youstr
youstr = input("Enter your choice: ")

reverse_dict = {1:"Rock",0:"Paper",-1:"Scissors"}

you = you_dict[youstr]

# now you have 2 number(variables) you and computer

print(f"You chose {reverse_dict[ you]}\nComputer chose {reverse_dict[ computer]}") # reversedict is used here bcz it has full forms of 1,0,-1


if(computer==you):
    print("It's a draw")

else:
    if(computer== 1 and you == -1):
        print("You lost")

    elif(computer ==1 and you ==0):
        print("You win!")

    elif(computer ==0 and you==-1):
        print("You win!")

    elif(computer==0 and you==1):
        print("You lost")

    elif(computer==-1 and you==1):
        print("You win!")

    elif(computer==-1 and you==0):
        print("You lost")

    else:
        print("Something went wrong")

