print("Welcome to the tip calculator")

try:
    # Check if bill input is valid
    bill = float(input("What was the total bill? $"))
    if bill <= 0:
        raise ValueError("The bill amount must be greater than zero.")
    
    # Check if tip input is valid
    tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
    if tip not in [10, 12, 15]:
        raise ValueError("Please choose a valid tip percentage: 10, 12, or 15.")
    
    # Check if people number input is valid
    people = int(input("How many people to split the bill? "))
    if people <= 0:
        raise ValueError("The number of people must be greater than zero.")
    
    # Calculate the amount each person should pay
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    print(f"Each person should pay: ${final_amount:.2f}")
    
except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError:
    print("Number of people cannot be zero.")


