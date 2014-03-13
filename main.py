from spilastokkur import *

deck = Make_Deck()
hand = []

while len(deck) >= 1:
	Draw_Card(deck, hand)
	print hand
	Check_Loop(hand)

Check_Loop(hand)

if not deck:
	Check_Final(hand)

