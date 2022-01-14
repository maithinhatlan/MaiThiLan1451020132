def SumNumber(n):
    sum = 0
    itemp = n
    while (n > 0):
        sum = sum + n % 10
        n = int(n / 10)
    print("Sum of digits of", itemp, "is:", sum)
middlenam = input("Enter your middle name: ")
print("Your middle name:", middlenam)
n = int(input("Enter an integer n = "))
SumNumber(n)