def fibon(n):
    n1 = 0
    n2 = 1
    fibonacci_list = [n1, n2]
    for i in range(0, n-1):
        num = n1 + n2
        fibonacci_list.append(num)

        # new values
        n1 = n2
        n2 = num

    return fibonacci_list[-1]


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))


def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


print("Sum of the 20 first integers: ", sumn(20))
print("Sum of the 100 first integers: ", sumn(100))