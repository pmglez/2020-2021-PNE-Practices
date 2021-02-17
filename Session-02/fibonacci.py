n1 = 0
n2 = 1
for i in range(0, 11):
    num = i
    if i > 1:
        num = n1 + n2
        # new values
        n1 = n2
        n2 = num
    print(num, end=" ")
