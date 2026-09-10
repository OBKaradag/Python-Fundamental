print('-----FONKSİYONLAR-----')
#Python dilinde fonksiyon tanımlamak için 'def' komutu kullanılır.
def topla():
    print(5,"+",7,"=",5+7)
topla()
"""print("---Fonksiyon Çıktıları---")
#RETURN:Bir hesaplamanın sonucunu döndürmek veya belirli verileri almak için kullanışlıdır.
def alan(u,k):
    A=u*k
    return A
def cevre(u,k):
    C=(u+k)*2
    return C
u=int(input("dikdörtgenin uzun kenarını giriniz:"))
k=int(input("dikdörtgenin kısa kenarını giriniz:"))
print('dikdörtgenin alanı:',alan(u,k),"m^2")
print('dikdörtgenin cevresi:',cevre(u,k),"m")"""
#Yerel(Lokal) Değişken:Fonksiyonlarda tanımlanan değişkenler
#Global Değişken:Fonksiyonun dışında veya global kapsamda bildirilen bir değişken
"""def topla():
    global a,b #global a,b yazmamış olsaydık a ve b değişkenini fonksiyon dışında kullanamayacaktık, a ve b değişkeninin bulunamadığı hatasını alacaktık.
    a=5
    b=6
    return (a+b)
print(topla())
print(a)
print(b)"""
#içeriği olmayan fonksiyon üretmek için fonksiyonun içine pass ya da return yazarız.
'''def carpma():
    pass
print(carpma())'''

'''print("fonksiyon kısaltma")
def dolar(TL):
    return (TL/41)
#Yukarıdaki ile aşağıdaki aynı fonksiyonlardır.
dolar=lambda TL: TL/41
miktar=float(input("miktarı giriniz:"))
print(dolar(miktar))'''
#öztekrarlı fonksiyon
"""def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1) #2*2*2*2*1

a=int(input("tabanı giriniz:"))
b=int(input("üssü giriniz:"))
print(ustel(a, b))"""