n = int(input("Введите количество чисел > "))

def print_numbers(n: int):
    if n == 0:
        return ""
    line = input("Введите число > ")
    return print_numbers(n - 1) + line + " "

print(print_numbers(n).strip())
 