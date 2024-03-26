import turtle

def get_coor(x, y):
    print(f"{x}, {y}")

screen = turtle.Screen()
screen.setup(width=1400,height=760)
screen.addshape('image.gif')
turtle.shape('image.gif')


turtle.onscreenclick(get_coor)
screen.mainloop()