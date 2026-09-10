"""print("---İNDEX---")
isim="Ömer Burak Karadağ"
print(isim[3]) #Bize isim değişkeninin 3. indisini verir.
print(isim[-1])  #Bize isim değişkeninin -1. indisini verir."""

'''print("---STRİNG BİRLEŞTİRME---")
A="Ömer"
B="Burak"
print(A+B,A,B)'''

"""print("---STRİNG BÖLME---")
C="PYTHON"
print(C[3:]) #C değişkenindeki ilk 3 indisi ayır.
print(C[:3]) #C değişkenindeki son 3 indisi ayır.
print(C[1:5]) #C değişkenindeki 1. ile 5. indis arasındaki karakterleri gösterir.
print(C[1::2]) #1.İndis'ten başla ikişer ikişer atlayarak karakterleri yazdır.
print(C[1:6:3]) #1.İndis'ten başlayarak 6.indis'e kadar üçer üçer atlayarak karakterleri yazdır.
print(C[::-1]) #C değişkenini tersten yazdırır.
C2=C[:3]+'T'+C[4:] #C değişkenindeki H'yi T ile değiştirdik.
print(C2)"""

'''print("---STRİNG DEĞİŞTİRME---")
#1.YÖNTEM
Adres="Pendik-İstanbul"
Adres2='Kadıköy'+Adres[6:]
print(Adres2)
#2.YÖNTEM
print(Adres.replace("Pendik","Kadıköy"))'''

""""print("---STRİNG SİLME---")
yazi="Python"
print(yazi)
for x in range(1,6):
    print(yazi[:-x])"""

'''print('---STRİNGE FOR DÖNGÜSÜ İLE ERİŞİM---')
a=''
s=0
indis=int(input("indis değerini giriniz:"))
for d in "ömerburak":
    if s==indis:
        a=d
    s+=1
print(a)'''

"""print("---STRİNGİ LİSTEYE DÖNÜŞTÜRME---")
cumle='seni_çok_seviyorum'
print(cumle.split('_'))
adres="DerebahçeMah,BahçeSok,Kafkas Cad,BahçekentSit"
print(adres.split(','))
notlar="78 90 88 46 67"
print(notlar.split())"""

"""print('---STRİNG UZUNLUĞU BULMA---')
cumle="selamlar, nasılsınız?"
print(len(cumle))
print(cumle.count("a")) #Count=Saymak"""

'''print("---STRİNG KARŞILAŞTIRMA---")
#1.YÖNTEM
print("ömer"=="ömer")
#2.YÖNTEMLER
print("ömer" is "ömer")
print("ömer" is not "ömer")
print("ömer" is "burak")
print("ömer" is not "burak")'''

"""print("---STRİNGİ TERS ÇEVİRME---")
#1.YÖNTEM
str1="ZAMAN"
str2=(str1[::-1])
print(str2)
#2.YÖNTEM
print(".".join(reversed(str2)))"""

"""print("---BÜYÜK KÜÇÜK HARF---")
a="SOFTware"
print(a.lower())
print(a.upper())
print(a[0::2].lower())
print(a.swapcase()) #Büyük yazılan karakterleri küçük, küçük yazılan karakterleri büyük yazdırdı.
b="yazılım"
print(b.capitalize()) #Baş harfi büyük yazdırdı"""

"""print("---STRİNG İÇERİSİNDE BAŞKA STRİNG ARAMA---")"""
'''print("er" in "ömer")
print("ER" in "ömer")
print("şişe" not in "su şişesi")
print("suluk" not in "su şişesi")'''
"""str1=input("isimleri gir:")
str2=input("ismin nedir?:")
if str2 in str1:
    print("hoşgeldin",str2,"!")
else:
    print(str2,"bulunamadı...")"""

'''print("---ÖRNEK---")
str1=input("1.kelime:")
if str1==str1[::-1]:
    print("kelime palindromdur,",str1,"nin tersi",str1[::-1],"dir.")
else:
    print("kelime palindrom değildir,",str1,"nin tersi",str1[::-1],"dir.")'''