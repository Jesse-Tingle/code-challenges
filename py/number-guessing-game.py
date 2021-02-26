import random

# Computer generates a random number for the user to guess.
randomNumber = random.randint(1, 20)
num = int

# for testing 
# print("randomNumber: ", randomNumber)

min = 1 
max = 0 

num = int(input("Guess a number between 1-20: "))
if num == randomNumber:
    print("Wooohooo! You guessed it!")

while (num != randomNumber ):
    if num == randomNumber:
        print("Wooohooo! You guessed it!")
    elif num < randomNumber:
        min = num + 1
        print("Too low.")
        num = int(input("Guess again: "))
    elif num > randomNumber:
        max = num - 1
        print("Too high!")
        num = int(input("Guess again: "))
    

print(f"Wooohooo! You guessed it. The number is {num}!")