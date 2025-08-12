import random

from game_data import data

score = 0

random.shuffle(data)


def format_data(account):
    """format data as we wish """
    account_name = account["name"]
    account_description = account["profession"]
    account_country = account['country']
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """take data and check answer"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


game_is_on = True
account_a = random.choice(data)
while game_is_on:

    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"with: B: {format_data(account_b)}")

    guess = input("who has more follower count \n").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)
    if is_correct:
        account_a=account_b
        score += 1
        print(f"you are right, current_score {score}")

    else:
        print(f"you are wrong, final_score: {score}")
        game_is_on = False
