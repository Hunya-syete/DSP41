import random

number = random.randint(1,20)

for i in range(3):
    guess = int(input("Guess the number between 1 and 20: "))
    
    if guess < number:
        print ("Too low!")
    elif guess > number:
        print("Too high!")
    else:
      print( "Congratulations! You guessed the number in " + str(i) + "tries!")
      break
else:
        print("Sorry, you didn't guess the number in 3 tries. The numberwas" + str(number))
