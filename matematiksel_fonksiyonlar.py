#MATH
"""print(abs(-15)) #sayının mutlak değerini alır.
print(max(23,25,27,30,35))
print((bin(66))) #sayıyı binary'e çeviriyor.
print((hex(66))) #sayıyı hexadecimal'e çeviriyor.
print((chr(66))) #sayıyı aski'e çeviriyor.
print(sum((45,45,26,23,54,156,848))) #içindeki değerleri toplar.
print(pow(4,3)) #4 ün 3. kuvveti yani 4 üzeri 3
print(math.sqrt(64)) # içindeki sayının karekökünü alır
print(math.gcd(81,27)) #EBOB"""
import random

#Örnek1-Küre
'''import math
r=int(input("yarıçapı metre cinsinden gir...:"))
Hacim=4/3*math.pi*pow(r,3)
Alan=4*math.pi*pow(r,2)
print("Kürenin Hacmi = ",Hacim,"m^3 dür.")
print("Kürenin Yüzey Alanı = ",Alan,"m^2 dir.")'''

#RANDOM
"""import random
print(random.random()) #0 ile 1 arasında rastgele float değerler üretir.
print(random.randint(1,15)) #1 ile 15 arasında rastgele int değerler üretir.
print(random.randrange(1,13,2))#1 ile 13 arasında 2 şer atlayarak sayı üretir.
print(random.uniform(1,20))#1 ile 20 arasında rastgele float değerler üretir.
Liste=[1,2,3,4,5,6,7,'a','b','c']
print(random.choice(Liste))#listeden rastgele seçim yapar.
(random.shuffle(Liste))#listedeki öğelerin sırasını rastgele değiştirir.
print(Liste)
print(random.sample(Liste,2))#Listeden rastgele 2 tane eleman seçti."""

"""#Örnek2-Rastgele
import random
tahmin=int(input("1 ile 10 arasında bir sayı giriniz..:"))
sayi=(random.randint(1,10))
skor=3
while sayi!=tahmin:
    print("Yanlış tekrar dene!!! Skorunuz:",skor)
    skor-=1
    tahmin = int(input("1 ile 10 arasında bir sayı giriniz..:"))
if sayi==tahmin:
    print("Tebrikler Kazandınız!!! Skornuz:",skor)"""

#TAŞ-KAĞIT-MAKAS
"""import random
Liste=['Taş','Kağıt','Makas']
pc=random.choice(Liste)
player=input(Liste).capitalize()

print("Bilgisayar",pc,"seçti")
print("Sen",player,"seçtin")

if pc==player:
    print("Durum Berabere")
if pc=='Taş' and player=='Kağıt':
    print("Tebrikler Kazandınız")
if pc=='Taş' and player=='Makas':
    print("Maalesef Kaybettiniz")
if pc=='Kağıt' and player=='Taş':
    print("Maalesef Kaybettiniz")
if pc=='Kağıt' and player=='Makas':
    print("Tebrikler Kazandınız")
if pc=='Makas' and player=='Kağıt':
    print("Maalesef Kaybettiniz")
if pc=='Makas' and player=='Taş':
    print("Tebrikler Kazandınız")
else:
    print("Hatalı Girdi!!!")"""
