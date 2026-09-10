"""import time
import turtle
from turtle import *"""

#FARE İLE YAZI YAZMA
"""pensize(3)
win=Screen()
win.setup(500,500)
penup()

def nokta(x,y):
    goto(x,y)
    pendown()

win.onclick(nokta)
mainloop()"""

#YÖN TUŞLARI İLE HAREKET
"""shape('turtle')
pensize(4)
win=Screen()
win.setup(500,500)

def solaDon():
    left(90)
    write("Sola döndüm")
def sagaDon():
    right(90)
    write("Sağa döndüm")
def ileriGit():
    forward(10)

def geriGit():
    backward(10)


win.onkeypress(solaDon,'Left')
win.onkeypress(sagaDon,'Right')
win.onkeypress(ileriGit,'Up')
win.onkeypress(geriGit,'Down')

win.listen()
done()"""

#TRAFİK IŞIĞI UYGULAMASI
"""import time as t
w=Screen()
w.setup(300,700)
w.title("Trafik Işık Uygulaması")

penup()
goto(0,180)
pendown()
pensize(4)

for a in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)

def red():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def yellow():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def green():
    penup()
    goto(40,00)
    fillcolor("green")
    shape("circle")
    shapesize(3)


def Durdurma():
    w.bye()  # Ekranı ve programı güvenli bir şekilde kapatır
# Işık döngüsünü yönetecek durum değişkeni ve asıl döngü fonksiyonu
durum = 0


def isik_dongusu():
    global durum
    if durum == 0:
        red()
        durum = 1
        w.ontimer(isik_dongusu, 3000)  # 3000 milisaniye (3 sn) sonra tekrar çalıştır
    elif durum == 1:
        yellow()
        durum = 2
        w.ontimer(isik_dongusu, 1500)  # 1500 milisaniye (1.5 sn) sonra tekrar çalıştır
    elif durum == 2:
        green()
        durum = 0
        w.ontimer(isik_dongusu, 3000)  # 3000 milisaniye (3 sn) sonra tekrar çalıştır
# Klavye dinleme olayları
w.listen()
w.onkeypress(Durdurma, "space")  # Space tuşuna basıldığında Durdurma fonksiyonunu tetikle
# İlk ışığı yakarak döngüyü başlat
isik_dongusu()
# Ekranın kapanmasını engelleyen ve tuş/zamanlayıcı olaylarını dinleyen ana döngü
w.mainloop()"""
#YILAN OYUNU
"""import turtle as tr
import time as t
import random as ran
Liste=[]
skor=0
maxSkor=0

w=tr.Screen()
w.title("Yılan Oyunu")
w.setup(600,600)
w.bgcolor("green")
w.tracer(0)

#Yılan Kafa
yn=tr.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("black")
yn.penup()
yn.goto(0,0)
yn.yon="dur"

def hareket():
    if yn.yon=="ust":
        y=yn.ycor()            #y ekseninde yukarı git
        yn.sety(y+20)
    elif yn.yon=="alt":
        y=yn.ycor()            #y ekseninde aşağı git
        yn.sety(y-20)
    elif yn.yon=="sag":
        x=yn.xcor()            #x ekseninde sağa git
        yn.setx(x+20)
    elif yn.yon=="sol":
        x=yn.xcor()            #x ekseninde sola git
        yn.setx(x-20)

def yukariGit():
    if yn.yon!="alt":
        yn.yon="ust"
def asagiGit():
    if yn.yon!="ust":
        yn.yon="alt"
def sagaGit():
    if yn.yon!="sol":
        yn.yon="sag"
def solaGit():
    if yn.yon!="sag":
        yn.yon="sol"

w.listen()
w.onkeypress(yukariGit,"Up")
w.onkeypress(asagiGit,"Down")
w.onkeypress(sagaGit,"Right")
w.onkeypress(solaGit,"Left")

yem=tr.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("brown")
yem.penup()
yem.goto(0,100)


def ye():
    global skor,maxSkor
    if yn.distance(yem)<20:
        x=ran.randint(-280,+280)
        y=ran.randint(-280,+280)
        yem.goto(x,y)

        kuyruk=tr.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)

        skor+=5
        if skor>maxSkor:
            maxSkor=skor
        w.title("Skor: {}  En yüksek skor: {}".format(skor, maxSkor))


    uzunluk=len(Liste)
    for indis in range(uzunluk-1,0,-1):
        x=Liste[indis-1].xcor()
        y=Liste[indis-1].ycor()
        Liste[indis].goto(x,y)
    if len(Liste)>0:
        x=yn.xcor()
        y=yn.ycor()
        Liste[0].goto(x,y)

def baslangic():
    global skor
    t.sleep(1)
    yn.goto(0,0)
    yn.yon="dur"

    for eklem in Liste:
        eklem.goto(1000,1000)
    Liste.clear()
    skor=0
    w.title("Skor: {}  En yüksek skor: {}".format(skor,maxSkor))

while True:
    w.update()
    ye()
    hareket()
    if yn.xcor()>290 or yn.xcor()<-290 or yn.ycor()>290 or yn.ycor()<-290:
        baslangic()
    for eklem in Liste:
        if eklem.distance(yn)<20:
            baslangic()
    t.sleep(0.1)

w.mainloop()"""