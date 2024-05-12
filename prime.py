'''def prime(a):
    if a == 2:
        return "bu sayi asaldir"
    if a == 1:
        return "bu sayi asal degildir"
    for i in range(2,a):
        if a % i == 0:
            return "bu sayi asal degildir"
        else:
            return "bu sayi asaldir"
print(prime(15)) '''



def prime(a):
    if a == 2:
        return "asaldir"
    if a < 2 or a % 2 == 0:
        return "asal degildir"
    for i in range(3, a, 2):
        if a % i == 0:
            return "asal degildir"
        else:
            return "asaldir"
print(prime(29))
