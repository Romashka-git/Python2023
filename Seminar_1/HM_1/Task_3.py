# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# n = 385916 -> yes
# n = 123456 -> no

n = 123456

n1 = n // 1000
n2 = n % 1000

sum1 = 0
delit1 = 0
i1 = 3
while i1 > 0:
    delit1 = n1 % 10
    sum1 = sum1 + delit1
    n1 = n1 // 10
    i1 = i1 - 1

sum2 = 0
delit2 = 0
i2 = 3
while i2 > 0:
    delit2 = n2 % 10
    sum2 = sum2 + delit2
    n2 = n2 // 10
    i2 = i2 - 1


if sum1 == sum2:
    print('yes')
else:
    print('no')
