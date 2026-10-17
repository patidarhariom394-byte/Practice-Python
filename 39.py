class grandp:
  def Grand(self):
    print("Hey i am gp")

class parent(grandp):
  def father(self):
    print("I am father")

class child(parent):
  def son(self):
    print("I am son")

c=child()
c.Grand()
c.father()
c.son()