import random


def valid_check(num):
    if num.isdigit():
        if 1 <= int(num) <= 100:
            return True
    else:
        return False


loop = True
while loop:
    number = random.randrange(1, 100)
    guessed = False
    count = 0
    guess = input("Guess the number between 1 and 100: ")
    while not guessed:
        if not valid_check(guess):
            guess = input("You might wanna guess it within a range(1-100): ")
            continue
        else:
            count = count + 1
            guess = int(guess)
            if guess < number:
                guess = input(f"{guess} is too low. Guess higher: ")
            elif guess > number:
                guess = input(f"{guess} is too high. Guess lower: ")
            else:
                print("\nYou guessed it correct ! 😁😁 ")
                print("You guessed it in ", count, " guesses.")
                guessed = True

    choice = input("Thank you for Playing. Wanna play again? (y/n): ")
    if choice.lower() != 'y':
        exit()
