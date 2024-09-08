import math
from tkinter import *
from random import *

window = Tk()
window.geometry("500x500")
window.title("Genetics")

canvas = Canvas(window, width=500, height=500, bg="#012")
canvas.pack()

genome = [
    {
        'length': 100,
        'size': randint(15, 25),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0, 255),
        'green': randint(0, 255),
        'blue': randint(0, 255),
        'red shift': uniform(-3,3),
        'green shift': uniform(-3, 3),
        'blue shift': uniform(-3, 3),
    },  # 1 level
    {
        'length': 70,
        'size': randint(12, 22),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0, 255),
        'green': randint(0, 255),
        'blue': randint(0, 255),
        'red shift': uniform(-3, 3),
        'green shift': uniform(-3, 3),
        'blue shift': uniform(-3, 3),
    },  # 2 level

    {
        'length': 50,
        'size': randint(10, 20),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0, 255),
        'green': randint(0, 255),
        'blue': randint(0, 255),
        'red shift': uniform(-3, 3),
        'green shift': uniform(-3, 3),
        'blue shift': uniform(-3, 3),
    },  # 3 level

    {
        'length': 40,
        'size': randint(10, 20),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0, 255),
        'green': randint(0, 255),
        'blue': randint(0, 255),
        'red shift': uniform(-3, 3),
        'green shift': uniform(-3, 3),
        'blue shift': uniform(-3, 3),
    },  # 4 level
    #
    # {   'length': 35,
    #     'size': randint(7,16),
    #     'size shift': uniform(-0.3, 0.3)
    # },   # 5 level
    #
    # {   'length': 30,
    #     'size': randint(6,14),
    #     'size shift': uniform(-0.3, 0.3)
    # },   # 6 level

]


def rgb(r, g, b):
    r = abs(math.floor(min(max(r,0),255)))
    g = abs(math.floor(min(max(g,0),255)))
    b = abs(math.floor(min(max(b,0),255)))
    return f'#{r:02x}{g:02x}{b:02x}'


def circle(centerx, centery, radius, color):
    shift = max(abs(radius), 3)/2
    startx = centerx - shift
    starty = centery - shift
    endx = centerx + shift
    endy = centery + shift
    canvas.create_oval(startx, starty, endx, endy, fill=color, width=0)


def rad_calc(angle):
    return (angle - 90) * math.pi / 180


def branch(startx, starty, angle, genome_line):
    nextx = startx
    nexty = starty
    radius = genome_line['size']
    red = genome_line['red']
    green = genome_line['green']
    blue = genome_line['blue']
    for step in range(genome_line['length']):
        nextx += math.cos(rad_calc(angle))
        nexty += math.sin(rad_calc(angle))
        radius += genome_line['size shift']
        red += genome_line['red shift']
        green += genome_line['green shift']
        blue += genome_line['blue shift']
        color = rgb(red, green, blue)
        circle(nextx, nexty, radius, color)

    save = {
        'endx': nextx,
        'endy': nexty,
        'angle': angle,
    }
    return save


def tree(startx, starty, angle, genome, depth=0):
    if depth == len(genome):
        return
    save = branch(startx, starty, angle, genome[depth])
    endx = save['endx']
    endy = save['endy']
    angle = save['angle']
    tree(endx, endy, angle-30, genome, depth+1)
    tree(endx, endy, angle+30, genome, depth+1)


tree(250, 450, 0, genome)


window.mainloop()
