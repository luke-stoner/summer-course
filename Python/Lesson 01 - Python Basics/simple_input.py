pizza_diameter = int(input("Enter the diameter of the pizza in inches: "))
pizza_cost = float(input("Enter the cost of the pizza in dollars: "))

print(f"Price per square inch: ${pizza_cost / (3.14 * (pizza_diameter / 2) ** 2):.2f}")



pizza1_diameter = int(input("Enter the diameter of the two pizzas in inches: "))
pizza1_cost = float(input("Enter the cost of the two pizzas in dollars: "))
pizza2_diameter = int(input("Enter the diameter of the large pizza in inches: "))
pizza2_cost = float(input("Enter the cost of the large pizza in dollars: "))       

pizza1_total_area = 2 * (3.14 * (pizza1_diameter / 2) ** 2)
pizza2_area = 3.14 * (pizza2_diameter / 2) ** 2

pizza1_cost_per_square_inch = pizza1_cost / pizza1_total_area
pizza2_cost_per_square_inch = pizza2_cost / pizza2_area

if pizza1_cost_per_square_inch < pizza2_cost_per_square_inch:
    print("The first pizza is the better deal.")
    print(f"Price per square inch of the two pizzas: ${pizza1_cost_per_square_inch:.2f}")
elif pizza1_cost_per_square_inch > pizza2_cost_per_square_inch:
    print("The second pizza is the better deal.")
else:
    print("Both pizzas are the same deal.")
