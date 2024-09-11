import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    
    if(a>n):
        print("Lower Number Please")
        guesses += 1
    else:
        print("Higher number please")
        guesses += 1
        
print(f"You have Gusses The Number {n} Correctly in {guesses} attempt")