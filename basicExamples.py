#örnek2
''' x = input("adınızı girin: ")
print("hay", x) '''

#ornek3
'''x = int(input("birinci sayiyi girin: "))
y = int(input("ikinvi sayiyi girin: "))
sonuc = (x + y) / 2
print(sonuc) '''

#ornek4
''' vize = float(input("vize notunuzu girin: "))
final = float(input("final notunuzu girin: "))
sonuc = (vize*0.4) + (final*0.6)
print("yıl sonu ortalamanız: ", sonuc) '''

#ornek5
''' yazili1 = float(input("birinci yazilinizi girin: "))
yazili2 = float(input("ikinci yazilinizi girin: "))
yazili3= float(input("ucuncu yazilinizi girin: "))
ortalama = (yazili1 + yazili2 + yazili3) / 3
print("ortalamaniz", ortalama) '''

#ornek6
'''' vize = float(input("vize notunuzu girin: "))
final = float(input("final notunuzu girin: "))
ortalama = (vize*0.4) + (final*0.6)
print("yıl sonu ortalamanız: ", ortalama)
if ortalama >= 60:
    print("gectiniz")
else:
    print("kaldiniz") '''

#ornek7
''' x = int(input("bir sayi giriniz: "))
if x % 2 == 0:
    print("sayi cift")
else:
    print("sayi tektir") '''

#ornek8
''' x = int(input("bir sayi giriniz: "))
if x == 0:
    print("sayiniz 0")
elif x > 0:
    print("sayiniz pozitif")
else:
    print("sayiniz negatif") '''

#ornek9
''' boy = float(input("boyunuzu giriniz(m): "))
kilo = float(input("kilonuzu giriniz: "))
VKI = kilo / (boy*boy)
if 18 < VKI < 25:
    print("normal")
elif 25 < VKI < 30:
    print("kilolu")
elif 30 <= VKI:
    print("obez")
elif 35 <= 35:
    print("ciddi obez") '''

#ornek10
''' yas = int(input("yasınızı giriniz: "))
if yas >= 18:
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alamazsiniz") '''

#ornek11
''' for i in range(1,101):
    if i % 2 == 0:
        print(i) '''

#ornek12
''' adet = int(input("sayi girin: "))
for i in range(1, adet + 1):
    print(i) '''

#ornek13
''' kisa_kenar = float(input("kisa kenar uzunlugu: "))
uzun_kenar = float(input("uzun kenar uzunlugu: "))
cevre = 2 * (kisa_kenar + uzun_kenar)
alan = kisa_kenar * uzun_kenar
print("cevre: {} ve alan: {}".format(cevre, alan)) '''

#ornek14
''' isim = input("isim giriniz: ")
for i in isim:
    print(i) '''

#ornek15
''' x = int(input("ilk sayi: "))
y = int(input("ikinci sayi: "))
total = 0
for i in range(x, y + 1):
    total += i
print("{} ile {} arasindaki sayilarin toplami {}".format(x, y, total)) '''

#ornek16
'''first_num = int(input("ilk sayi: "))
second_num = int(input("ikinci sayi: "))
if first_num > second_num:
    min_num = second_num
else:
    min_num = first_num
for i in range(min_num, 1, -1):
    if first_num % i == 0 and second_num % i == 0:
        print(first_num, "ile", second_num, "sayisini bolen en buyuk sayi", i)
        break
else:
    print("ortak bolenleri yok") '''

#ornek17
''' num = int(input("sıfırdan buyuk bir sayı giriniz: "))
totalodd = 0
totaleven = 0
if num < 0:
    print("sıfırdan buyuk sayı girmelisiniz")

else:
    for i in range(1, num, 2):
        totalodd += i
    print("tek sayilarin toplami", totalodd)
    for i in range(0, num, 2):
        totaleven += i
    print("çift sayilarin toplami", totaleven) '''


''' a = [1,2,3]
b = a


print(a==b)
print(a is b) '''

''' def fonksiyonum():
    sayi = 20
    print("fonksiyonun ici", sayi)

sayi = 10
print("fonksiyon oncesi", sayi)
fonksiyonum()
print("fonksiyon sonrasi", sayi) '''

#ornek18
''' def polindrom():
    x = int(input("bir sayi girin:"))
    if x ==int(str(x)[::-1]):
        print("this is polindrom number")
    else:
        print("this is not polindrom number")
polindrom() '''


#eger fonkisyona girdigin iki sayinin bolen sayisi esitse bunlar friends sayi.

''' def friends_number():
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    num_1_sayac = 0
    num_2_sayac = 0
    for bolen in range(1, num_1 + 1):
        if (num_1 % bolen) == 0:
            num_1_sayac += 1
    for bolen in range(1, num_2 + 1):
        if (num_2 % bolen) == 0:
            num_2_sayac += 1
    if num_1_sayac == num_2_sayac:
        print("they are friends number")
    else:
        print("they are not friends number")

friends_number() '''

#x = "1.34,2.47,3.46,5.87"

#verilen sayilar string. bunlari bi sekil listeye al toplaminni bul.

x = "1.2, 2.4, 3.4, 5.8"
list_x = x.split(",") #["1.34", "2.47", "3.46", "5.87"]
x_float = []
total = 0
for each_number in list_x:
    x_float.append(float(each_number))
for sum in x_float:
    total += sum

print(total)

    
