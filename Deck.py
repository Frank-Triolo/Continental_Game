class Deck:
  def __init__(self):
    self.cards = []

  def add_card(self, card_input):
    self.cards.append(card_input)
  
  def remove_card(self):
    return self.cards.pop(0)
