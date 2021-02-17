def fibon(n):
    n1 = 0
    n2 = 1
    for i in range(0, n+1):
        num = i
        if i > 1:
            num = n1 + n2
            # new values
            n1 = n2
            n2 = num
        print(num)



print("Fibonacci Sequence: ", fibon(20))