# Python program to find the largest number among the three input numbers

a = float(input("inter the first number: "))
b = float(input("inter the second number: "))
c = float(input("inter the third number: "))

if(a>=b) and (b>=c):
    largest = a
elif(b>=a) and (b>=c):
    largest = b
else:
    largest = c

print("the largest number is", largest)