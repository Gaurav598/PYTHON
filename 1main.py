import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter you choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
everseDict = {1: "snake", -1:"water", 0:"gun"}
you = youDict[youstr]

# by now, we have two 2 numbers(variables), you and computer

print(f"you chose {everseDict[you]}\ncomputer chose {everseDict[computer]}")

if(computer == you):
    print("Its a draw!")
    
else:
    if(computer == -1 and you == 1):
        print("you win!")
    
    elif(computer == -1 and you == 0):
        print("you lose!")
    
    elif(computer == 1 and you == -1):
        print("you lose!")

    elif(computer == 1 and you == 0):
        print("you win!")

    elif(computer == 0 and you == -1):
        print("you win!")

    elif(computer == 0 and you == 1):
        print("you lose!")
    
    else:
        print("Something went wrong!")