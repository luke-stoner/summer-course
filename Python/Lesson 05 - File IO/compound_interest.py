def compound_interest(P: float, r: float, t: int, n=1) -> float:
    return P*(1+r/n)**(n*t)

print(compound_interest(1000, .0061, 10, 1))
