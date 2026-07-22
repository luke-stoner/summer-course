with open("Python/Lesson 05 - File IO/output.txt", "r") as output:
    nums = [int(num.strip()) for num in output.readlines()]

min = 100
max = 50
count = 0
sum = 0

for num in nums:
    if num < min:
        min = num
    elif num > max:
        max = num
    count += 1
    sum += num
average = sum / count

print(f"Average: {average}")
print(f"Minimum: {min}")
print(f"Maximum: {max}")