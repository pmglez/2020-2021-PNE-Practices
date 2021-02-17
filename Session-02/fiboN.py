def fibon(n):
    n1 = 0
    n2 = 1
    fibonacci_list = [n1, n2]
    for i in range(0, (n - 1)):
        num = n1 + n2
        fibonacci_list.append(num)

        # new values
        n1 = n2
        n2 = num

    return fibonacci_list[-1]


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))