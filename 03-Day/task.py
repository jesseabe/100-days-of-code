try:
    print("Welcome to the rollercoaster!")
    height = float(input("What's your Height? "))
    bill = 0

    if height > 1.20:
        age = int(input("Whats your age? "))
        if age > 18:
            bill = 12
            print(f"Adults tickets are ${bill}")
        elif age >= 12:
            bill = 7
            print(f"Youth tickets are ${bill}")        
        else:
            bill = 5
            print(f"Child tickets are ${bill}")

        wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No: ")

        if wants_photo == "y":
            bill += 3 

        print(f"Your final bill is {bill}")
            

    else:
        print("You need to grow taller before you can ride!")

except:
    print("Error")