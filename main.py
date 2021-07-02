def addTwoLast(lis):  # Adding two last elements of the list to each other and adding to the end of list
    len(lis)
    lis.append(lis[len(lis) - 1] + lis[len(lis) - 2])
    return lis


def fibo(num):  # Main Fibonacci function
    if num == 1:
        x = [0]
        return x
    if num >= 2:
        i = 3
        x = [0, 1]
        if num == 2:
            return x
        else:
            while i <= num:
                x = addTwoLast(x)
                i += 1
        return x


uNum = int(input("Give me number to generate Fibonacci: "))
print(fibo(uNum))
