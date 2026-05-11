# функция
def f(x):
    return x**2 - 4*x + 6


a, b = 0, 5
eps = 0.01

# числа Фибоначчи
fib = [1, 1]
while fib[-1] < (b - a) / eps:
    fib.append(fib[-1] + fib[-2])

n = len(fib)

# начальные точки
y = a + fib[n-3] / fib[n-1] * (b - a)
z = a + fib[n-2] / fib[n-1] * (b - a)

for k in range(n - 2):
    if f(y) <= f(z):
        b = z
        z = y
        y = a + fib[n-k-3] / fib[n-k-1] * (b - a)
    else:
        a = y
        y = z
        z = a + fib[n-k-2] / fib[n-k-1] * (b - a)

# результат
x_min = (a + b) / 2

print("x_min =", x_min)
print("f(x_min) =", f(x_min))