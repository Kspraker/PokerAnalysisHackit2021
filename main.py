card = {
    'value' : 0,
    'suit' : ' '
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

community = list()

suits = [0, 1, 2, 3]
# Hearts, Diamonds, Club, Spade 
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

#river.append(Card("heart", "2"))


card = {
    'value' : 0,
    'suit' : ' '
}

deckSize = 52

inPlay = [Card(13, 1), Card(12, 1), Card(11, 1), Card(10, 1), Card(2, 1), Card(1, 1)]
sortedSuits = inPlay
flushList = list()


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
    sortSuits()

    this = checkRoyalFlush()
    print(this)

    #playAgain = input("Do you want to play again? ")
def sortCards():
    inPlay.sort(key = lambda x: x.value, reverse = True)

def sortSuits():
    sorted = list()
    sortedSuits.sort(key = lambda x: x.suit, reverse = True)

def checkCurrentBestHand():
    print("This Function evaluates what the current best hand is based on the current river and your cards\n")

def checkRoyalFlush():
    print("This Function evaluates if the current hand is a royal flush based on the current river and your cards\n")
    count = 1
    ace = 1
    card = 13
    if checkFlush() == True:
        
        for j in sortedSuits:
            print(j.value)
        for i in range(len(sortedSuits)-2):
            if sortedSuits[i].value != card:
                return False
            card =  card - 1

        if sortedSuits[len(sortedSuits)-1].value != ace:
            return False

    else:
        return False

    return True

def checkStraightFlush():
    print("This Function evaluates if the current hand is a straight flush based on the current river and your cards\n")
    # might be error with something, i forgot what i typed
    count = 1
    if checkFlush() == True:
        flushList.sort(key = lambda x: x.value, reverse = True)
        for i in range(len(flushList)-1):
            if flushList[i].value - 1 != flushList[i+1]:
                count = count + 1

    else:
        return False
    
    if count == 5:
        return True
    
    else:
        return False

def checkFourOfAKind():
    print("This Function evaluates if the current hand is a four of a kind based on the current river and your cards\n")

    total = 0
    for i in range(len(inPlay)-1):
        if inPlay[i].value == inPlay[i+1].value:
            total += 1
        else:
            total = 0
        if total == 3:
            print("You have four of a kind of: " + str(inPlay[i].value) + "'s")
            break

def checkFullHouse():
    print("This Function evaluates if the current hand is a full house based on the current river and your cards\n")

    total = 0
    firstPair = -1
    for i in range(len(inPlay)-1):
        if inPlay[i].value == inPlay[i+1].value:
            total += 1
        else:
            total = 0
        if total == 2:
            firstPair = inPlay[i].value
            removed = inPlay
            del removed[i]
            if (i+1) < len(inPlay):
                del removed[i+1]
            else:
                del removed[i-1]
            break

    print(total)

    if (firstPair != -1):
        for j in range(len(removed)):
            if (removed[j+1].value != None) and (removed[j].value == removed[j+1].value):
                print("You have three of a kind of: " + str(firstPair) + "'s")
                print("You have a pair of: " + str(removed[j].value) + "'s")
                break

def checkFlush():
    print("This Function evaluates if the current hand is a flush based on the current river and your cards\n")
    total = 1
    end = len(sortedSuits)-1
    
    for i in range(len(sortedSuits)-1):
        if total == 4:

            for j in range(5):
                flushList.append(sortedSuits[end-j])

            # for j in flushList:
            #     print(j.suit)

            return True

        if sortedSuits[i].suit == sortedSuits[i+1].suit:
            total = total + 1
        else:
            total = 1

    return False
    # if total == 4:
    #     return True
    
    # else:
    #     return False

def checkStraight():
    # Remember to make case for ace, since it can begin and end
    print("This function evaluates if the player has a straight\n")
    flag = True
    count = 1

    for i in range(len(inPlay)-1):
        if(inPlay[i+1] != None):
            if inPlay[i].value - 1 == inPlay[i+1].value:
                count = count + 1

            else:
                count = 0

    print(count)






def checkThree():
    print("This function evaluates if the player has three of a kind\n")
    total = 0
 
    # probably messed up the indexing here, not starting at 0
    # current = inPlay[0].value
    for i in range(len(inPlay)-1):
        if total == 2:
            break
        if inPlay[i].value == inPlay[i+1].value:
            total = total + 1
        else:
            total = 0

    print(total)



def checkTwoPair():
    print("This function evaluates if the player has two pairs\n")

    firstPair = -1
    for i in range(len(inPlay)):
        if (inPlay[i+1].value != None) and (inPlay[i].value == inPlay[i+1].value):
            firstPair = inPlay[i].value
            removed = inPlay
            del removed[i]
            break

    if (firstPair != -1):
        for j in range(len(removed)):
            if (removed[j+1].value != None) and (removed[j].value == removed[j+1].value):
                print("You have a pair of: " + str(firstPair) + "'s")
                print("You have a pair of: " + str(removed[j].value) + "'s")
                break

def checkPair():
    print("This function evaluates if the player has one pair\n")

    for i in range(len(inPlay)):
        if (inPlay[i+1].value != None) and (inPlay[i].value == inPlay[i+1].value):
            print("You have a pair of: " + str(inPlay[i].value) + "'s")
            break

def checkHighCard():
    print("This function evaluates if the player only has high card\n")
    highest = inPlay[0]

    for i in inPlay:
        if i.value > highest.value:
            highest = i

    print("Your highest card is " + i)



main()