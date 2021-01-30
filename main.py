card = {
    'value' : 0,
    'suit' : ' '
}

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

community = list()

colors = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

deck = [Card(value, color) for value in range(1, 14) for color in colors]

#river.append(Card("heart", "2"))


card = {
    'value' : 0,
    'suit' : ' '
}

deckSize = 52

inPlay = [Card(2, 'Hearts'), Card(3, 'Diamonds'), Card(11, 'Clubs')]

def main():
    print("Hello, this is program a Texas Holdem Game Analysis\n")
    
    #for i in deck:
        #print(i.value)

    # for i in range(3):
    #     cardVal = input("What is the value of the first card on the river? ")
    #     suit = input("What is the suit for the first card on the river? ")
    #     community.append(Card(cardVal, suit))
    
   
    
    #checkHighCard()
    sortCards()


    #playAgain = input("Do you want to play again? ")
def sortCards():
    sorted = list()
    inPlay.sort(key = lambda x: x.value, reverse = True)


def checkCurrentBestHand():
    print("This Function evaluates what the current best hand is based on the current river and your cards\n")

def checkIfRoyalFlush():
    print("This Function evaluates if the current hand is a royal flush based on the current river and your cards\n")

def checkIfStraightFlush():
    print("This Function evaluates if the current hand is a straight flush based on the current river and your cards\n")

def checkIfFourOfAKind():
    print("This Function evaluates if the current hand is a four of a kind based on the current river and your cards\n")

def checkIfFullHouse():
    print("This Function evaluates if the current hand is a full house based on the current river and your cards\n")

def checkIfFlush():
    print("This Function evaluates if the current hand is a flush based on the current river and your cards\n")

def checkStraight():
    print("This function evaluates if the player has a straight\n")

def checkThree():
    print("This function evaluates if the player has three of a kind\n")

def checkTwoPair():
    print("This function evaluates if the player has two pairs\n")

def checkPair():
    print("This function evaluates if the player has one pair\n")

def checkHighCard():
    print("This function evaluates if the player only has high card\n")
    highest = inPlay[0]

    for i in inPlay:
        if i.value > highest.value:
            highest = i

    print("Your highest card is " + i)



main()