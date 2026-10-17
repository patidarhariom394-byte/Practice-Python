class father:
  def money(self):
    print("I have money")

class mother:
  def gold(self):
    print("I have gold")

class child(father,mother):
  def son(self):
    print("I have both")

m=child()
m.gold()
m.money()