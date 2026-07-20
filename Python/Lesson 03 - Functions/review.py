import random

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

user_choice = input("Rock, Paper, or Sissors?: ").capitalize()
computer_choice = random.choice(["Rock", "Paper", "Scissors"])
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
    print(f"It's a Tie! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
elif result_dict[choice_combo] == user_choice:
    print(f"You Win! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
else:
    print(f"You Lose! Your Choice: {user_choice}, Computer Choice: {computer_choice}")
