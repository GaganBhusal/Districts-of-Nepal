import turtle
import pandas

my_data = pandas.read_csv('new_data.csv')
my_districts = list(my_data.d)
my_x_coors = list(my_data.x)
my_y_coors = list(my_data.y)


tommy = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1400,height=760)

screen.addshape('image.gif')
tommy.shape('image.gif')

a = 0
running = True
what_to_do = screen.textinput("What do you wanna do?", "Type 'show' to see and 'play' to play").lower()

def show_map(guess):
    if guess in my_districts:
        print(guess)
        new_puppy = turtle.Turtle()
        new_puppy.hideturtle()
        new_puppy.penup()
        # new_puppy.goto(0, 0)
        new_puppy.goto(my_x_coors[my_districts.index(guess)], my_y_coors[my_districts.index(guess)])
        new_puppy.write(arg=guess,move=True,font = ('Arial', 13, 'normal'))


while running:
    if what_to_do == 'show':

        for districts in my_districts:
            guess = districts
            show_map(guess)
            a+=1
            if a == len(my_districts):
                running = False
    elif what_to_do == 'play':
        guess = screen.textinput(f"{a}/{len(my_districts)} Guess", 'Which district').title()
        if guess in my_districts:
            show_map(guess)
            a+=1
            if a == len(my_districts):
                running = False

screen.mainloop()
