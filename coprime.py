def coprime(a,b):
    for i in range(2, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            return "aralarinda asal degil"
    else:
        return "aralarinda asal"
print(coprime(27,9))
