def reversiblenumber(n):
    number_1 = str(n)    
    number_2 = number_1[::-1] 
    if (number_1 == number_2):
        print(n, "It is reversible number")
    else:
        print(n, "It isn't reversible number")
name = input("Enter your name: ")
print("Your fullname is:", name)
n = int(input("Enter an integer n: "))
reversiblenumber(n)