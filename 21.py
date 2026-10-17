num=[1,3,5]

for i in range(1,6):
  if i not in num:
    print(i)

    num.append(i)

print(num)

num.sort()
print(num)

num.sort(reverse = True)
print(num)