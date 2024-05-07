def square_root(n):
    global iterasyon
    tahmin = n - ((1 + n) / 2)
    orta_deger = (((n + 1) / 2) + n) / 2
    iterasyon = 0

    while iterasyon < 999:
        if tahmin > 0:
            orta_deger = (((n + 1) / 2) + n) / 2
            tahmin = n - (orta_deger**2)
            iterasyon += 1
        else:
            orta_deger = (((n + 1) / 2) + 1) / 2
            tahmin = n - (orta_deger**2)
            iterasyon += 1
    return tahmin
result = square_root(10)
print(result)
print(iterasyon)
