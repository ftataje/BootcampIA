import random
import sys

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number. 
Type 'exit' to end the game.
Good luck!""")

print("What's your guess between 1 and 99?")

number = random.randint(1, 100)
guessIni = input("Your guess: ")
if guessIni == "exit":
    print("Goodbye!")
    sys.exit()
else:
    guess = int(guessIni)
tries = 0
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    tries += 1
    guessIni = input("Your guess: ")
    if guessIni == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        guess = int(guessIni)

if  number == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if tries == 1:
    print("Congratulations! You got it on your first try!!!!!!¡?=)(?)!!")
else:
    print("Congratulations, you've got it!")
    print("You won in", tries, "attempts!")

