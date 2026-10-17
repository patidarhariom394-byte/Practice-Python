number=int(input("Enter the number--"))

if (number%3==0):
  print("Only divisible by 3")

elif(number%7==0):
  print("Only divisible by 7")
  
elif (number%3==0 and number%7==0):
  print("Divisible by 3 and 7")

else:
  print("Not Divisible")