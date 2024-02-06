import random

secret_number = random.randint(1, 20)

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    user_guess = int(input("Guess the number (between 1 and 20): "))

    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    if attempt == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")
