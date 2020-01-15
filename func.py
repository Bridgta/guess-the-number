# This is a guess the number game

import random 

print('Hello. What is your name?')
name = input()

print(f'Well {name}, I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7): 
    print(f'take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print(f'Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print(f'Good job {name}! You guessed my number in {guessesTaken} guesses')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}')

