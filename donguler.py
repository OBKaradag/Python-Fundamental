print("----DÖNGÜLER----")
#FOR = Döngü sayısı önceden bellidir.
#WHİLE = Döngü sayısı belli olmayıp koşula bağlıdır.
"""liste=["ömer",'burak',"karadağ"]
print(liste)
print(type(liste))
liste2=[23,30,45]
print(liste2)
liste3="python"
print(liste3)"""
#İN , NOT İN = Liste içerisinde bir elemanın olup olmadığını denetlemek için in , not in kullanılır.
#Çıktımız bool (true,false) tipindedir.
'''print("ömer" in liste)
print(33 in liste2)
print('t' not in liste3)
print('t' in liste3) '''
#masaNO=0
"""REZlist=["ömer","mert","serdar","mehmet","salih"]
YRNlist=["mustafa","abdullah","emre"]
isim=str(input("isminiz nedir?..."))
if isim=="ömer":
    masaNO=7
if isim=="mert":
    masaNO=9
if isim=="serdar":
    masaNO=5
if isim=="mehmet":
    masaNO=3
if isim=="salih":
    masaNO=11
if isim in REZlist:
    print("Rezervasyonunuz var.",masaNO,"numaralı masa")
elif isim in YRNlist:
    print("Rezervasyonunuz yarın.")
elif isim not in REZlist and isim not in YRNlist:
    print("Rezervasyonunuz yok.")"""
"""print("RANGE KOMUTU")"""
#RANGE komutu istenen aralıkta sayı dizisi oluşturmak için kullanılır aynı zamanda FOR döngü yapısında tekrar sayısını belirtmek için kullanılır.
"""print(range(0,5)) #=0,1,2,3,4
print(range(6)) #=0,1,2,3,4,5
print(range(1, 10, 2)) #=1,3,5,7,9
print(range(15, 3, -4)) #=15,11,7"""
"""for a in range(0,5):
    print(a)"""
"""for b in range(1, 11, 2):
    print(b)"""
'''for c in range(15, 2, -3):
    print(c)'''
'''print(list(range(0,3)))'''
""""print("FOR DÖNGÜSÜ")"""
'''for a in range(1,30,2):
    print(a)'''
"""for a in range(1,30):
    if (a%2==1):
        print(a)"""
"""print("WHİLE DÖNGÜSÜ")
A=1
print("çıkış için sıfıra bas")
while (A!=0):
    A=(int(input("sayıyı giriniz:")))
    if A==0:
        break
    print('sayının karesi=',A*A)
print("güle güle")"""
'''klncadi="omerburakkrdg"
kullaniciadi=0
while (klncadi!=kullaniciadi):
    kullaniciadi=str(input("kullanıcı adını giriniz:"))
    if klncadi!=kullaniciadi:
        print("yanlış, tekrar deneyiniz.")
print("Hoş geldiniz...")'''
"""print("BREAK KOMUTU")
print('çıkmak için 0 a basınız')
while True: #Sonsuz döngü
    D=int(input("Bir sayı girin:"))
    print("karesi=",D*D)
    if (D==0):
        break #Döngüden çık
print("Döngüden çıktınız.")"""
"""print("CONTİNUE KOMUTU")
#Sadece 7 ve 7'nin katlarını yazdıralım.
for A in range(100):
    if (A%7!=0):
        continue #parantez içini umursamadan devam etmemizi sağladı.
    print(A)"""
'''#İç içe döngüler
#Çarpım Tablosu
for A in range(1,11):
     for B in range(1,11):
         print(A,"*",B,"=",A*B)
     print("\n")'''
