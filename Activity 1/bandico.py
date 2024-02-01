name = input("Name: ")
math = int(input("Math Grade: "))
science = int(input("Science Grade: "))
english = int(input("English Grade: "))

average = (math + science + english) / 3

if average >= 75:
    print("Congratulations! You passed the semester.")
else:
    print("Sorry, you failed the semester.")

if math < 75:
    print("But you need to re-enroll Math subject.")
if science < 75:
    print("But you need to re-enroll Science subject.")
if english < 75:
    print("But you need to re-enroll English subject.")
