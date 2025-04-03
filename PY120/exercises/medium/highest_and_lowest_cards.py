class Card:
    RANK = {
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14
    }
    
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    @property 
    def value(self):
        return self.RANK.get(self.rank, self.rank) #look for the rank in RANK, if not exist (aka its 2-10), use the int)
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def __gt__(self, other):
        return self.value > other.value
        
    def __lt__(self, other):
        return self.value < other.value
        
    def __eq__(self, other):
        return self.value == other.value

# class Deck:
#     RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
#     SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
#     def __init__(self):
#         self._deck = None
#         self.construct()
#         self.
        
#     def construct(self):
#         for rank in self.RANKS:
#             for suit in self.SUITS:
#                 self._deck.append((rank, suit))
                
#     def draw(self):
        