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

inPlay = [Card(11, 1), Card(10, 1), Card(9, 1), Card(8, 1), Card(7, 0)]
sortedSuits = inPlay

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

    print(FlushChance())


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
    #if checkIfFlush()
    #    return true
    print('1')

def checkStraightFlush():
    # if checkIfStraight() and checkIfFlush()
    #     return true
    print('1')

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
    
    for i in range(len(sortedSuits)-1):
        if total == 5:
            break
        if sortedSuits[i].suit == sortedSuits[i+1].suit:
            total = total + 1
        else:
            total = 1

    print(total)

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