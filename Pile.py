class Pile:
  def __init__(self):
    self.cards = []
  
  def remove_card(self):
    return self.cards.pop(0)
  def add_card(self, card_input):
    self.cards.insert(0, card_input)
