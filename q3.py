import random

def randomguess():
    randomno=random.randint(0,99)
    print(randomno)
    guesses=0
    correct=False
    guess = int(input("Guess a number between 0 and 99: "))
    guesses += 1
    while not correct:
        while guess <0 or guess >99:
            guess=("you have guessed below 0 or above 99 guess again ")
        guess+=1
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

