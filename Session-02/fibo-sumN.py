def fibo_sum(n):
    n1 = 0
    n2 = 1
    fibonacci_list = [n1, n2]
    for i in range(0, n-1):
        num = n1 + n2
        fibonacci_list.append(num)

        # new values
        n1 = n2
        n2 = num

    res = 0
    for i in fibonacci_list:
        res += i
    return res


print("Sum of the First 5 terms of the Fibonacci series: ", fibo_sum(5))
print("Sum of the First 5 terms of the Fibonacci series: ", fibo_sum(10))
