def fak():
    x = int(input("hangi sayinin faktoriyeli alinsin: "))
    sonuc = 1
    while x >= 0:
        for i in range(1, x + 1):
            if x == 0 or x==1:
                return 1
            else:
                sonuc *= i
        return sonuc
print(fak())

