card = {
    'value' : 0,
    'suit' : ' '
}

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

river = list()

river.append(Card("heart", "2"))



deckSize = 52

def main():
    print("Hello, this is program a Texas Analysis\n")
    print(card['value'])
    

    for i in range(3):
        cardVal = input("What is the value of the first card on the river? ")
        suit = input("What is the suit for the first card on the river? ")
    



    playAgain = input("Do you want to play again? ")

    print(deckSize)

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

main()
