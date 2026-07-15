import random

# secret_num = random.randint(1, 100)
# user_guess = int(input("Guess the secret number between 1 and 100: "))
# num_guesses = 1

# while user_guess != secret_num:
#     if user_guess < secret_num:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
    
#     user_guess = int(input("Guess the secret number between 1 and 100: "))
#     num_guesses += 1

# print(f"Congratulations! You guessed the secret number in {num_guesses} guesses.")



games = 100000
total_guesses = 0
max_num = 100

for _ in range(games):
    secret_num = random.randint(1, max_num)
    left = 1
    right = max_num
    guess = (left + right) // 2
    num_guesses = 1

    while guess != secret_num:
        if guess < secret_num:
            left = guess + 1
            guess = (left + right) // 2
        else:
            right = guess - 1
            guess = (left + right) // 2
        
        num_guesses += 1

    total_guesses += num_guesses

average_guesses = total_guesses / games
print(f"Average number of guesses over {games} games: {average_guesses:.3f}")


def total_depth(left, right, depth):
    if left > right:
        return 0
    else:
        mid = (left+right) // 2
        return (
            depth +
            total_depth(left,mid-1,depth+1) +
            total_depth(mid+1,right,depth+1)
        )


N = 100
avg_guesses = total_depth(1,N,1) / N
print(f"Numerical Average: {avg_guesses}")

