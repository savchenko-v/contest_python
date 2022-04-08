L = []
while True:
    n = int(input())
    if n != 0:
        L.append(n)
    else:
        break
print(sum(L))
