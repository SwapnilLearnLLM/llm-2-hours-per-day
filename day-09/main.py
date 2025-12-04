from auction_art import logo

print(logo)
print("Welcome to the secret auction program.")

should_continue = True

bidding_info = {}

def find_highest_bidder(bidding_info):
    winner = ""
    highest_bid = 0
    for bidder in bidding_info:
        bid_amount = bidding_info[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print (f"The winner is {winner} with a highest bid of ${highest_bid}")


while should_continue:
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid? $ "))
    bidding_info[name] = bid
    other_user = input("Are there any more bidders? yes or no \n").lower()
    if other_user == "no":
        should_continue = False
        find_highest_bidder(bidding_info)
    else:
        print("\n" * 50)
bidding_info[name] = bid


