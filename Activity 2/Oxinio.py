def calculate_bonus(years_in_service, office):
    if office == "it":
        if years_in_service >= 10:
            return 10000
        else:
            return 5000
    elif office == "acct":
        if years_in_service >= 10:
            return 12000
        else:
            return 6000
    elif office == "hr":
        if years_in_service >= 10:
            return 15000
        else:
            return 7500
    else:
        return 0  

def check_employee_status(years_in_service, office):
    bonus = calculate_bonus(years_in_service, office)

    if bonus > 0:
        print(f"Congratulations! You are eligible for a bonus of ${bonus}.")
        print(f"You are in the {office.upper()} department.")
    else:
        print("Sorry, you are not eligible for a bonus or the office specified is invalid.")


years_in_service = int(input("Enter the number of years in service: "))
office = input("Enter the office (it, acct, hr): ")


check_employee_status(years_in_service, office)
