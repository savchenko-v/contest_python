# put your python code here
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if (x1 == х2 and у1 != у2) or (x1 != х2 and у1 == у2) or abs(x1 - х2) == abs(у1 - у2):
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')