def palindrome(s):
  if s==s[::-1]:
    print("Palindrome")
  else:
    print("Not palindrome")


palindrome("madam")
palindrome("skd")


def table(a):
  for i in range(1,11):
    print(a, "X", i, "=", a*i)

table(2)

a=5
for i in range(1,11):
  print(a, "X", i, "=", a*i)
