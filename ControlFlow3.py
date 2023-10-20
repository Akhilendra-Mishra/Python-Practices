
# Write a program which prints all the divisors of a number.

num = int(input("Enter number: "))

for i in range(1, num):
    if num % i == 0:
        print(i)