from random import randint

int_list = []
for _ in range(100):
    int_list.append(randint(50,100))

with open("Python/Lesson 05 - File IO/output.txt", 'w') as output:
    [output.write(f"{num}\n") for num in int_list]
