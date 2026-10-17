s=input("Enter the ch-- ")
count=0

for ch in s:
  if ch in "aeiouAEIOU":
    count+=1

print("vowels=", count)