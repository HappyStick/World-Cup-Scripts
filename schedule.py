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

# Each match class instance is assigned a match number, team names and time
class match:

    def __init__(self, number, team_1, team_2, match_time, done, match_score):

        self.number = number
        self.team_1 = team_1
        self.team_2 = team_2
        self.match_time = match_time
        self.done = done
        self.match_score = match_score

# Copies over the flags and outputs time into .txt
def schedule(matches):

    copyfile(f"{flags_path}{matches.team_1}.png", f"{schedule_output_path}{matches.number}_flag_1.png")
    copyfile(f"{flags_path}{matches.team_2}.png", f"{schedule_output_path}{matches.number}_flag_2.png")

    with open(f"{schedule_output_path}{matches.number}_time.txt", "w") as match_time_text:
        match_time_text.write(f"{matches.match_time} UTC")
    
    with open(f"{schedule_output_path}{matches.number}_score.txt", "w") as match_score_text:
        match_score_text.write(f"{matches.match_score}")

    # If a tickbox is ticked it hides all associated elements in OBS
    def hide():

        async def hide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, password) as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}", render=False, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_{matches.number}", render=False, scene_name="Scene")),   
                    obsws.require(SetSourceRenderRequest(source=f"text_{matches.number}", render=False, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_done", render=True, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_{matches.number}_done", render=True, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"match_{matches.number}_score", render=True, scene_name="Scene"))
                ] )
        
        hide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(hide_2())

    # If a tickbox is unticked it unhides all associated elements in OBS
    def unhide():

        async def unhide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, password) as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}", render=True, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_{matches.number}", render=True, scene_name="Scene")),   
                    obsws.require(SetSourceRenderRequest(source=f"text_{matches.number}", render=True, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_done", render=False, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"flag_{matches.number}_{matches.number}_done", render=False, scene_name="Scene")),
                    obsws.require(SetSourceRenderRequest(source=f"match_{matches.number}_score", render=False, scene_name="Scene"))
                ] )
        
        unhide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(unhide_2())

    # Checks if checkbox is ticked and runs appropriate function
    if matches.done == 1:
        hide()
    elif matches.done == 0:
        unhide()

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

    score_box = tk.Entry(frame, textvariable = score_input_list[count], width = "4")
    score_box.pack(side = tk.LEFT)

    check_box_box = tk.Checkbutton(frame, variable = check_box_list[count])
    check_box_box.pack(side = tk.RIGHT) 

# Runs code after new inputs are filled in
def run_button():

    frame_count = 0

    for count in range(0, match_amount):

        frame_count = frame_count + 1

        matches = match(f"{frame_count}", selected_country_list[count * 2].get(), selected_country_list[count * 2 + 1].get(), time_input_list[count].get(), check_box_list[count].get(), score_input_list[count].get())

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
score_list = ["0 : 0"]

# Creates empty country, time and checkbox lists
selected_country_list = []
time_input_list = []
check_box_list = []
score_input_list = []

match_amount = int(input("Match count?:\n"))

# Creates 12 iterations of time_input to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    time_input = tk.StringVar()
    time_input.set(time_list[0])
    time_input_list.append(time_input)

# Creates 12 iterations of score_input to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    score_input = tk.StringVar()
    score_input.set(score_list[0])
    score_input_list.append(score_input)

# Creates 12 iterations of checkbox to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    check_box = tk.IntVar()
    check_box.set(check_box_input[0])
    check_box_list.append(check_box)

# Creates 24 iterations of selected_country to be used by frames() at initial runtime
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

root.mainloop()

