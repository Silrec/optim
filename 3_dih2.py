def f(x):
    return 2*x**2 + 5*x + 2.5

def df(x):
    return 4*x + 5


x = -3      # начальная точка (из интервала)
alpha = 0.1 # шаг
eps = 0.01  # точность

for _ in range(100):
    grad = df(x)

    if abs(grad) < eps:
        break

    x = x - alpha * grad

print("x_min =", x)
print("f(x_min) =", f(x))