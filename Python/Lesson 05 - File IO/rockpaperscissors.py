from random import choice
from time import sleep

odd_games = False
while odd_games == False:
    number_games = int(input(f"\nHow many games would you like to play?: "))
    sleep(1)
    if number_games % 2 == 1 and number_games <= 9:
        odd_games = True
    else:
        print("\nEnter an odd number of games between 1 and 9")

winning_num = number_games // 2 + 1
user_wins = 0
comp_wins = 0
art_dict = {
    "Rock": """
___________
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
""",
    "Paper":
    """
    _______
---'    ____)
        ______)
        _______)
        _______)
---.__________)
""",
    "Scissors":
    """
______
______)_______
        ______)
    __________)
    (____)
____(___)
"""
}

while user_wins < winning_num and comp_wins < winning_num:
    user_choice = input("\nRock, Paper, or Sissors?: ").capitalize()
    sleep(1)
    print(f"\nUser: {art_dict[user_choice]}")
    sleep(1)
    computer_choice = choice(["Rock", "Paper", "Scissors"])
    sleep(1)
    print(f"Computer: {art_dict[computer_choice]}")
    sleep(1)
    choice_combo = tuple(sorted([user_choice, computer_choice]))

    result_dict = {
        ("Paper", "Rock"): "Paper",
        ("Paper", "Scissors"): "Scissors",
        ("Paper", "Paper"): "Tie",
        ("Rock", "Rock"): "Tie",
        ("Rock", "Scissors"): "Rock",
        ("Scissors", "Scissors"): "Tie",
    }

    if result_dict[choice_combo] == "Tie":
        print(f"\nIt's a Tie! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
    elif result_dict[choice_combo] == user_choice:
        print(f"\nYou Win! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
        user_wins += 1
        print(f"\nScore: User {user_wins}, Computer {comp_wins}")
    else:
        print(f"\nYou Lose! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
        comp_wins += 1
        print(f"\nScore: User {user_wins}, Computer {comp_wins}")

sleep(1)
if user_wins > comp_wins:
    "Game over! You win!"
else:
    "Game over! You lose!"