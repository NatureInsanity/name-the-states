import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_list = []
screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
screen.title("Name the State")

while len(guess_list) < 50:
    answer = screen.textinput(f"{len(guess_list)}/50 States Correct", "Write Down Your Answer").title()
    missing_states = []
    if answer == "Exit":
        for state in all_states:
            if state not in guess_list:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guess_list.append(answer)
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        state_data = data[data.state == answer]
        xcor = int(state_data.x)
        ycor = int(state_data.y)
        pen.goto(xcor, ycor)
        pen.write(state_data.state.item())
