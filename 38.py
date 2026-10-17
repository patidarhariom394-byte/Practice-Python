class parent:
  def show(self):
    print("this is parent class")

class child(parent):
  def display(self):
    print("This is child class")

c=child()
c.display()
c.show()