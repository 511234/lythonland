import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        # must use int(input()), otherwise interpreter reads it as string and cannot execute logical operators
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess too low.')
        elif guess > random_number:
            print('Sorry, guess too large')
    print(f'The correct answer is {guess}!')

guess(10)