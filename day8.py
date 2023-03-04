#  Loops in python

num = [1,2,3,4,5,6,7,89,64,2,34,3,234,6,543,24,43]

for i in num:
    print(i)

print()

fruit = "apple"

for i in fruit:
    print(i)

print()

num = [1,2,3,4,5,89,64,543,24,43]
for i in num:
    print(i)
    if i== 5:
        break

print()

num = [1,2,3,4,5,6,7,89]
for i in num:
    if i== 5:
        continue
    print(i)

print()

for i in range(14):
    print(i)

print()

for i in range(5, 14):
    print(i)

print()

# While loop

r=1
while r<7:
    print(r)
    if r==5:
        break
    r+=1