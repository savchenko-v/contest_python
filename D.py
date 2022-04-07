n = int(input())
i = 1
a = 0
while a <= n:
    a = i**2
    print(a)
    if (i+1)**2 <= n:
        i += 1
    else:
        break
