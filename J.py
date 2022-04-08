L = []
while True:
    n = int(input())
    if n != 0:
        L.append(n)
    else:
        break
maxx = max(L)
count = 0
for i in range(len(L)):
    if L[i] == maxx:
        count += 1
print(count)
