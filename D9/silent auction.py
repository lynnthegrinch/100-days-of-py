import os
highest_bid = 0
print('welcome to the auction')
bids = {}
more_people = True
while more_people:
    name = input("what's your name: ")
    bid = int(input("what's your bid? "))
    bids[name] = int(bid)
    question = input("is there more people? y or n")
    if question != "y":
        more_people = False
    elif question == "y":
        os.system('cls')
print(bids)
for i in bids:
        if bids[i] > highest_bid:
            highest_bid = bids[i]
            bidder = i
print(f"our winner is {bidder} with {highest_bid}$")
