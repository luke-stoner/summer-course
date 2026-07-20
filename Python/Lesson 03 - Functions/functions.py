def area(l:int, w:int) -> int:
    return l*w

# len = int(input("What is the length?: "))
# width = int(input("What is the width?: "))
# print(f"The area is {area(len,width)}")

def tip(total: float, percent: float) -> list:
    tip = total * (percent/100)
    return tip, tip + total 

# bill = float(input("How much was the bill? "))
# percentage = float(input("What percentage would you like to tip? "))
# user_tip, user_total = tip(bill, percentage)
# print(f"Tip: {user_tip: .02f}, New Bill Total: {user_total: .02f}")

def has_more_characters(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        return f"{str1} is longer"
    elif len(str1) < len(str2):
        return f"{str2} is longer"
    else:
        return "The strings are the same length"
    
word1 = input("What is the first word? ")
word2 = input("What is the second word? ")
print(has_more_characters(word1, word2))
