import Art

print(Art.logo)




def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: \n ")
    price = int(input("What is your bid?: \n $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        # Clear the screen (by printing newlines) before revealing the winner
        print("\n" * 50) # You can adjust the number of newlines
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear the screen (by printing newlines) for the next bidder
        print("\n" * 50) # You can adjust the number of newlines