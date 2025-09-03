balance = 5 
vending_machine = {"chips" : 3, "soda" : 5, "candy": 2}

while balance > 0:
    # buy something 
    print("\nYour Balance: ", balance)
    print("Menu:")
    for item, price in vending_machine.items():
        print(f"{item} - ${price}")

        choice = input("Choose a snack (or 'quit'): ")
        print(f"you have selected {choice}")
        
        balance = balance - price