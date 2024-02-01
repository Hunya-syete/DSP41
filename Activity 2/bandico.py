service = int(input("Enter Employees Years of Service: "))
dept = str(input("Enter Department: ")).upper()

if dept == "IT":
     if service >= 10: print("You got 10000 initiatives")
     else: print("You got 5000 initiatives")

elif dept == "ACCT":
     if service >= 10: print("You got 12000 initiatives") 
     else: print("You got 6000 initiatives")

elif dept == "HR":
     if service >= 10: print("You got 15000 initiatives")
     else: print("You got 7500 initiatives")

else: print("Invalid department")
