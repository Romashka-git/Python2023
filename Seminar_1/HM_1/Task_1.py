n = None
n = 123
sum = 0
delit = 0
i = 3
while i > 0:
    delit = n % 10
    sum = sum + delit
    n = n // 10
    i = i - 1
# Введите ваше решение ниже

res = sum
print(res)