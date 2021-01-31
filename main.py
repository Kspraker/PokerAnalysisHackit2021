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
    checkRoyalFlush()
    checkStraightFlush()
    checkFourOfAKind()
    checkFullHouse()
    checkFlush()
    checkStraight()
    checkThree()
    checkTwoPair()
    checkPair()
    checkHighCard()

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
    total = 0
    for i in range(len(inPlay)-1):
        if inPlay[i].value == inPlay[i+1].value:
            total += 1
        else:
            total = 0
        if total == 3:
            print("You have four of a kind of: " + str(inPlay[i].value) + "'s")
            return True

    return False

def checkFullHouse():
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

    if (firstPair != -1):
        for j in range(len(removed)):
            if (removed[j+1].value != None) and (removed[j].value == removed[j+1].value):
                print("You have three of a kind of: " + str(firstPair) + "'s and")
                print("you have a pair of: " + str(removed[j].value) + "'s")
                return True

    return False

def checkFlush():
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
                print("You have a pair of: " + str(firstPair) + "'s and")
                print("you have a pair of: " + str(removed[j].value) + "'s")
                break

def checkPair():
    for i in range(len(inPlay)):
        if (inPlay[i+1].value != None) and (inPlay[i].value == inPlay[i+1].value):
            print("You have a pair of: " + str(inPlay[i].value) + "'s")
            break

    

def checkHighCard():
    print("Your highest card is " + inPlay[0])





def RoyalFlushChance():
    print("1")

def StraightFlushChance():
    print("1")

def FourOfAKindChance():
    print("1")

def FullHouseChance():
    print("1")

def FlushChance():
    print("Chance of getting a flush next turn - ", end="")

    hearts = 0
    diams = 0
    clubs = 0
    spades = 0
    for i in range(0, len(sortedSuits)):
        if sortedSuits[i].suit == 0:
            hearts += 1
        elif sortedSuits[i].suit == 1:
            diams += 1
        elif sortedSuits[i].suit == 1:
            clubs += 1
        else:
            spades += 1
    
    if hearts == 4 or diams == 4 or clubs == 4 or spades == 4:
        return 100 * round((9 / (52 - len(inPlay))), 4)
        
    else:
        return 0

def StraightChance():
    print("1")

def ThreeOfAKindChance():
    print("1")

def TwoPairChance():
    print("1")

def PairChance():
    print("1")

main()