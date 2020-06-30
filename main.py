import random
from random import shuffle
from itertools import combinations
import time

Final = []
for line in open("outfile.txt",'r'):
  Final.append(int(line.strip()))

def list_prod(L):
  p = 1
  for x in L:
    p *= x
  return p

def calculate_done(prod,possible):
  #print(prod)
  ret = False
  if prod == 1:
    print("Valid hand!")
    return True
  for melds in possible:
    if prod%melds == 0:
      ret = calculate_done(prod//melds,possible)
      if ret == True:
        return True
    #print(ret)
  #print("Not Valid Hand")
  return False


class Card:
  def __init__(self, name, suit):
    self.name = str(name)
    self.suit = suit
    self.hidden = 0
    try:
      if int(name) <= 10:
        self.val = int(name)
    except:
      if name == "King" or name == "Queen" or name == "Jack":
        self.val = 10
      elif name == "Joker":
        self.val = 0
      else:
        self.val = 15
  def __str__(self):
    return self.name + " of " + self.suit + ": " + str(self.hidden)
  def set_hidden(self,n):
    self.hidden = int(n)

class Deck:
  def __init__(self):
    self.cards = []

  def add_card(self, card_input):
    self.cards.append(card_input)
  
  def remove_card(self):
    return self.cards.pop(0)

  def clear(self):
    self.cards = []
  
  def __str__(self):
    return str(len(self.cards))

  def shuffle(self):
    shuffle(self.cards)

class Pile:
  def __init__(self):
    self.cards = []
  
  def remove_card(self):
    return self.cards.pop(-1)
  
  def clear(self):
    self.cards = []
  
  def add_card(self,c):
    self.cards.append(c)
  
  def __str__(self):
    return str(self.cards[-1])

class Player:
  def __init__(self):
    self.hand = []
    self.points = 0
    self.complete = False
    self.score = 0
    self.hidden = []
  
  def take_from_deck(self, d):
    c = d.remove_card()
    self.hand.append(c)
    self.points += c.val
    self.hidden.append(c.hidden)

  def take_from_pile(self, p):
    c = p.remove_card()
    self.hand.append(c)
    self.hidden.append(c.hidden)
    self.points += c.val
  
  def throw_rand(self,p):
    c = random.choice(self.hand)
    self.hand.remove(c)
    self.hidden.remove(c.hidden)
    self.points -= c.val
    p.add_card(c)
  
  def throw_card(self, c, p):
    self.hand.remove(c)
    self.hidden.remove(c.hidden)
    self.points -= c.val
    p.add_card(c)

  def throw_by_hidden(self,n,p):
    for c in self.hand:
      print(c.hidden)
      if c.hidden == n:
        self.hand.remove(c)
        self.hidden.remove(c.hidden)
        self.points -= c.val
        p.add_card(c)
        return

  def __len__(self):
    return len(self.hand)
  
  def is_complete(self):    
    all_combos = combinations(self.hidden, 10)

    for combo in all_combos:
      l_p = list_prod(combo)
      print(l_p)
      if calculate_done(l_p,Final) == True:
        return True
    return False
  
  def __str__(self):
    l = []
    for c in self.hand:
      l.append(str(c))
    l.append('\n')
    return '\n'.join(l)

P = [ # Products-To-Be
 [241,"Hearts","Diamonds","Spades","Clubs"],
 [0,41,101,167,239],
 ['2',2,43,103,173],
 ['3',3,47,107,179],
 ['4',5,53,109,181],
 ['5',7,59,113,191],
 ['6',11,	61,	127,	193],
 ['7',13,	67,	131,	197],
 ['8',17,	71,	137,	199], 
 ['9',19,	73,	139,	211],
 ['10',23,	79,	149,	223],
 ['J',29,	83,	151,	227],
 ['Q',31,	89,	157,	229],
 ['K',37,	97,	163,	233],
 ['A',41,	101,	167,	239]
]

Card_Pile = Pile()
Card_Deck = Deck()
P1 = Player()
P2 = Player()

def Make_Round(round_number): 
  for i in range(2):
    All_Vals = list(range(2,11,1))
    All_Vals += ["Jack","Queen","King","Ace"]
    All_Suits = ["Hearts","Diamonds","Spades","Clubs"]
    for val in range(len(All_Vals)):
      for suit in range(len(All_Suits)):
        c = Card(str(All_Vals[val]),All_Suits[suit])
        c.set_hidden(P[val+2][suit+1])
        #print(c)
        Card_Deck.add_card(c)
  Card_Deck.shuffle()

  for i in range(10):
    P1.take_from_deck(Card_Deck)
    P2.take_from_deck(Card_Deck)
    #print(len(P1))
  P1.take_from_deck(Card_Deck)
  P1.throw_rand(Card_Pile)
  '''
  if round_number % 2 == 0:
    P1.take_from_deck(Card_Deck)
  else:
    P2.take_from_deck(Card_Deck)
  '''


def Clear_Round():
  Card_Deck.clear()
  Card_Pile.clear()

t1 = time.time()

round_num = 0
turn = 0

Make_Round(round_num)

done = False

while (not done):
  
  if turn == 0:
    if round_num %2 == 0:
      P1.take_from_deck(Card_Deck)
      print(P1)
      done = P1.is_complete()
      h = int(input("Input hidden to remove: "))
      P1.throw_by_hidden(h,Card_Pile)
      turn += 1
      continue
    else:
      P2.take_from_deck(Card_Deck)
      print(P2)
      done = P2.is_complete()
      P1.throw_rand(Card_Pile)
      turn += 1
      continue
  print()
  ran = random.random()
  if turn%2 == 0:
    print(len(P1))
    print(P1)
    print(Card_Pile)
    take = input("Input Pile (p) or Deck (d): ")
    
    if take.lower() == 'p':
      P1.take_from_pile(Card_Pile)
    else:
      P1.take_from_deck(Card_Deck)
    #which to take from?
    print(len(P1))
    print(P1)
    
    done = P1.is_complete() # This should be done before the throw
    if done == True:
      break

    h = int(input("Input hidden to remove: "))
    P1.throw_by_hidden(h,Card_Pile)

    '''
    if ran > 0.5:
      P1.take_from_deck(Card_Deck)
    else:
      P1.take_from_deck(Card_Pile)
    done = P1.is_complete()
    if done == False:
      P1.throw_rand(Card_Pile)
    '''
  else:
    if ran > 0.5:
      P2.take_from_deck(Card_Deck)
    else:
      P2.take_from_pile(Card_Pile)
    done = P2.is_complete()
    if done == False:
      P2.throw_rand(Card_Pile)

  turn += 1

print(turn)

t2 = time.time()

print(str(t2-t1))

'''
while (P1.score < 100 and P2.score < 100):
  Card_Deck.clear()
  Card_Pile.clear()
  for val in All_Vals:
    for suit in All_Suits:
      c = Card(val,suit)
      Card_Deck.add_card(c)

  while (P1.complete == False and P2.complete == False):
    break
  P1.score += P1.points
'''