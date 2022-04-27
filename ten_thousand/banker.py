class Banker:
  def __init__(self):
    self.balance = 0
    self.shelved = 0

  def shelf(self, points):
    self.shelved += points

  def bank(self):
    self.balance += self.shelved
    self.clear_shelf()

  def clear_shelf(self):
    self.shelved = 0