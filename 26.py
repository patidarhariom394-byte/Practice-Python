a="123@"
Password=input("Enter the password-- ")
i=1

while i<=3:
  Password=input("Enter the password")

  if Password==a:
    print("Login successful")
    break
  else:
    i+=1
    print("Try again")

    

if i==3:
  print("Blocked")

