hafta_gunleri = ["pazar","pazartesi","salı", "carsamba","persembe","cuma","cumartesi"]
gidilen_gun = int(input("hangi gün gidilecek?(0 pazar 6 cumartesı aradan bı sayı sec aslanım):" ))
kalınacak_gun = int(input("kac gun kalacaksın?:" ))
additation = gidilen_gun + kalınacak_gun
donulecek_gun = additation % 7

print(f"sonuc: {hafta_gunleri[donulecek_gun]}")