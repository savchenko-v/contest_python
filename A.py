"""Дано трехзначное число. Найдите сумму его цифр."""

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100

print(a + b + c)
