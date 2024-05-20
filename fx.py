def f(x):
    xs = str(x)
    if len(xs) == 1:
        return int(xs)
    n = int(xs[0]) + int(xs[1])
    if len(xs) == 2:
        return n
    else:
        return n + f(xs[2:])

print(f(12345))