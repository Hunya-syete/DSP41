Name = input("Name: ")
Math = float(input("Grade in  Math: "))
Science = float(input("Grade in Science: "))
English = float(input("Grade in English: "))
average = (Math + Science + English)/3
print(average)

if average <=(74):
    print("Sorry You Failed The Semester")
if average >(74):
    print("Congratulations You Passed The Semester")
if Math <=float(74):
    print("But you need to re-enroll Math")
if Science <=(74):
    print("But you need to re-enroll Science")
if English <=(74):
    print("But you need to re-enroll English")
