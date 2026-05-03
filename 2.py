def f(x):
    return 2*x**2 + 5*x + 2.5


x0 = 0      # начальная точка
t = 0.5     # шаг

# шаг 1
f0 = f(x0)
f_minus = f(x0 - t)
f_plus = f(x0 + t)

# проверка
if f_minus >= f0 <= f_plus:
    a, b = x0 - t, x0 + t

elif f_minus <= f0 >= f_plus:
    print("Функция не унимодальная")
    exit()

else:
    # определяем направление
    if f_plus < f0:
        delta = t
        x_prev = x0
        x_curr = x0 + t
    else:
        delta = -t
        x_prev = x0
        x_curr = x0 - t

    k = 1

    while True:
        x_next = x_curr + (2**k) * delta

        if f(x_next) < f(x_curr):
            x_prev = x_curr
            x_curr = x_next
            k += 1
        else:
            if delta > 0:
                a, b = x_prev, x_next
            else:
                a, b = x_next, x_prev
            break

print("Интервал с минимумом:", [a, b])