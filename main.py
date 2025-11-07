bidders = {}
print("Welcome to Blind Auction\n")
continue_bidding = True
while continue_bidding:
    name = input("What is your name\n")
    price = int(input("What is your bid\n"))
    bidders[name] = price
    exit_loop = True
    while exit_loop:
        other_bidders = input("Are there any other bidders? type yes or no\n").lower()
        if other_bidders == "yes":
            print("\n" * 50)
            exit_loop = False
        elif other_bidders == "no":
            print("\n" * 50)
            exit_loop = False
            continue_bidding = False
        else:
            print("Invalid input. Try again")

winner_value = 0
winner = []
for i in bidders:
    if bidders[i] > winner_value:
        winner_value = bidders[i]
        winner = [i]
    elif bidders[i] == winner_value:
        winner.append(i)
if len(winner) == 1:
    print(f"The winner is {winner[0]} with a bid of {winner_value}")
else:
    print(f"its a tie, winning bid value: {winner_value}")
    print("the winners are: ")
    for name in winner:
        print(name)
input("Press enter to exit...")
