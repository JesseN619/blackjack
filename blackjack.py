from random import choice
# initialize with deck (dict)
# face cards are 10, ace is 11
# random.choice(list(adict.keys()))
# player gets two cards, dealer gets two but can only see one
# if player == 21, 'blackjack'
# 'hit' to get additional card, 'stand' when done
# if > 21, bust
# when player says 'stand', dealer reveals card, takes another if <= 16
# if dealer > 21, dealer bust
# winner is closest to 21 without going over


class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
         
class Deck:
    def __init__(self):
        self.deck = {}

    def create_new(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        names = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        for suit in suits:
            for name in names:
                if name == 'Jack' or name == 'Queen' or name == 'King':
                    self.deck[name + ' of ' + suit] = 10
                elif name == 'Ace':
                    self.deck[name + ' of ' + suit] = 11
                else:
                    self.deck[name + ' of ' + suit] = int(name)

class Player:
    def __init__(self):
        self.cards = {}

    def select_card(self):
        new_card = choice(list(new_deck.deck.keys()))
        # print(f"{new_card} is new card.")
        self.cards[new_card] = new_deck.deck[new_card]
        # print(f"Player cards is now: {self.cards}")
        del new_deck.deck[new_card]
        # print(f"Deck is now: {new_deck.deck}")

    def start(self):
        while len(self.cards) < 2:
            self.select_card()

    def show_player_cards(self):
        print("Player cards:")
        for card in self.cards:
            print(card)

    # def show_1_dealer_card(self):
    #     for i in range(len(self.cards.keys())):
    #         if i == 0:
    #             print(f"Dealer cards:\n{list(self.cards.keys())[i]}")
    #         else:
    #             print("*Hidden card*")

    # def show_dealer_cards(self):
    #     print(f"Dealer cards:\n{self.cards}")

class Dealer(Player):
    def show_1_dealer_card(self):
        for i in range(len(self.cards.keys())):
            if i == 0:
                print(f"Dealer cards:\n{list(self.cards.keys())[i]}")
            else:
                print("*Hidden card*")

    def show_dealer_cards(self):
        print(f"Dealer cards:\n{self.cards}")



class Game:
    def start_game(self):
        new_deck.create_new()
        player = Player()
        player.start()
        player.show_player_cards()
        dealer = Dealer()
        dealer.start()
        # print(list(dealer.cards.keys()))
        dealer.show_1_dealer_card()
        




# new_game = Game()
# new_game.start_game()

new_deck = Deck()
# new_deck.create_new()
new_game = Game()
new_game.start_game()
