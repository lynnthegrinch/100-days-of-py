import os, random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
Game = True
Player = False
Dealer = False
print("let's play some blackjack")
print("Setting up the game")
while Game == True and Player == False or Dealer == False:
    player_cards = random.choices(deck, k=2) #setting up. player's deck
    print(f"player's cards: {player_cards}")
    total_player = 0
    for i in player_cards:
        total_player += i       
    print(f"player's total is {total_player}")
    dealer_cards = random.choices(deck, k=2)#dealer
    total_dealer = 0
    for i in dealer_cards:
        total_dealer += i 
    print(f"dealer's card: {dealer_cards[0]}")
    print("player's turn")
#player's turn
    while Player == False:
        if total_player == 21:
                print(f"player's cards: {player_cards}")
                print('player wins')
                Player = True #change of flags
                Dealer = True
        elif total_player > 21:
            print(f"player's cards: {player_cards}")
            if 11 in player_cards: #check for ace
                ace = total_player - 10
                if ace <= 21:
                    player_cards.remove(11)
                    player_cards.append(1)
                    print(f"player's cards: {player_cards}")
                    continue
                else:
                    continue
            else:
                Player = True 
                Dealer = True    
                #player break game
        elif total_player < 21:
                print("do you want another card?")
                player_new = input("y or n\n")
                if player_new == "y":
                    new_card = random.choice(deck)
                    print(f"here's your new card: {new_card}")
                    player_cards.append(new_card)
                    print(f"Player's cards: {player_cards}")
                    total_player += new_card
                    print(f"player's total: {total_player}")
                    continue
                        #start again loop
                elif player_new == "n":
                    Player = True
        
#dealer's turn
    while Dealer == False: 
        if total_dealer == 21:
            print(dealer_cards)
            print("dealer won")
            Dealer = True
        elif total_dealer > 21:
                #loose, out of loop
            print(dealer_cards)
            print("dealer lost")
            Dealer = True
        elif total_dealer < 17:
            new_cardd = random.choice(deck)
            dealer_cards.append(new_cardd)
            print("dealer is playing...")
            total_dealer += new_cardd
            print(new_cardd)
            if total_dealer >= 17:
                break
    #finding end total:
    tot1 = 0
    tot2 = 0
    for i in player_cards:
        tot1 += i
    for i in dealer_cards:
        tot2 += i               
    #ends loop when above 17 or 
    #out of small loops
    print("let's see the results...")
    if tot1 <= 21 and tot2 <= 21:
        if tot1 == tot2:
            print(f"player: {tot1}")
            print(f"dealer: {tot2}")
            print("it's a draw")
        elif tot1 > tot2:
            print(f"player: {tot1}")
            print(f"dealer: {tot2}")
            print("player wins")
        elif tot1 < tot2:
            print(f"player: {tot1}")
            print(f"dealer: {tot2}")
            print("dealer wins")
    if tot1 > 21 and tot2 <= 21:
        print(f"player: {tot1}")
        print(f"dealer: {tot2}")
        print("Dealer won")
    if tot2 > 21 and tot1 <= 21:
        print(f"player: {tot1}")
        print(f"dealer: {tot2}")
        print("player won")

    #want to play again
    game = input("wanna play again? y or n")
    if game == 'y':
        os.system('cls')
        Player = False
        Dealer = False
        continue
    elif game == 'n':
        Game = False
