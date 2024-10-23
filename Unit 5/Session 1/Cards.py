class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def print_card(self):
	    print(f"{self.rank} of {self.suit}")
		


spade8 = Card('Spades', 8)
card = Card("Clubs", 'Ace')
card.print_card()
