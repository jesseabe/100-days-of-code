print("Welcome to Treasure Island. Your Mission is to find the treasure.")
direction = input("What direction do you want L for Left and R for Right: ").upper()
try:
    if direction == "L":
        action = input("Do you want swim or wait? Write, please: ").lower()

        if action == "wait":
            door = input("Which door? red, blue or yellow? ").lower()

            if door == "yellow":
                print("You Win!")
            else:
                print("Game Over")

        elif action == "swim":
            print("Game Over")
            
    else:
        print("Game Over")

except:
    print("Your input was wrong")