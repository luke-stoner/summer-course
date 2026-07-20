import area

def print_boarding_list(passengers):
    for seat, passenger in enumerate(passengers, start=1):
        print(f"Seat {seat}: {passenger}")

passengers = ['tom', 'dick', 'harry']
print_boarding_list(passengers)