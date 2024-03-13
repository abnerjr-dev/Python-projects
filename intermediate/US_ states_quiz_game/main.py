import turtle as t
import pandas as pd
from writer import Writer

screen = t.Screen()
screen.title("Name The US States")
screen.bgpic("intermediate/US_ states_quiz_game/blank_states_img.gif")
screen.setup(725, 491)

writer = Writer()

data = pd.read_csv("intermediate/US_ states_quiz_game/50_states.csv")
state_list = data["state"].to_list()
correct_guesses = []

game_on = True
score = 0

while game_on:
    answer = screen.textinput(
        title=f"{score}/50 Guessed Correctly", prompt="Name a new State:"
    ).title()

    if answer == "Exit":
        missing_states = [s for s in state_list if s not in correct_guesses]
        # missing_states = []
        # for s in state_list:
        #     if s not in correct_guesses:
        #         missing_states.append(s)

        missing_states_dict = {"States to Learn": missing_states}
        ds = pd.DataFrame(missing_states_dict)
        ds.to_csv("intermediate/US_ states_quiz_game/states_to_learn.csv")

        for state in missing_states:
            state_info = data[data["state"] == state]
            s_x = int(state_info["x"])
            s_y = int(state_info["y"])
            writer.color("red")
            writer.write_state(state=state, x=s_x, y=s_y)

        break

    if answer in state_list:
        state_info = data[data["state"] == answer]
        state_x = int(state_info["x"])
        state_y = int(state_info["y"])
        if answer not in correct_guesses:
            score += 1
            writer.write_state(state=answer, x=state_x, y=state_y)
            correct_guesses.append(answer)

    if len(correct_guesses) == len(state_list):
        game_on = False
        writer.winner()


screen.mainloop()
