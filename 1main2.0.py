import random
'''
1 for rock
-1 for paper
0 for scissor
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter you choice: ")
youDict = {"r": 1, "p": -1, "s": 0}
everseDict = {1: "rock", -1: "paper", 0: "scissor"}
you = youDict[youstr]

# by now, we have two 2 numbers(variables), you and computer

print(f"you chose {everseDict[you]}\ncomputer chose {everseDict[computer]}")

if(computer == you):
    print("Its a draw!")
    
else:
    if(computer == -1 and you == 1):
        print("you lose!")
    
    elif(computer == -1 and you == 0):
        print("you win!")
    
    elif(computer == 1 and you == -1):
        print("you win!")

    elif(computer == 1 and you == 0):
        print("you lose!")

    elif(computer == 0 and you == -1):
        print("you lose!")

    elif(computer == 0 and you == 1):
        print("you win!")

    else:
        print("Something went wrong!")