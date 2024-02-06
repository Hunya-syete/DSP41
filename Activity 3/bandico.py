
print("Welcome To Guess Number Game")
number_to_guess = 15  
attempts = 0

while attempts < 3:
    
    user_guess = int(input("Guess a number between 1 and 20: "))
    
    if user_guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    
    elif user_guess < number_to_guess:
        print("Too low!")
    
    else:
        print("Too high!")
    
    attempts += 1

if attempts == 3:
    print("Game Over!")
