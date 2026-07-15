import math

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

try: 
    math.sqrt(num)
    try:
        1/num
        print("The number is positive.")
    except:
        print("The number is zero.") 
    
except ValueError:
    print("The number is negative.")

