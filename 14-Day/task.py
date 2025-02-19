from game_data import data
import random

print("############# HIGHER AND LOWER #############")

# Format the account data into printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_follower, b_followers):
    """Take a user's guess and the follower counts and returns if they got ir right"""
    if a_follower > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)



    print(f"Compare A: {format_data(account_a)}")
    print(" VS ")
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False