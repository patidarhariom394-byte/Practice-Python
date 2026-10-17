inventory = {
"Laptop": 1008,
"Mouse": 50,
"keyboard": 150,
"Monitor": 2000
}

def calculate_total(items):
  total=0

  for item in items:
   if item in inventory:
    total+=inventory[item]

  else:
    print("Sorry we don't have", item)




  print("Total amount=", total)

cust1_items=['Laptop','Mouse','Monitor']
calculate_total(cust1_items)

