import random
def game():
    num2g = random.randint(1,20)
    attempts=3
    for attempt in range(3):
        Uguess=int(input("Guess the Number (1-20)"))
        if Uguess == num2g:
            print("Congrats! U Gussed it")
            return
        elif Uguess < num2g:
            print("too low.")
        else:
            print("Too High")

    print(f" U ran out of attempts. The Number was {num2g}.")
game()
