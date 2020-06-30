class Card:
  def __init__(self, name, suit):
    self.name = name
    self.suit = suit
    if int(name) <= 10:
      self.val = int(name)
    elif name == "King" or name == "Queen" or name == "Jack":
      self.val = 10
    else:
      self.val = 15
