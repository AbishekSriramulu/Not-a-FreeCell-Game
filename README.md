# Not-a-FreeCell-Game
FreeCell kind of game
@@ -0,0 +1,68 @@
NOT FREECELL DOCUMENTATION

Class Card:
This class contain two class variables 
�	card_suit - A list holding the suits (�S� ? spade, �H� ? Hearts, �C� ? Clubs, �D� ? Diamond)
The suits are placed in the list in a fashion that the red coloured suits are in the even index and odd index positions hold black colour suits.
�	card_face � A list containing the face values of the cards.
Card.face_add method:
If the user requires face values is greater than 13, this method appends new face values into the list Card.card_face.
Card.suit_add method:
If the user wants more than 4 suits, this method appends new suits into the list Card.card_suit.

Class Deck:
This class contains 5 class variables
�	deck_cards - An empty list for storing all the cards created for the game.
�	deck - A empty list of 12 empty lists (8 lists to store the cards in a random manner and 4 extra empty lists for the game).
�	start_face - For storing the start value of the face entered by the user.
�	end_face -  For storing the end value of the face entered by the user.
�	total_suits � For storing the total number of suits entered by the user.
Constructor:
If the start value of the face entered by the user is greater than 13, Card.face_add method is called
If the suits required is more than 4, Card.suit_add method is called
Algorithm for creating the deck
1. for loop1:  for �suits� in range (0 to total number of suits required)
2.	For loop2 inside for loop1: for �face� in range (start value of face to end value of face entered   										 by the user)
3.		Create a string by concatenating the value of Card.card_face[index= face - 1] and									 Card.card_suit[index= suits]
Example: card_suit = ['S', 'H', 'C', 'D']									   card_face = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']					   The suits variable holds the values of range 0 to total number of suits incremented by 1 for	    each loop. So if suits = 0, Card.card_suit[index = 0] returns the value �S� and if face = 2 the 	    Card.card_face[index = 2 - 1] will return the value ��2� which will get concatenated and	     appended to the list as �2S�
4. The list Deck.deck_cards is appended with a string containing the face and suit values


Shufflelist method:
This is a static method as it does not require an object to be created to call this method.
This method shuffles the Deck.deck_cards list and slices it in a random manner appends each slice into the first 8 sub-lists of the list Deck.deck 

Class NotFreecell:
NotFreecell.check_suits:
This method checks whether the sources and target deck�s last cards are of opposite colours (As we stored suits of colour red in even and suits of colour black in odd index positions respectively, we can guess the colour of the suit by finding the index card�s suit in the list Card.card_suit)
If the cards are of different colours, NotFreecell.check_face method is called.
NotFreecell.check_face:
This method checks whether the target card�s face value is one step higher than the source card�s face value
NotFreecell.check_move:
This method gets the inputs for source and target values from the user by calling the NotFreecell.get_input method and stores them in source and target variables respectively and checks whether the move is possible by calling the NotFreecell.check_suits method (NotFreecell.check_suits method will call the NotFreecell.check_face method). If the move it possible, NotFreecell.nove method is called
NotFreecell.check_win:
This method checks whether the game is won or not by making the following checks
1. Total number of suits is equal to total number of non-empty sublists in                                Deck.deck, if yes move to check 2.
2. Check if the first and last face values in each non-empty sublist are equal to the starting and ending face values entered by the user, if yes move to check 3.
3. Compare each element in the sublist with the next element and make sure they are of opposite colors and have face value one step higher than the next element�s face value. (This is done by calling the NotFreecell.check_suits method)
NotFreecell.display:
This method displays the decks with labels (labels ? deck numbers)
NotFreecell.move:
This method deletes the card from the source deck and appends it into the target deck
NotFreecell.get_input:
This method gets input and makes sure that the user provides proper input (Should accept only numbers between 0 to 11)




get_num Function:
This method gets input and makes sure that the input provided by the user is a number
Main Function:
The variables start_face, end_face and suit_value holds the user inputs for start value of face, end value for the face and total number of suits respectively with which the Class Deck constructor is called (object is created).
Play ? object variable for the class NotFreecell
Deck.shufflelist method is called to shuffle the list and the created Deck.deck is displayed on the screen by calling the display method from the NotFreecell class
A while loop which ends only when the game is won holds
1. Method call for check_win method in NotFreecell class. If the method returns True, the screen prints You won and exits the program
2. The method check_move is called from class NotFreecell, to get the inputs for the game 
3. The output after the move is made is displayed by calling the display method from NotFreecell class
