class Player:
  def __init__(self):
    self.hand = []
    self.points = 0
    self.complete = False
    self.score = 0
  
  def take_from_deck(self, d):
    c = d.remove_card()
    self.hand.append(c)
    self.points += c.val

  def take_from_pile(self, p):
    c = p.remove_card()
    self.hand.append(c)
    self.points += c.val
  
  def throw_card(self, c, p):
    self.hand.remove(c)
    self.points -= c.val
    p.add_card(c)
  
  def is_complete(self):    
    done = False
    # Write checking code to determine whether hand is complete
    self.complete = done

