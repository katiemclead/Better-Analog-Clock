#modified from:
#https://www.codespeedy.com/how-to-create-analog-clock-in-python/

import tkinter as tk
import turtle

wn = turtle.screensize(300,300)  
#wn.screensize(200,200)
t = turtle.Turtle()
"""window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")
hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()"""



def draw_clock(hr, mn):

    # Draw clock 
    t.penup()
    t.goto(0, 100)
    t.setheading(180)
 
    t.pendown()
    t.circle(100)

    # Draw hour hashes
    t.up()
    t.goto(0, 0)
    t.setheading(90)
    hour = 12

    for _ in range(12):
        t.fd(80)
        t.pendown()
        t.fd(20)
        t.penup()
        t.bk(40)
        t.write(hour,font = ("Calibri", 10, "bold"))
        if hour == 12:
          hour = 1
        else:
          hour = hour + 1
        t.goto(0, 0)
        t.rt(30)

    # Draw the hands
    
    
    #hour hand
    angle = hr * 30 + mn/2
    t.penup()
    t.goto(0, 0)
    t.pensize(10)
    t.setheading(90)
    t.rt(angle)
    t.pendown()
    t.fd(35)
    #t.rt(30)
    #t.bd(20)
    #t.fd(20)
    

    #minute hand
    angle = mn * 6
    t.penup()
    t.goto(0, 0)
    
    t.setheading(90)
    t.rt(angle)
    t.pendown()
    t.pensize(8)
    t.fd(50)

myHour = int(input("Hour: "))
myMinute = int(input("Minute: "))
draw_clock(myHour,myMinute)
t.penup()
t.goto(-200,-230)
