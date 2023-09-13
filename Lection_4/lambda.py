def math(op, x, y):
    print(op(x, y))

def calc (a, b):
    return a * b

math(calc, 5, 5)

# -----------------------------------------

calc1 = lambda a, b: a * b

math(calc1, 4, 4)

# -----------------------------------------

math(lambda a, b: a * b, 3, 4)