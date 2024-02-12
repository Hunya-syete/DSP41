import random

def play_game():
    number = random.randint(1, 20)
    attempts = 0

    while attempts < 3:
        guess = int(input("Guess the number between 1 and 20: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in " + str(attempts) + " tries!")
            return True

    print("Sorry, you didn't guess the number in 3 tries. The number was " + str(number))
    return False

def main():
    while True:
        if play_game():
            break

        play_again = input("Do you want to play again (yes/no)? ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
