def compute_average(name):
    # Validate and input math grades
    while True:
        try:
            math_grades = float(input("Enter math grades: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for math grades.")

    # Validate and input science grades
    while True:
        try:
            science_grades = float(input("Enter science grades: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for science grades.")

    # Validate and input English grades
    while True:
        try:
            english_grades = float(input("Enter English grades: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for English grades.")

    # Calculate the average
    average = (math_grades + science_grades + english_grades) / 3

    # Print the student's grades
    print("Name:", name)
    print("Math:", math_grades)
    print("Science:", science_grades)
    print("English:", english_grades)
    print("Average:", average)

 # Determine the student's status
    if average >= 75:
        print("Congratulations! You passed the semester.")
        if english_grades < 75:
            print("But you need to re-enroll in English subject.")
        if science_grades < 75:
            print("But you need to re-enroll in Science subject.")
        if math_grades < 75:  
            print("But you need to re-enroll in Math subject.")
    else:
        print("Sorry, You failed the semester.")
# Prompt for the student's name
name = input("Enter student's name: ")
compute_average(name)

  
