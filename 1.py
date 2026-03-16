def f_x(a, b, c, x):
    return a*(x**2) + b*x + c

def one(a, b, c):
    # 2*a*x + b = 0
    x = ((-1)*b)/(2*a)
    y = f_x(a, b, c, x)
    extr = '?'
    if x > 0:
        extr = 'min'
    elif x < 0:
        extr = 'max'
    return [x, y, extr]

print(one(1, -4, 6))
