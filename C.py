"""
Требуется определить, является ли данный год високосным. (Год является високосным, если его номер кратен 4,
 но не кратен 100, а также если он кратен 400).

 На вход подается натуральное число N - номер года (0 < N < 100000).
 Вывести YES если год високосный и NO в противном случае.
"""

year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('YES')
elif year % 400 == 0:
    print('YES')
else:
    print('NO')
