name = input("Enter employee name: ")
years_in_service = int(input("Enter the employee's years of service: "))
office = input("Enter the employee's office (it, acct, or hr): ").lower()

if office == "it":
    if years_in_service >= 10:
        salary = 10000
    else:
        salary = 5000
elif office == "acct":
    if years_in_service >= 10:
        salary = 12000
    else:
        salary = 6000
elif office == "hr":
    if years_in_service >= 10:
        salary = 15000
    else:
        salary = 7500
else:
    print("Invalid office")
    exit()

print(name + ", Who works at " + office + f" for {years_in_service}yrs, has a salary of ${salary}.")
