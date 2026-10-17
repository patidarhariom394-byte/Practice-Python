class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def display(self):
    print("This is ", self.name, "my age is ", self.age)

a=student("HARI", 20)
a.display()

b=student("Kris", 18)
b.display()