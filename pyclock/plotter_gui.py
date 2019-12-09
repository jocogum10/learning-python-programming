# plot circles on a canvas
import math, sys
from tkinter import *

def point(tick, range, radius):
    angle = tick * (360/range)
    radians_per_degree = math.pi/180
    point_x = int(round(radius*math.sin(angle*radians_per_degree)))
    point_y = int(round(radius*math.cos(angle*radians_per_degree)))
    return (point_x, point_y)
    
def circle(points, radius, center_x, center_y, slow=0):
    canvas.delete('lines')
    canvas.delete('points')
    for i in range(points):
        x, y = point(i+1, points, radius-4)
        scaled_x, scaled_y = (x + center_x), (center_y - y)
        canvas.create_line(center_x, center_y, scaled_x, scaled_y, tag='lines')
        canvas.create_rectangle(scaled_x-2, scaled_y-2, scaled_x+2, scaled_y+2, fill='red', tag='points')
        if slow: canvas.update()
        
def plotter():  # 3.x //trunc div
    circle(scale_var.get(), (width // 2), origin_x, origin_y, check_var.get())
    
def makewidgets():
    global canvas, scale_var, check_var
    canvas = Canvas(width=width, height=width)
    canvas.pack(side=TOP)
    scale_var = IntVar()
    check_var = IntVar()
    scale = Scale(label='Points on circle', variable=scale_var, from_=1, to=360)
    scale.pack(side=LEFT)
    Checkbutton(text='Slow mode', variable=check_var).pack(side=LEFT)
    Button(text='Plot', command=plotter).pack(side=LEFT, padx=50)
    
if __name__ == '__main__':
    width = 500                                     # default width, height
    if len(sys.argv) == 2: width = int(sys.argv[1]) # width cmdline args
    origin_x = origin_y = width//2                  # same as circle radius
    makewidgets()
    mainloop()