# Not Freecell By Abishek Sriramulu. Student ID: 28957113. Unit: FIT9133 Assignment 2
import random


# This class Holds the card values
class Card:
    card_suit = ['S', 'H', 'C', 'D']
    card_face = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # this function adds face values if the user wants more than 13 faces
    def face_add(self, value_end):
        for x in range(14, value_end + 1):
            Card.card_face.append(str(x))

    # this function adds suits if the user wants more than 4 suits, naming the extra suits as numbers from 0 to N
    def suit_add(self, number_of_suits):
        for x in range(0, number_of_suits - 4):
            Card.card_suit.append(str(x))


# This class creates the Deck of cards and shuffles it
class Deck:
    deck_cards = []
    deck = [[], [], [], [], [], [], [], [], [], [], [], []]
    start_face = 0
    end_face = 0
    total_suits = 0

    # This constructor creates the Deck
    def __init__(self, value_start, value_end, number_of_suits):
        Deck.start_face = value_start
        Deck.end_face = value_end
        Deck.total_suits = number_of_suits
        if value_end > 13:
            Card.face_add(self, value_end)
        if number_of_suits > 4:
            Card.suit_add(self, number_of_suits)
        for suits in range(0, number_of_suits):
            for face in range(value_start - 1, value_end):
                Deck.deck_cards.append(Card.card_face[face] + Card.card_suit[suits])

    # This function shuffles the Deck and places it in 8 different lists of random sizes
    @staticmethod
    def shufflelist():
        random.shuffle(Deck.deck_cards)
        temp = 0
        while temp < 7 and len(Deck.deck_cards):
            Deck.deck[temp].extend(Deck.deck_cards[0:random.randrange(0, len(Deck.deck_cards))])
            Deck.deck_cards = [x for x in Deck.deck_cards if x not in Deck.deck[temp]]
            temp += 1
        if len(Deck.deck_cards) != 0:
            Deck.deck[temp].extend(Deck.deck_cards[0:len(Deck.deck_cards)])


# This class contains all game functions
class NotFreecell:
    # This method checks whether the entered source and target suits are of different colors
    def check_suits(self, source_value, target_value):
        if Card.card_suit.index(source_value[-1]) % 2 == 0:
            if Card.card_suit.index(target_value[-1]) % 2 == 0:
                return False
            else:
                if NotFreecell.check_face(self, source_value, target_value):
                    return True
                else:
                    return False
        else:
            if Card.card_suit.index(target_value[-1]) % 2 == 0:
                if NotFreecell.check_face(self, source_value, target_value):
                    return True
                else:
                    return False
            else:
                return False

    # This method checks whether the entered target card's face value is one step higher than source card's face value
    def check_face(self, source_value, target_value):
        if Card.card_face.index(target_value[0:-1]) - Card.card_face.index(source_value[0:-1]) == 1:
            return True
        else:
            return False

    # This method gets the inputs for making the move and checks whether the move is possible
    def check_move(self):
        print("enter the deck no. of the card you want to move or Press q to end: ")
        source = int(NotFreecell.get_input(self))
        print("enter your target deck or Press q to end: ")
        target = int(NotFreecell.get_input(self))
        if len(Deck.deck[source]) == 0:
            print("sorry the move is not possible. Enter valid inputs again")
            return NotFreecell.check_move(self)
        else:
            if len(Deck.deck[target]) == 0:
                NotFreecell.move(self, source, target)
            else:
                source_value = Deck.deck[source][-1]
                target_value = Deck.deck[target][-1]
                if NotFreecell.check_suits(self, source_value, target_value):
                    NotFreecell.move(self, source, target)
                else:
                    print("sorry the move is not possible. Enter valid inputs again")
                    return NotFreecell.check_move(self)

    # This method checks whether the game won
    def check_win(self):
        count = 0
        for temp in Deck.deck:
            if len(temp) != 0:
                count += 1
        if count == Deck.total_suits:
            for temp in Deck.deck:
                if len(temp) != 0:
                    if temp[0][0:-1] == Card.card_face[Deck.end_face - 1] \
                            and temp[-1][0:-1] == Card.card_face[Deck.start_face - 1]:
                        for i, j in zip(range(0, len(temp) - 1), range(1, len(temp))):
                            if not NotFreecell.check_suits(self, temp[j], temp[i]):
                                return False
                    else:
                        return False
            return True
        else:
            return False

    # This method displays the deck
    def display(self):
        labels = ['deck 0', 'deck 1', 'deck 2', 'deck 3', 'deck 4', 'deck 5', 'deck 6', 'deck 7', 'deck 8', 'deck 9',
                  'deck 10', 'deck 11']
        for temp, label in zip(Deck.deck, labels):
            print(label)
            print(temp)

    # This method makes the move from source deck to target deck
    def move(self, source, target):
        Deck.deck[target].append(Deck.deck[source].pop())

    # Makes sure the user provides valid input for the moves
    def get_input(self):
        num = str(input())
        if not num.isdigit() and num == 'q':
            exit()
        if not num.isdigit() or int(num) > 11:
            print("This input can have only numbers between 0 and 11 or Press q to end. Please Enter Again: ")
            return NotFreecell.get_input(self)
        else:
            return num


# Makes sure the user provides valid input for creating the deck
def get_num():
    num = str(input())
    if not num.isdigit():
        print("This input can have only numbers. Please Enter Again: ")
        return get_num()
    else:
        return num


print("Enter the start value of face: ")
start_face = int(get_num())
print("Enter the end value of face: ")
end_face = int(get_num())
# to make sure end value is not greater than start value
while end_face < start_face:
    print("End value should not be higher than the start value, enter the end value again")
    end_face = int(get_num())
print("Enter the number of suits: ")
suit_value = int(get_num())
Deck(start_face, end_face, suit_value)
play = NotFreecell()
Deck.shufflelist()
play.display()
while True:
    if play.check_win():
        print("\n\n\n ********************   YOU WIN   ************* \n\n\n")
        exit()
    play.check_move()
    print("\n\n\n\n")
    play.display()
