def sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

print("Sum of the 20 first integers: ", sum(20))
print("Sum of the 100 first integers: ", sum(100))