import json

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

results = {
	'royalFlushChance': 0,
	'straightFlushChance': 0,
	'fourKindChance': 0,
	'fullHouseChance': 0,
	'flushChance': 0,
	'straightChance': 0,
	'threeKindChance': 0,
	'twoPairChance': 0,
	'onePairChance': 0
}

suits = [0, 1, 2, 3]
# Hearts, Diamonds, Club, Spade 
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

deckSize = 52

inPlay = []
sortedSuits = []
flushList = list()

def lambda_handler(event, context):
	
	body = event['body']
	body = json.loads(body)
	
	for i in body:
		print(i)
		stuff = i.split()
		inPlay.append(Card(int(stuff[0]), int(stuff[1])))
		
	sortedSuits = inPlay
	sortCards()
	sortSuits()
	
	checkCurrentBestHand()

	return {
		'statusCode': 200,
		'headers': {
			"Access-Control-Allow-Origin" : "*", # Required for CORS support to work
			"Access-Control-Allow-Credentials" : True # Required for cookies, authorization headers with HTTPS 
		  },
		'body': json.dumps(results)
	}

def sortCards():
	inPlay.sort(key = lambda x: x.value, reverse = True)

def sortSuits():
	sortedSuits.sort(key = lambda x: x.suit, reverse = True)

def checkCurrentBestHand():
	if not checkRoyalFlush():
		results['royalFlushChance'] = RoyalFlushChance()
	
	if not checkStraightFlush():
		results['straightFlushChance'] = StraightFlushChance()
	
	if not checkFourOfAKind():
		results['fourKindChance'] = FourOfAKindChance()

	if not checkFullHouse():
		results['fullHouseChance'] = FullHouseChance()

	if not checkFlush():
		results['flushChance'] = FlushChance()

	if not checkStraight():
		results['straightChance'] = StraightChance()
	
	if not checkThree():
		results['threeKindChance'] = ThreeOfAKindChance()
	
	if not checkTwoPair():
		results['twoPairChance'] = TwoPairChance()

	if not checkPair():
		results['onePairChance'] = PairChance()
	
	checkHighCard()

def checkRoyalFlush():
	print("This Function evaluates if the current hand is a royal flush based on the current river and your cards\n")
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
	count = 1

	removed = inPlay
	for n in range(len(inPlay)-1):
		if ((n+1) < len(inPlay)):
			if inPlay[n].value == inPlay[n+1].value:
				del removed[n]

	for i in range(len(removed)-1):
		if ((i+1) < len(removed)):
			if removed[i].value - 1 == removed[i+1].value:
				count = count + 1
				if count == 5:
					print("You have a straight")
					return True
			else:
				count = 1

	entire = 0
	j = 0
	while True:
		if ((j+1) < len(removed)):
			if j == (len(removed)-1):
				j = 0
			if removed[j].value - 1 == removed[j+1].value:
				count = count + 1
				if count == 5:
					print("You have a straight")
					return True
			else:
				count = 1
			entire += 1
			if entire == (len(removed)*2):
				return False

	return False

def checkThree():
	total = 0
 
	# probably messed up the indexing here, not starting at 0
	# current = inPlay[0].value
	for i in range(len(inPlay)-1):
		if total == 2:
			return True
		if inPlay[i].value == inPlay[i+1].value:
			total = total + 1
		else:
			total = 0

	return False


def checkTwoPair():
	firstPair = -1
	for i in range(len(inPlay)):
		if (i + 1 < len(inPlay)) and (inPlay[i].value == inPlay[i+1].value):
			firstPair = inPlay[i].value
			removed = inPlay
			del removed[i]
			break

	if (firstPair != -1):
		for j in range(len(removed)):
			if (i + 1 < len(inPlay)) and (removed[j].value == removed[j+1].value):
				print("You have a pair of: " + str(firstPair) + "'s and")
				print("you have a pair of: " + str(removed[j].value) + "'s")
				return True
	
	return False

def checkPair():
	for i in range(len(inPlay)):
		if (i + 1 < len(inPlay)) and (inPlay[i].value == inPlay[i+1].value):
			print("You have a pair of: " + str(inPlay[i].value) + "'s")
			return True
	
	return False

	
def checkHighCard():
	print("Your highest card is " + str(inPlay[0].value))


def RoyalFlushChance():
	noDupes = inPlay
	for n in range(len(inPlay)-1):
		if(n+1)<len(inPlay):
			if inPlay[n].value == inPlay[n+1].value:
				del noDupes[n]
	if noDupes[0].value != 13 and noDupes[1] != 12:
		return 0

	elif noDupes[1].value != 12 and noDupes[2] != 11:
		return 0
	
	elif noDupes[2].value != 11 and noDupes[3] != 10:
		return 0

	elif noDupes[0].value != 13 and noDupes[len(noDupes)-1] != 1:
		return 0

	else:
		return ((1/(deckSize - len(inPlay)))*100)
	
	

def StraightFlushChance():
	cardsLeft = 52 - len(inPlay)

	removed = inPlay
	for n in range(len(inPlay)-1):
		if ((n+1) < len(inPlay)):
			if inPlay[n].value == inPlay[n+1].value:
				del removed[n]

	total = 0
	fourKind = -1
	four = list()
	for i in range(len(removed)-1):
		print(total)
		if (removed[i].value - 1) == removed[i+1].value:
			total += 1
		else:
			total = 0
		if total == 3:
			fourKind = removed[i].value
			four.append(removed[i-2])
			four.append(removed[i-1])
			four.append(removed[i])
			four.append(removed[i+1])
			break
	
	if (fourKind != -1):
		for j in range(len(four)-1):
			if four[j].suit != four[j+1].suit:
				return 0
		return ((1/cardsLeft)*100)

	return 0


def FourOfAKindChance():
	count = 1
	for i in range(len(inPlay)-1):
		if count == 3:
			return ((1/(deckSize - len(inPlay)))*100)

		if inPlay[i].value == inPlay[i+1].value:
			count = count + 1

		else:
			count = 1
	
	return 0


def FullHouseChance():
	cardsLeft = 52 - len(inPlay)
	total = 0
 
	# probably messed up the indexing here, not starting at 0
	# current = inPlay[0].value
	threeKind = -1
	for i in range(len(inPlay)-1):
		if total == 2:
			threeKind = inPlay[i].value
			break
		if inPlay[i].value == inPlay[i+1].value:
			total = total + 1
		else:
			total = 0

	if (threeKind != -1):
		handLeft = len(inPlay) - 3
		return (((handLeft * 3)/cardsLeft)*100)


	firstPair = -1
	secondPair = -1
	for i in range(len(inPlay)):
		if (i + 1 < len(inPlay)) and (inPlay[i].value == inPlay[i+1].value):
			firstPair = inPlay[i].value
			removed = inPlay
			del removed[i]
			break

	if (firstPair != -1):
		for j in range(len(removed)):
			if (i + 1 < len(inPlay)) and (removed[j].value == removed[j+1].value):
				#print("You have a pair of: " + str(firstPair) + "'s and")
				#print("you have a pair of: " + str(removed[j].value) + "'s")
				secondPair = removed[j].value
				break

	if (secondPair != -1):
		return ((4/cardsLeft)*100)

	return 0

def FlushChance():
	#print("Chance of getting a flush next turn - ", end="")

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
	count = 1

	removed = inPlay
	for n in range(len(inPlay)-1):
		if ((n+1) < len(inPlay)):
			if inPlay[n].value == inPlay[n+1].value:
				del removed[n]

	for i in range(len(removed)-1):
		if((i+1) < len(removed)):
			if removed[i].value - 1 == removed[i+1].value:
				count = count + 1
				if (count == 4):
					break
			else:
				count = 1

	# four cards in a row
	cardsLeft = 52 - len(removed)
	if (count == 4):
		return ((4/cardsLeft)*100)

	count = 1
	# four total cards
	for i in range(len(removed)-1):
		if((i+1 < len(removed))):
			if removed[i].value - 1 == removed[i+1].value:
				count = count + 1
			else:
				count = 1
		if (count == 3):
			threeRow = removed[i].value

			if (((i-2) >= 0) and ((threeRow + 3) == removed[i-2].value)) and (((i+2) < len(removed)) and ((threeRow - 3) == removed[i+2].value)):
				return (((4/cardsLeft) * (4/cardsLeft))*100)
			elif (((i-2) >= 0) and ((threeRow + 3) == removed[i-2].value)) or (((i+2) < len(removed)) and ((threeRow - 3) == removed[i+2].value)):
				return ((4/cardsLeft)*100)
		elif ((i+2) < len(removed)) and (count == 2) and ((removed[i+1].value - 1) != removed[i+2].value):
			if ((removed[i+2].value - 1) == removed[i+3].value):
				return ((4/cardsLeft)*100)
			
	return 0

		

def ThreeOfAKindChance():
	cardsLeft = 52 - len(inPlay)

	numerator = 2

    if checkPair == False:
        return 0
    else:
        ((numerator/cardsLeft)*100)

def TwoPairChance():
	cardsLeft = 52 - len(inPlay)

	numerator = 3 * (len(inPlay) - 2)

    if checkPair == False:
        return 0
    else:
        return ((numerator/cardsLeft)*100)

def PairChance():
	cardsLeft = 52 - len(inPlay)

	numerator = 3 * len(inPlay)

	return ((numerator/cardsLeft)*100)