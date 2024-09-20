'''
Deck: 52 card of
4 suits - heart, diamonds, clubs, spades
13 values - 2-10, jack, queen, kind, ace

values: 2-10 worth face value, jack-king worth 10
ace can be 1 or 11

goal: get as close to 21 as possible without going over
- if go over 21, its a bust

setup: a DEALER and a PLAYER. both dealt 2 cards
- player can see own 2 cards, and see one of dealer's cards

=== STEPS ===
- initialize a deck
- deal cards to dealer and player
- get player input for hit or stay
    - repeat until bust or stay
- if player bust dealer wins
- dealer's turn: hit or stay
    - repeat until total >= 17
- if dealer bust, player wins
- compare cards and declare winner

=== data structure ===
- populate a list for a deck of cards 4x ('ace', '1', '2', ...)
- dictionary containing value of cards
{'ace': (1, 11), '2': 2, '3': 3, etc.}
- dict of player's hand, and of dealer's hand
- when dealing, randomly select a card and assign to a party

'''

import random

VALUES = {
    'ace': 0,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    }

    
def new_deck():    
    deck = list(VALUES.keys()) * 4
    random.shuffle(deck)
    return deck

def deal(party, deck):
    party.append(deck.pop())
    
def hand_total(hand):
    total = 0
    for card in hand:
            total += VALUES[card]
    for card in hand:
        if card == 'ace':
            if total <= 10:
                total += 11
            else:
                total += 1
    return total
    
def display(hand):
    text = ''
    for card in hand[0: -1]:
        text += card + ', '
    text += 'and ' + hand[-1]
    return text
    
def play_again():
    while True:
        answer = input('Play again? (y/n)\n').casefold()
        print('-----------------------')
        if answer in ['y', 'n']:
            return answer == 'y'
    
def twentyone():
    # fresh deck
    deck = new_deck()
    
    player = []    
    dealer = []
    
    # dealing cards to player + dealer
    deal(player, deck)
    deal(player, deck)
    deal(dealer, deck)
    deal(dealer, deck)
    print(f'==> Dealer has: {dealer[-1]} and unkonwn card')
    print(f'==> You have: {player[0]} and {player[1]}')
    
    # player's' turn
    while True:
        player_choose = input("==> hit or stay?\n").casefold()
        
        if player_choose not in ('hit', 'stay'):
            print("==> not a valid selection, enter 'hit' or 'stay'")
        
        elif player_choose == 'hit':
            deal(player, deck)
            
            if hand_total(player) > 21:
                break
            else:
                print(f'==> you have {display(player)}')
            
        else:
            if player_choose == 'stay':
                break
    
    # dealer's turn
    if hand_total(player) < 21:
        while hand_total(dealer) < 17:
            deal(dealer, deck)
            print(f'==> dealer has {display(dealer)}')
            if hand_total(dealer) > 21:
                break

    
    # calc totals and anounce winner
    
    player_score = hand_total(player)
    dealer_score = hand_total(dealer)
    print('-----------------------')
    print(f'Player has {display(player)} with total of {player_score}')
    print(f'Dealer has {display(dealer)} with total of {dealer_score}')
    
    if (player_score > 21):
        print(f'Dealer Wins!')
    elif (dealer_score > 21):
        print(f'Player Wins!')
    elif dealer_score > player_score:
        print(f'Dealer Wins!')
    elif player_score > dealer_score:
        print(f'Player Wins!')
    else:
        print(f"It's a tie!")
    print('-----------------------')
            
    
def main():
    while True:
        twentyone()
        if not play_again():
            break


main()
