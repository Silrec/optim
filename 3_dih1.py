def f(x):
    return x**2 - 4*x + 6


a, b = 0, 5
eps = 0.001   # маленькое число (ε)
l = 0.01      # точность

while (b - a) > l:
    y = (a + b - eps) / 2
    z = (a + b + eps) / 2

    if f(y) < f(z):
        b = z
    else:
        a = y

x_min = (a + b) / 2

print("x_min =", x_min)
print("f(x_min) =", f(x_min))