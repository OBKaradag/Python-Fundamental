#import turtle
#import turtle as tr
from turtle import *

#turtle.setposition(-50,-80)
#turtle.goto(82,36)
#turtle.setpos(56,-65)
#print(turtle.pos())
#turtle.reset()
#turtle.home()
#turtle.done()

'''turtle.forward(100)
turtle.right(90) #turtle.rt
turtle.fd(100)
turtle.right(90)
turtle.backward(50)
turtle.left(45)  #turtle.lt
turtle.bk(50)
turtle.done()'''

"""#KARE ÇİZİMİ
tr.fd(100)
tr.rt(90)
tr.bk(100)
tr.lt(90)
tr.bk(100)
tr.rt(90)
tr.fd(100)"""
#Turtle Simgeleri
"""print(turtle.getshapes()) #Simgelerin ne olduklarını görürüz.
tr.shape('circle')
tr.fd(200)
tr.shape('turtle')
tr.rt(90)
tr.fd(100)
tr.hideturtle()
tr.lt(45)
tr.fd(100)
tr.showturtle()
print(tr.pos())
tr.done()"""
#KARE ÇİZİMİ V.2
"""def kareCizim(mesafe): #Kare çizim fonksiyonu
    for a in range(1,5):
        forward(mesafe)
        left(90)

hideturtle()
pensize(5)
x=int(input("kare sayısı gir:"))
x+=1
for a in range(x):
    kareCizim(50*a)
done()"""
#ÜÇGEN ÇİZİMİ
"""def ucgenCizimi(mesafe):
    for a in range(1,4):
        fd(mesafe)
        rt(120)

hideturtle()
pensize(2)
x=int(input("Kaç tane ü.gen olsun? = "))
x+=1
for a in range(x):
    ucgenCizimi(50*a)
exitonclick()"""

#RENK KOMUTLARI
"""colormode(255)
color(0,0,0)
def ucgenCizimi():
    for a in range(3):
        fd(200)
        lt(120)

def kare():
    for a in range(4):
        fd(200)
        right(90)

pensize(5)
begin_fill()
fillcolor(165,42,42) #Kahverengi sayısal karşılığı
ucgenCizimi()
end_fill()

begin_fill()
fillcolor(128,128,128) #Gri sayısal karşılığı
kare()
end_fill()
done()"""

#DAİRE ÇİZİMİ
"""circle(100)"""
    #JAPON BAYRAĞI
"""pensize(12)
shape('blank')
for x in range(2):
    forward(150)
    right(90)
    forward(100)
    right(90)
pencolor('red')
penup()
goto(75,-80)
pendown()
fillcolor('red')
begin_fill()
circle(30)
end_fill()
done()"""
   #TRAFİK LAMBASI
"""pensize(12)
shape('blank')
for x in range(2):
    forward(100)
    right(90)
    forward(250)
    right(90)

pencolor('red')
penup()
goto(50,-80)
pendown()
fillcolor('red')
begin_fill()
circle(30)
end_fill()

pencolor('yellow')
penup()
goto(50,-155)
pendown()
fillcolor('yellow')
begin_fill()
circle(30)
end_fill()

pencolor('green')
penup()
goto(50,-230)
pendown()
fillcolor('green')
begin_fill()
circle(30)
end_fill()

done()"""

#ÇOKGENLER
"""N=int(input("köşe sayısını girin..:"))
aci=360/N
pensize(3)
for x in range(N):
    forward(50)
    left(aci)
done()"""
"""pensize(4)
circle(100,360,7) #yedigen
done()"""

#Veri girişi için iletişim
"""N=int(numinput("poligon","kenar sayısı",5))
renk=textinput("renk","iç rengi")
pensize(4)
begin_fill()
fillcolor(renk,)
circle(100,360,N)
end_fill()
exitonclick()"""
#ÇERÇEVE İÇİNE RESİM KOYMAK
"""setup(512,512)
bgpic("Icon_Bird_512x512.gif")
title("KUŞ")
done()"""
#TÜRK BYARAĞI
"""pensize(4)
title("Türk Bayrağı")
setup(600,400)
bgcolor("red")
def renkKonum(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()
def yildiz():
    renkKonum("white",80,25)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()
def hilal(cap):
    circle(cap)
    end_fill()
renkKonum("white",-110,-120)
hilal(130)
renkKonum("red",-70,-90)
hilal(100)

yildiz()
mainloop()"""