from turtle import Turtle, Screen
import pandas

screen = Screen()
state_map = Turtle()
states = Turtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

state_map.shape(image)

data_states = pandas.read_csv("50_states.csv")
all_states = data_states["state"].to_list()
# print(all_states)
guess_state = []

game = True

score = 0

while game:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").title()
    for state in all_states:
        if answer_state == "Exit":
            learn_state = [state for state in all_states if state not in guess_state]
            # learn_state = []
            # for state in all_states:
            #     if state not in guess_state:
            #         learn_state.append(state)
            # print(learn_state)
            data = pandas.DataFrame(learn_state)
            data.to_csv("states_to_learn.csv")
            game = False
            break
        elif answer_state == state:
            states.hideturtle()
            states.penup()
            pos_x = int(data_states[data_states.state == answer_state].x)
            pos_y = int(data_states[data_states.state == answer_state].y)
            states.goto(pos_x, pos_y)
            states.write(answer_state, align="center", font=("Arial", 12, "normal"))
            score += 1
            guess_state.append(answer_state)
        else:
            game = True
