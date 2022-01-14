def D(d):
    d = dict()
    for i in range(1, n + 1, 1):
        d[i] = i * i
    print (d)
name = input("Enter your name:")
print("Your name is:", name)
n = int(input("Enter an integer n: "))
print("Dictionary is:")
D(n)