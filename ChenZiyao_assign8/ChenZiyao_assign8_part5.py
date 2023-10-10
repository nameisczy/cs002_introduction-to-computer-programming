#Part 5
while True:
    bank = int(input("How much money do you want to give for playing the game? "))
    if bank <= 0:
        print("Invalid number. Try again.")
    else:
        break
while bank > 0:
    print("You have", bank)
    while True:
        money = int(input("How much money do you want to give for this time? "))
        if money > bank or money <= 0:
            print("Invalid number. Try again")
        else:
            break
    cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
    values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]
    import random
    c1 = random.choice(cards)
    n1 = cards.index(c1)
    v1 = values[n1]
    c2 = random.choice(cards)
    n2 = cards.index(c2)
    v2 = values[n2]
    player_cards = [c1, c2]
    player_values = [v1, v2]
    while True:
        player_sum1 = 0
        player_sum2 = 0
        for i in range(len(player_cards)):
            if 'Ace' in player_cards[i]:
                player_sum1 = player_sum1 + 1
                player_sum2 = player_sum2 + 11
            else:
                player_sum1 = player_sum1 + player_values[i]
                player_sum2 = player_sum2 + player_values[i]
        if player_sum2 > 21:
            player_sum2 = player_sum1
        if player_sum1 != player_sum2:
            print("Player hand:",player_cards,"is worth",player_sum1,"or",player_sum2)
            if player_sum2 == 21:
                print("You got Blackjack!  You win!")
                bank = bank + money
                break
        else:
            print("Player hand:",player_cards,"is worth",player_sum1)
        if player_sum1 > 21:
            print("Bust!")
            print("Computer Wins!")
            bank = bank - money
            break
        elif player_sum1 < 21:
            choice = input("(h)it or (s)tand? ")
            if choice == 'h':
                c3 = random.choice(cards)
                print("You drew " + c3)
                player_cards.append(c3)
                n3 = cards.index(c3)
                v3 = values[n3]
                player_values.append(v3)
            elif choice == 's':
                print()
                c4 = random.choice(cards)
                n4 = cards.index(c4)
                v4 = values[n4]
                c5 = random.choice(cards)
                n5 = cards.index(c5)
                v5 = values[n5]
                computer_cards = [c4, c5]
                computer_values = [v4, v5]
                while True:
                    computer_sum1 = 0
                    computer_sum2 = 0
                    for z in range(len(computer_cards)):
                        if 'Ace' in computer_cards[z]:
                            computer_sum1 = computer_sum1 + 1
                            computer_sum2 = computer_sum2 + 11
                        else:
                            computer_sum1 = computer_sum1 + computer_values[z]
                            computer_sum2 = computer_sum2 + computer_values[z]
                    if computer_sum2 > 21:
                        computer_sum2 = computer_sum1
                    if computer_sum1 != computer_sum2:
                        print("Computer hand:",computer_cards,"is worth",computer_sum1,"or",computer_sum2)
                        if computer_sum2 == 21:
                            print("Computer got 21!  Blackjack!")
                            print("Computer wins!")
                            bank = bank - money
                            break
                    else:
                        print("Computer hand:",computer_cards,"is worth",computer_sum1)
                    if computer_sum1 == computer_sum2:
                        if computer_sum1 > 21:
                            print("Bust!")
                            print("Player Wins!")
                            bank = bank + money
                            break
                        elif computer_sum1 < 21 and computer_sum1 <= player_sum2:
                            c6 = random.choice(cards)
                            print("Computer drew " + c6)
                            computer_cards.append(c6)
                            n6 = cards.index(c6)
                            v6 = values[n6]
                            computer_values.append(v6)
                        elif computer_sum1 < 21 and computer_sum1 > player_sum2:
                            print("Computer wins!")
                            bank = bank - money
                            break
                        else:
                            print("Computer got 21!  Blackjack!")
                            print("Computer wins!")
                            bank = bank - money
                            break
                    else:
                        if computer_sum2 > player_sum2:
                            print("Computer wins")
                            bank = bank - money
                            break
                        else:
                            c7 = random.choice(cards)
                            print("Computer drew " + c7)
                            computer_cards.append(c7)
                            n7 = cards.index(c7)
                            v7 = values[n7]
                            computer_values.append(v7)          
                break
            else:
                print("Invalid. Should be 'h' or 's'. Try again.")
        else:
            print("You got Blackjack! You win!")
            bank = bank + money
            break
print("You have no money left")
print("You loss")
