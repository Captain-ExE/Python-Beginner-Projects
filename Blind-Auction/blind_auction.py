from replit import clear

bids = {}
bidding_finished = False


def Highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        Highest_bidder(bids)
    elif should_continue == "yes":
        clear()
