import random

def randomguess():
    randomno=random.randint(0,99)
    print(randomno)
    guesses=0
    correct=False
    guess = int(input("Guess a number between 0 and 99: "))
    guesses += 1
    while not correct:
        if guess < randomno:
            guess=int(input("Too low. Guess again: "))
            guesses+=1
        elif         guess > randomno:
            guess=int(input("Too high. Guess again: "))
            guesses+=1
        else:
            print("Correct. It took you {} guesses".format(guesses))
            correct=True
randomguess()

