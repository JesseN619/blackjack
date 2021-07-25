from random import choice
import os
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
         
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
        self.cards[new_card] = new_deck.deck[new_card]
        del new_deck.deck[new_card]

    def start(self):
        while len(self.cards) < 2:
            self.select_card()

    def show_player_cards(self):
        print("\nYour cards:")
        for card in self.cards:
            if len(self.cards) < 2:
                input("Press 'Enter' to have the dealer deal you a card... ")
            print(card)
        print(f"\nYour score: {self.score()}\n")

    def score(self):
        score = sum(list(self.cards.values()))
        return score

    def check_blackjack(self):
        if self.score() == 21:
            return "blackjack"

    def hit_or_stand(self):
        while self.score() < 21:
            play = input("'Hit' or 'Stand'? ")
            if play.lower() != 'hit' and play.lower() != 'stand':
                print("Invalid response. Please type 'hit' or 'stand'.")
                continue
            elif play.lower() == 'hit':
                clear()
                self.select_card()
                self.show_player_cards()
                dealer.show_1_dealer_card()
            elif play.lower() == 'stand':
                return
        if self.score() > 21:
            return "bust"


class Dealer(Player):
    def show_1_dealer_card(self):
        for i in range(len(self.cards.keys())):
            if i == 0:
                print(f"\nDealer cards:\n{list(self.cards.keys())[i]}")
            else:
                print("*Hidden card*")
        print("\n")

    def show_dealer_cards(self):
        print("\nDealer cards:")
        for card in self.cards:
            print(card)
        print(f"\nDealer score: {self.score()}\n")
    
    def dealer_hit_stand(self):
        while self.score() < 17:
            input("Dealer score is less than 17, so Dealer must hit. Press 'Enter' to continue... ")
            dealer.select_card()
            clear()
            player.show_player_cards()
            dealer.show_dealer_cards()
    
        if self.score() > 21:
            return "bust"


class Game:
    def start_game(self):
        clear()
        print("Welcome to Jesse's Blackjack Table!\n")
        print("(Face cards have a value of 10. Aces only have a value of 11.)\n")
        input("Press Enter to start game... ")
        clear()
        new_deck.create_new()
        player.start()
        player.show_player_cards()
        dealer.start()
        dealer.show_1_dealer_card()
        if player.score() == 21:
            input("\nPress Enter to reveal dealer cards... ")
            clear()
            player.show_player_cards()
            dealer.show_dealer_cards()
            if dealer.score() == 21:
                print(f"{'-'*6}\n Push\n{'-'*6}\n")
                return
            else:
                print(f"{'-'*22}\n Blackjack! You won!\n{'-'*22}\n")
                return
        play = player.hit_or_stand()
        input("Press Enter to reveal dealer cards... ")
        clear()
        player.show_player_cards()
        dealer.show_dealer_cards()
        if play == "bust":
            print(f"{'-'*7}\n Bust!\n{'-'*7}\n")
            return

        dealer_play = dealer.dealer_hit_stand()
        if dealer_play == "bust":
            print(f"{'='*23}\n Dealer bust. You won!\n{'='*23}\n")
            return
        outcome = self.check_outcome()
        if outcome == "player win":
            print(f"{'-'*10}\n You won!\n{'-'*10}\n")
            return
        elif outcome == "dealer win":
            print(f"{'='*12}\n Dealer won\n{'='*12}\n")
            return
        elif outcome == "push":
            print(f"{'-'*6}\n Push\n{'-'*6}\n")
            return

    def check_outcome(self):
        player_diff = 21 - player.score()
        dealer_diff = 21 - dealer.score()
        if player_diff == dealer_diff:
            return "push"
        elif player_diff < dealer_diff:
            return "player win"
        else:
            return "dealer win"

clear()
while True:
    play_or_no = input("Would you like to play a game of blackjack? (y/n) ")
    if play_or_no.lower() == 'y':
        # self.start_game()
        new_deck = Deck()
        new_game = Game()
        player = Player()
        dealer = Dealer()
        new_game.start_game()
    elif play_or_no.lower() == 'n':
        break