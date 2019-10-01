from sys import exit
from random import randint
import random
from turtle import *
import turtle

#done imports

def fib_sq(n):
    ap.fd(n)
    ap.pu()
    ap.fd(3)
    ap.pd()
    ap.fd(int(n//2))
    ap.color('green')
    ap.write('a')
    ap.color('red')
    ap.fd(int(n/2))
    ap.pu()
    ap.lt(90)
    ap.fd(3)
    ap.lt(90)
    ap.fd(n)
    ap.pd()

    ap.rt(90)
    ap.fd(n)
    ap.pu()
    ap.lt(90)
    ap.fd(3)
    ap.lt(90)
    ap.pd()
    ap.fd(int(n//2))
    ap.color('green')
    ap.write('b')
    ap.color('red')
    ap.fd(int(n/2))
    ap.pu()
    ap.lt(90)
    ap.fd(3)
    ap.lt(90)
    ap.fd(n)
    ap.pd()

    ap.rt(90)
    ap.fd(n)
    ap.rt(90)
    ap.fd(n)  
        
        
        
        


def fibon(n=100):
    a,b =1,1
    fl = [1]
    sl = []
    grl = []
    grls = []
    try:
        for i in range(n-1):
            fl.append(b)
            grl.append(b/a)
            a,b = b,a+b
    except ZeroDivisionError:
        pass

    ap.pu()
    ap.goto(-400,-290)
    ap.pd()
    ap.color('red')
    ap.write("corresponding fibrobonnaci sequence starting with 1 as follows (upto 40 terms): \n")
    
    for i in range(40):
        sl.append(fl[i])
    ap.pu()
    ap.goto(-400,-292)
    ap.pd()
    ap.write(sl,"\n")
    

    for j in range(40):
        grls.append(grl[j])

        
    ap.pu()
    ap.goto(-400,-298)
    ap.pd()
    ap.write("also see ratio upto 40 terms..\n")
    ap.pu()
    ap.goto(-400,-306)
    ap.pd()
    ap.write(grls,"\n")
    ap.pu()
    ap.goto(-400,-320)
    ap.pd()
    ap.write("Ratios appears to tend 1.618 and it is found almost everywhere in nature..")
    
    
    print("The golden ratio list is as follows for 100 samplespace :")
    print(grl)
    
    print("\n")
    print("As you can see the above list ..after 12 number(11th index)")
    print("and the list is special because tends to attain the value 1.618")
    print("It coincides with the Golden Ratio(researchers calls it god's ratio)..")
    print("The same number(1.618) is represented by symbol 'phi' of mathematics")
    print("The name phi is kept on the name of a mathematician 'phidias'")
    print("Because it is found almost everywhere in nature..in structure of universe,")
    print("in human fingerprint,dna of a living being, in ancient historic monuments(collaseum,etc),")
    print("In flower structure,almost everywhere..This is yet Another proof of,")
    print("also, it is said that if our ratios of face structures tends to coincide with god's ratio,")
    print("then our faces tends to looks perfect and exact 1.618 attains perfect structure..")
    print("How powerful is mathematics and how god used mathematics to create cosmos..")
    print("The Significance of this ratio also proves uniqueness of GOD.")
    print("\n")
    

    
    print("\n")
    print("do you want to see the full fibronacci list upto 1000?\n(caution:it consumes more memory and takes some time..")
    print("Y/N or type exit to exit from application")
    get = input(str('Y/N'))
    if (get == "Y" or get == 'y'):
          fibon()
          print("thats it..")
    elif(get == "N" or get == 'n'):
        print('Thank you for usig this app..please provide me feedback if,\n you see any bug in the application i will corrrect that.')
        print("Would you like to start again? Y/N")
        ch = input(str())
        if (ch == "Y" or ch == 'y'):
              fibon()
        elif(ch == "N" or ch =="n"):
              print("OK BYE BYE..SEE YOU AGAIN")
              exit()
    elif(get == "exit" or get == "EXIT" or get == "Exit"):
        exit(0)
    return fl,grl
screen = Screen()
screen.tracer(0)
screensize(1.5)
ap = Turtle()
title("GOLDEN RATIO - ANIMATION EXPLAINATION BY ANAND PRABHAKAR")
ap.pensize(1.5)
ap.color('red')
tracer(5)
ap.pu()
ap.goto(150,150)
ap.pd()
ap.color('red')
ap.write("a:b here represents 1.618 i.e phi")  

ap.pu()
goto(0,0)
ap.pd()
color('blue')
pensize(1)
tracer(2)
speed(8)
drange = 13
for z in range(0,4):
    e = 0
    i = 1
    g = 0
      
    for y in range(0, 4):
        e = 0
        i = 1
        g = 0
        
        for x in range(0, drange):
            circle(i, 90)
            g = e + i
            e = i
            i = g
        goto(0, 0)
        right(80)


ap.goto(0,0)
z,x =1,1
li= [1]
for i in range(13):
    li.append(x)
    z,x = x,z+x
    
ap.pu()
ap.goto(-300,330)
ap.color('green')
ap.pd()
ap.write(li)
ap.goto(0,0)
for i in li:
    fib_sq(i)
    
        
fibon()

done()



