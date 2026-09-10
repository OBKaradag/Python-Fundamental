'''a=3
b=3.14
c='ömer'
d=[1,2,3,'burak']
e={'bir':1,'iki':2,'üç':3,'pazartesi':'haftanın birinci günü'}
f={1,2,3,3,5,'a'}
g=(1,2,3,'b')
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))'''


"""def a():
    pass

class araba:
    pass

class hayvan(cins) :
    tur=cins
    def metot(self):
        self.cins="balıklar" """

"""class hayvan:
    pass
class araba:
    pass
At=hayvan()
Horoz=hayvan()

SUV=araba()
Kamyon=araba()"""

"""class Araba():
    def __init__(self,model,marka,renk): #METOT
        self.model=model
        self.marka=marka
        self.renk=renk
    def aracbilgisi(self):
        print("marka:",self.marka)
        print("model:",self.model)
        print("renk:",self.renk)

Taksi=Araba(2020,"FİAT","YEŞİL")

'''print(Taksi.model,Taksi.marka,Taksi.renk)
Taksi.model=2013
print(Taksi.model)'''
print("\n Taksi  bilgisi:")
print(Taksi.aracbilgisi())

Kamyon=Araba(2010,"MAN","Kırmızı")
print("\n Kamyon  bilgisi:")
print(Kamyon.aracbilgisi())

#print(dir(Taksi))

a=3
print(type(a))
print(type(Taksi))"""

"""------KALITIM-----"""
#Üst sınıfa ait olan özelliklerin altsınıflara miraz olarak aktarılması özelliğidir.
#Böylece alt sınıf üst sınıfın özelliklerini taşır.
"""import datetime
a=465364

class araba:
    def __init__(self,model,fiyat,renk):
        self.model=model
        self.fiyat=fiyat
        self.renk = renk
    def arabaBilgi(self):
        print("Araba Modeli:",self.model,"\n","Araba Fiyatı:",self.fiyat,"TL","\n","Araba Renk:",self.renk)
        return(datetime.datetime.now(),a)

class kamyon(araba):
    def __init__(self,model,fiyat,renk):
        '''self.model = model
        self.fiyat = fiyat'''
        araba.__init__(self,model,fiyat,renk)
        self.renk=renk

k1=kamyon(2020,220000,"mavi")
print(k1.arabaBilgi())"""

"""-----MODÜL-----"""
#İMPORT ŞEKİLLERİ

"""-----Bölüm Sonu örnekleri"""
#POW = pow (power) fonksiyonu, bir sayının üssünü almak için kullanılır.
# Temel olarak x üzeri y matematiksel işlemini gerçekleştirir.
"""from math import *

class kup:
    def __init__(self,a):
        self.a=a

    def yuzALAN(self):
        return (6*pow(self.a,2))

    def Hacim(self):
        return (pow(self.a,3))
class kure:
    def __init__(self,r):
        self.r=r

    def yuzALAN(self):
        return ("yuzey alanı..:",4*pi*pow(self.r,2),"cm^2 dir")

    def Hacim(self):
        return ((4/3)*pi*pow(self.r,3))

class silindir:
    def __init__(self,r,h):
        self.r = r
        self.h = h

    def yuzALAN(self):
        return (2*pi*self.r(self.r+self.h))

    def Hacim(self):
        return (pi*pow(self.r,2)*self.h)

futbolTopu=kure(10)
pinponTopu=kure(3)

kupSeker=kup(2)
koli=kup(50)

merdane=silindir(3,50)
matara=silindir(12,15)

print(silindir.Hacim(merdane))
print(kure.yuzALAN(pinponTopu))
print(kup.Hacim(koli))"""
