import random

class Card():
	def __init__(self, faceNum, suitNum):
		self.faceNum = faceNum
		self.suitNum = suitNum

	def getCardName(self):
		nameSuit = ['H', 'S', 'T', 'L']
		nameFace = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
		return "%s%s" % (nameSuit[self.suitNum], nameFace[self.faceNum])

# make the deck
def Make_Deck():
	deck = []
	shuffle = []
	for suitNum in range(4):
		for faceNum in range(13):
			newCard = Card(faceNum, suitNum)
			deck.append(newCard)
	# shuffle the cards
	for card in deck:
		shuffle.append(card.getCardName())
	random.shuffle(shuffle)
	# return a shuffled deck
	return shuffle

# draw a card and put it in our hand
def Draw_Card(deck, hand):
	draw = deck[0]
	hand.append(draw)
	deck.remove(draw)

# if the last card and the 4th last card have the same suit we take out the cards between them
def Remove_All(hand):
		for i in range(-4, -0):
			hand.remove(hand[i])

# if the last card and the 4th last card have the face we remove all 4 cards
def Remove_Two(hand):
		for i in range(-3, -1):
			hand.remove(hand[i])

# take the last card we have in our hand and put it first
def Last_First(hand):
	return hand[1:] + hand[:1]

# function that checks what to do with the cards we have
# in our hand each time after we draw a new card
# and calles relevent functions
def Check_Loop(hand):
	if len(hand) >= 4:
		if hand[-4][1:3]==hand[-1][1:3]:
			Remove_All(hand)
		elif hand[-4][:1]==hand[-1][:1]:
			Remove_Two(hand)
			if len(hand) >= 4:
				if hand[-4][1:3]==hand[-1][1:3]:
					Remove_All(hand)

# function that check what we can do when we have drawn all cards
# from the deck and calls relevent functions
# tells us if we lose ore win
def Check_Final(hand):
	if len(hand)==2 or len(hand)==0:
		#print 'jei'
		print 'kapallinn gekk upp, thu att ' + str(len(hand)) + ' spil eftir'
	elif len(hand)==3 or len(hand)==1:
		print 'kapallinn gekk ekki upp, thu att ' + str(len(hand)) + ' spil eftir'
	else:
		hand = Last_First(hand) # setjum sidasta stakid fyrst
		print hand
		if hand[-4][1:3]==hand[-1][1:3]: # er seinasta og fjorda seinasta sama typa
			Remove_All(hand)
			Check_Final(hand)
		elif hand[-4][:1]==hand[-1][:1]: # er seinasta og fjorda seinasta sami typa
			Remove_Two(hand)
			Check_Final(hand)
		else:
			print 'kapallinn gekk ekki upp, thu att ' + str(len(hand)) + ' spil eftir'



