"""
Types of numbers in Python

1) int : All the integers
2) float : All the decimal numbers
3) complex : Integer with letter 'j'
"""

x = 1
y = 5.25
z = 9j

print(type(x))
print(type(y))
print(type(z))

#Converting number type

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

j=10
g=20

#Addition
sum=(j+g)
print(sum)

#Substraction
sub=(j-g)
print(sub)

#Multiplication
mul=(j*g)
print(mul)

#division
div=(j/g)
print(div)

#Modulous
mod=(j%g)
print(mod)

#Power
P=(j**g)
print(P)

#Floor Division (division then round to the closest smaller integer)
fd=(j//g)
print(fd)


