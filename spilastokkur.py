import random

class Card():
	def __init__(self, faceNum, suitNum):
		self.faceNum = faceNum
		self.suitNum = suitNum

	def getCardName(self):
		nameSuit = ['H', 'S', 'T', 'L']
		nameFace = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
		return "%s%s" % (nameSuit[self.suitNum], nameFace[self.faceNum])

# buum til stokkinn
def Make_Deck():
	deck = []
	stokk = []
	for suitNum in range(4):
		for faceNum in range(13):
			newCard = Card(faceNum, suitNum)
			deck.append(newCard)
	# stokkum stokkinn
	for card in deck:
		stokk.append(card.getCardName())
	random.shuffle(stokk)
	# skilum stokkudum spilastokk
	return stokk

# drogum spil og setjum i hand
def Draw_Card(deck, hand):
	draw = deck[0]
	hand.append(draw)
	deck.remove(draw)

# ef seinasta spilid og fjorda seinasta spilid eru somu gerdar fjarlaegjum vid thau sem eru a milli
def Remove_All(hand):
		for i in range(-4, -0):
			hand.remove(hand[i])

# ef seinasta spilid og fjorda seinasta spilid eru sama numer fjarlaegjum vid thau oll
def Remove_Two(hand):
		for i in range(-3, -1):
			hand.remove(hand[i])

# faerum seinasta spilid fremst
def Last_First(hand):
	return hand[1:] + hand[:1]

# fall sem skodar thad sem vid erum med a hendi i hvert skipti
# eftir ad vid drogum nytt spil ur stokkinum
def Check_Loop(hand):
	if len(hand) >= 4:
		# ef seinasta spilid og fjorda seinasta spilid eru sama numer fjarlaegjum vid thau oll
		if hand[-4][1:3]==hand[-1][1:3]:
			Remove_All(hand)
		# ef seinasta spilid og fjorda seinasta spilid eru somu gerdar fjarlaegjum vid thau sem eru a milli
		elif hand[-4][:1]==hand[-1][:1]:
			Remove_Two(hand)
			if len(hand) >= 4:
				if hand[-4][1:3]==hand[-1][1:3]:
					Remove_All(hand)

# fall sem skodar thad sem vid erum med a hendi
# thegar stokkurinn okkar er tomur og
# segir okkur hvort kapallinn gangi upp eda ekki
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
	




