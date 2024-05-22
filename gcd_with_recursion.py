def ebob(m, n):
    if m % n == 0:
        return n
    else:
        return ebob(n, m % n)
print(ebob(24, 10))