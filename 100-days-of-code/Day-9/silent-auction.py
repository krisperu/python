from replit import clear
from art import logo

print(logo)
bids = {}
more_bids = False

def auction(bidding_record):
    highest_bid = 0
    winner = ""
    for name in bidding_record:
        price = bidding_record[name]
        if price > highest_bid:
            highest_bid = price
            winner = name
    print(f"The auction is complete. {winner} won the auction with a bid of ${highest_bid}.")

while not more_bids:
    bidder = input("What is your name: ")
    bid = int(input("How much do you want to bid: $"))
    bids[bidder] = bid
    ans = input("Are there more bidders? Type 'yes' or 'no'. \n")
    if ans == "no":
        more_bids = True
        auction(bids)
    elif ans == "yes":
        clear()


