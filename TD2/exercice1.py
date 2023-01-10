class Book:
  def __init__(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price


  def view(self):
    print(f"title : {self.title}, \nauthor : {self.author}, \nprice : {self.price} $")

b1 = Book("The Psychology of Money: Timeless lessons on wealth, greed, and happiness","Morgan Housel",12.2)
b2 = Book("Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones","James Clear",14.11)

print("------------------------------------")
b1.view()
print("------------------------------------")
b2.view()
