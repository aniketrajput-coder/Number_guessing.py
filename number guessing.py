import random

def guess_no_game():
    number = random.randint(1,100)
    guess = None
    tryi = 0

    print("Guess the number between 1 to 100.....")

    while guess != number:
        guess = int(input("Enter your guesed number : "))
        tryi += 1
 
        if guess > number :
            print("To high try again ")
        elif guess < number:
            print("To low try again ")
        else :
            print("You Guessed the the right number congratulation ")
            print("Total attempt take",tryi)

guess_no_game()