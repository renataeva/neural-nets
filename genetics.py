import math
from tkinter import *
from random import *

window = Tk()
window.geometry("500x500")
window.title("Genetics")

canvas = Canvas(window, width=500, height=500, bg="#012")
canvas.pack()


def circle(centerx, centery, radius):
    shift = radius / 2
    startx = centerx - shift
    starty = centery - shift
    endx = centerx + shift
    endy = centery + shift
    canvas.create_oval(startx, starty, endx, endy, fill="red", width=0)


def rad_calc(angle):
    return (angle - 90) * math.pi / 180

def branch(startx, starty, angle, lenght):
    nextx = startx
    nexty = starty
    for step in range(lenght):
        nextx += math.cos(rad_calc(angle))
        nexty += math.sin(rad_calc(angle))
        circle(nextx, nexty, 2)

    save = {
        'endx': nextx,
        'endy': nexty,
        'angle': angle,
    }
    return save

def tree(startx, starty, angle, length, depth):
    if depth == 0: return
    save = branch(startx, starty, angle, length)
    endx = save["endx"]
    endy = save["endy"]
    angle = save["angle"]
    tree(endx, endy, angle - 30, length - 14, depth - 1)
    tree(endx, endy, angle + 30, length - 14, depth - 1)
    tree(endx, endy, angle, length - 14, depth - 1)

tree(250,450,0,100, 3)


window.mainloop()
