import tkinter as tk
import json
import asyncio

from shutil import copyfile
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetSourceRenderRequest

flags_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Flags/"
schedule_output_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Schedule Files/"
current_output_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
script_path = "F:/World Cup/2018 - Taiko/Scripts/"
resources_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"

# Each match class instance is assigned a match number, team names and time
class match:

    def __init__(self, number, team_1, team_2, match_time, done, conditional, match_score_1, match_score_2):

        self.number = number
        self.team_1 = team_1
        self.team_2 = team_2
        self.match_time = match_time
        self.done = done
        self.conditional = conditional
        self.match_score_1 = match_score_1
        self.match_score_2 = match_score_2

# Copies over the flags and outputs time into .txt
def schedule(matches):

    copyfile(f"{flags_path}{matches.team_1}.png", f"{schedule_output_path}{matches.number}_flag_1.png")
    copyfile(f"{flags_path}{matches.team_2}.png", f"{schedule_output_path}{matches.number}_flag_2.png")

    with open(f"{schedule_output_path}name_{matches.number}.txt", "w") as team_name_1:
        team_name_1.write(f"{matches.team_1}")

    with open(f"{schedule_output_path}name_{matches.number}_{matches.number}.txt", "w") as team_name_2:
        team_name_2.write(f"{matches.team_2}")

    with open(f"{schedule_output_path}{matches.number}_time.txt", "w") as match_time_text:
        match_time_text.write(f"{matches.match_time} UTC")
    
    with open(f"{schedule_output_path}{matches.number}_score_1.txt", "w") as match_score_text_1:
        match_score_text_1.write(f"{matches.match_score_1}")
    
    with open(f"{schedule_output_path}{matches.number}_score_2.txt", "w") as match_score_text_2:
        match_score_text_2.write(f"{matches.match_score_2}")

    if matches.match_score_1 > matches.match_score_2:
        copyfile(f"{resources_path}winner_hl.png", f"{schedule_output_path}{matches.number}_hl_1.png")
        copyfile(f"{resources_path}loser_hl.png", f"{schedule_output_path}{matches.number}_hl_2.png")

    elif matches.match_score_2 > matches.match_score_1:
        copyfile(f"{resources_path}loser_hl.png", f"{schedule_output_path}{matches.number}_hl_1.png")
        copyfile(f"{resources_path}winner_hl.png", f"{schedule_output_path}{matches.number}_hl_2.png")

    # If a tickbox is ticked it hides all associated elements in OBS
    def hide():

        async def hide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_flag", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_flag", render=False, scene_name="Schedule")), 
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_flag_done", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_flag_done", render=True, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_text", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_name", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_name", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_name_done", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_name_done", render=True, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_score", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_score", render=True, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_vs", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_vs_done", render=True, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_hl", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_hl", render=True, scene_name="Schedule"))
                ] )
        
        hide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(hide_2())

    # If a tickbox is unticked it unhides all associated elements in OBS
    def unhide():

        async def unhide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_flag", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_flag", render=True, scene_name="Schedule")), 
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_flag_done", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_flag_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_text", render=True, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_name", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_name", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_name_done", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_name_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_score", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_score", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_vs", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_vs_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_hl", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_hl", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_name 2", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_flag 2", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_vs 2", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_flag 2", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_{matches.number}_name 2", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_text 2", render=True, scene_name="Schedule"))
                ] )
        
        unhide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(unhide_2())

    #If a match is conditional it will unhide the conditional text element
    def unhide_conditional():

        async def unhide_conditional_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_conditional", render=True, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"conditional_explanation", render=True, scene_name="Schedule"))
                ] )
        
        unhide_conditional_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(unhide_conditional_2())

    #If a match is conditional it will hide the conditional text element
    def hide_conditional():

        async def hide_conditional_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"{matches.number}_conditional", render=False, scene_name="Schedule"))
                ] )
        
        hide_conditional_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(hide_conditional_2())


    # Checks if checkbox is ticked and runs appropriate function
    if matches.done == 1:
        hide()
    elif matches.done == 0:
        unhide()
    
    if matches.conditional == 1:
        unhide_conditional()
    elif matches.conditional == 0:
        hide_conditional()

# Creates var count instances of frames with Match #, Team 1 / 2 and time
def frames(count):

    frame = tk.Frame(root)
    frame.pack()

    match_label = tk.Label(frame, text = f"Match {frame_count}")
    match_label.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2], *country_list)
    country_menu.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2 + 1], *country_list)
    country_menu.pack(side = tk.LEFT)

    time_box = tk.Entry(frame, textvariable = time_input_list[count], width = "5")
    time_box.pack(side = tk.LEFT)

    score_box_1 = tk.Entry(frame, textvariable = score_input_list_1[count], width = "2")
    score_box_1.pack(side = tk.LEFT)

    score_box_2 = tk.Entry(frame, textvariable = score_input_list_2[count], width = "2")
    score_box_2.pack(side = tk.LEFT)

    check_box_conditional_box = tk.Checkbutton(frame, text = "Cond.", variable = check_box_conditional_list[count])
    check_box_conditional_box.pack(side = tk.RIGHT)

    check_box_box = tk.Checkbutton(frame, text = "Match Over", variable = check_box_list[count])
    check_box_box.pack(side = tk.RIGHT)

# Resets the entire schedule screen to blank. Previously the elements previously used when moving to a smaller schedule would have to be hidden manually.
def reset_button():

    for count in range(1, 9):

        async def unhide_reset():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"{count}_flag", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_flag", render=False, scene_name="Schedule")), 
                    obsws.require(SetSourceRenderRequest(source=f"{count}_flag_done", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_flag_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_text", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_name", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_name", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_name_done", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_name_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_score", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_score", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_vs", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_vs_done", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_hl", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_hl", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_text 2", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_name 2", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_{count}_flag 2", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_vs 2", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_flag 2", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"{count}_name 2", render=False, scene_name="Schedule")),

                    obsws.require(SetSourceRenderRequest(source=f"{count}_conditional", render=False, scene_name="Schedule")),
                    obsws.require(SetSourceRenderRequest(source=f"conditional_explanation", render=False, scene_name="Schedule"))
                ] )
        
        unhide_reset()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(unhide_reset())

# Runs several actions that need to take place when moving into a new match, avoiding slip-ups
def next_match_button():

    copyfile(f"{maps_path}transparant.png", f"{current_output_path}banned_map_1.png")
    copyfile(f"{maps_path}transparant.png", f"{current_output_path}banned_map_2.png")
    with open(f"{current_output_path}roll_1.txt", "w") as roll_1:
        roll_1.write("")
    with open(f"{current_output_path}roll_2.txt", "w") as roll_2:
        roll_2.write("")

    for count in range(0,15):
        copyfile(f"{maps_path}{count}_default.png", f"{current_output_path}{count}_map.png")

    def next_match_hide():

        async def next_match_hide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"Tourney Client", render=False, scene_name="Mappool")),
                ] )
        
        next_match_hide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(next_match_hide_2())    
    
    next_match_hide()

# Runs code after new inputs are filled in
def run_button():

    frame_count = 0

    for count in range(0, match_amount):

        frame_count = frame_count + 1

        matches = match(f"{frame_count}", selected_country_list[count * 2].get(), selected_country_list[count * 2 + 1].get(), time_input_list[count].get(), check_box_list[count].get(), check_box_conditional_list[count].get(), score_input_list_1[count].get(), score_input_list_2[count].get())

        schedule(matches)

root = tk.Tk()

root.title("OBS Schedule Tool")
root.geometry("500x500")

# Creates country_list based on schedule.json
with open(f"{script_path}countries.json") as file:
    country_data = json.load(file)

country_list = []
for countries in country_data["countries"]:
    country_list.append(countries["abbreviation"])

time_list = ["00:00"]
check_box_input = [False]
check_box_conditional_input = [False]
score_list_1 = ["0"]
score_list_2 = ["0"]

# Creates empty country, time and checkbox lists
selected_country_list = []
time_input_list = []
check_box_list = []
check_box_conditional_list = []
score_input_list_1 = []
score_input_list_2 = []

match_amount = int(input("Match count?:\n"))

# Creates iterations of time_input to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    time_input = tk.StringVar()
    time_input.set(time_list[0])
    time_input_list.append(time_input)

# Creates iterations of score_input to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    score_input_1 = tk.StringVar()
    score_input_1.set(score_list_1[0])
    score_input_list_1.append(score_input_1)

for numbers in range(0, match_amount):

    score_input_2 = tk.StringVar()
    score_input_2.set(score_list_2[0])
    score_input_list_2.append(score_input_2)

# Creates iterations of checkbox to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    check_box = tk.IntVar()
    check_box.set(check_box_input[0])
    check_box_list.append(check_box)

for numbers in range(0, match_amount):

    check_box_conditional = tk.IntVar()
    check_box_conditional.set(check_box_conditional_input[0])
    check_box_conditional_list.append(check_box_conditional)

# Creates iterations of selected_country to be used by frames() at initial runtime
for numbers in range(0, match_amount * 2):

    selected_country = tk.StringVar()
    selected_country.set(country_list[0])
    selected_country_list.append(selected_country)

# Creates frame count for frames()
frame_count = 0

for count in range(0, match_amount):

    frame_count = frame_count + 1
    frames(count)

run_btn = tk.Button(root, text = "Run", command = run_button)
run_btn.pack(side = tk.BOTTOM)

reset_btn = tk.Button(root, text = "Reset Schedule", command = reset_button)
reset_btn.pack(side = tk.BOTTOM)

next_match_btn = tk.Button(root, text = "Next Match", command = next_match_button)
next_match_btn.pack(side = tk.BOTTOM)

root.mainloop()

