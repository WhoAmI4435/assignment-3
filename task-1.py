a = int(input("enter number: "))
if a < 0:
    print("factorial of", a, "is not defined")
elif a>-1:
    s = 1
    for i in range(1, a+1):
        s = s*i
    print("factorial of", a, "is", s)

