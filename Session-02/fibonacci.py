n1 = 0
n2 = 1
fibonacci_list = [n1, n2]
for i in range(0, 11-len(fibonacci_list)):
    num = n1 + n2
    fibonacci_list.append(num)

    # new values
    n1 = n2
    n2 = num

# print list
for i in fibonacci_list:
    print(i, end=" ")
