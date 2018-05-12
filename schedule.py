import tkinter as tk
import math
import json
import asyncio

from shutil import copyfile
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetSourceRenderRequest

flags_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Flags/"
schedule_output_path = "F:/World Cup/2018 - Current Cup/Scripts/OBS Output/Schedule Files/"
current_output_path = "F:/World Cup/2018 - Current Cup/Scripts/OBS Output/Current Files/"
script_path = "F:/World Cup/2018 - Current Cup/Scripts/"
resources_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/"
maps_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Maps/"
rounds_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Round Name Files/"
players_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Country Players/"

# Each match class instance is assigned a match number, team names and time
class match:

    def __init__(self, number, team_1, team_2, match_time, done, conditional, current, match_score_1, match_score_2, round_name):

        self.number = number
        self.team_1 = team_1
        self.team_2 = team_2
        self.match_time = match_time
        self.done = done
        self.conditional = conditional
        self.current = current
        self.match_score_1 = match_score_1
        self.match_score_2 = match_score_2
        self.round_name = round_name

# Copies over the flags and outputs time into .txt
def schedule(matches, month, day, satsun):

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

    if matches.current == 1:
        current(matches, month, str(day), satsun)

# Updates all settings for currently selected match
def current(matches, month, day, satsun):

    with open(f"{script_path}country_players.json") as file:
        country_data_current = json.load(file)

    country_players_list = list(country_data_current.keys())
    full_country_name_1 = ""
    full_country_name_2 = ""

    i = 0
    for countries in country_data_current.values():
        if countries["Abbreviation"] == matches.team_1:
            full_country_name_1 = country_players_list[i]
        if countries["Abbreviation"] == matches.team_2:
            full_country_name_2 = country_players_list[i]
        i += 1

    def flag_location(color, country_name):

        copyfile(f"{flags_path}{country_name}.png", f"{current_output_path}{color}_flag.png")
    
    def country_names(color, country_name, country_name_short):

        with open(f"{current_output_path}country_file_{color}.txt", "w") as country_file:
            country_file.write(country_name)
        with open(f"{current_output_path}country_file_{color}_short.txt", "w") as country_file_short:
            country_file_short.write(country_name_short)

    def match_times(month, day, time):

        with open(f"{current_output_path}match_time.txt", "w") as match_file:
            match_file.write(f"{day} {month} {time} UTC")
        with open(f"{current_output_path}match_time_short.txt", "w") as match_time:
            match_time.write(f"{time} UTC")

    def player_lists(color, country_name):

        # Adds user_input .txt into memory then reads the lines in the .txt and inputs it into var
        player_list = open((f"{players_path}{country_name}.txt"), "r")
        player_data = player_list.readlines()

        # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
        for number in range(5):
            # Ensures that if a country has less than 4 players it creates an empty .txt for each slot
            if number < len(player_data):
                player = player_data[number]

                with open(f"{current_output_path}{color}_player{str(number + 1)}.txt", "w+") as player_name:
                    player_name.write(player)

            else:
                with open(f"{current_output_path}{color}_player{str(number + 1)}.txt", "w+") as empty_name:
                    empty_name.write("")

        player_list.close()

    def round_names(round, satsun):

        copyfile(f"{rounds_path}{matches.round_name}.png", f"{current_output_path}current_round.png")
        copyfile(f"{rounds_path}intro {matches.round_name}.png", f"{current_output_path}current_round_intro.png")

        if satsun == "Sat":
            copyfile(f"{rounds_path}{satsun} sched {matches.round_name}.png", f"{current_output_path}current_round_schedule.png")
        if satsun == "Sun":
            copyfile(f"{rounds_path}{satsun} sched {matches.round_name}.png", f"{current_output_path}current_round_schedule.png")

    flag_location("red", matches.team_1)
    flag_location("blue", matches.team_2)

    country_names("red", full_country_name_1, matches.team_1)
    country_names("blue", full_country_name_2, matches.team_2)

    match_times(selected_month.get(), str(selected_day.get()), matches.match_time)

    player_lists("red", full_country_name_1)
    player_lists("blue", full_country_name_2)

    round_names(matches.round_name, satsun)

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

    round_input = tk.OptionMenu(frame, selected_round_list[count], *round_list)
    round_input.pack(side = tk.LEFT)

    score_box_1 = tk.Entry(frame, textvariable = score_input_list_1[count], width = "2")
    score_box_1.pack(side = tk.LEFT)

    score_box_2 = tk.Entry(frame, textvariable = score_input_list_2[count], width = "2")
    score_box_2.pack(side = tk.LEFT)

    check_box_current_box = tk.Checkbutton(frame, text = "Current", variable = check_box_current_list[count])
    check_box_current_box.pack(side = tk.LEFT)

    check_box_box = tk.Checkbutton(frame, text = "Finished", variable = check_box_list[count])
    check_box_box.pack(side = tk.LEFT)

    check_box_conditional_box = tk.Checkbutton(frame, text = "Cond.", variable = check_box_conditional_list[count])
    check_box_conditional_box.pack(side = tk.LEFT)

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
        roll_1.write("-")
    with open(f"{current_output_path}roll_2.txt", "w") as roll_2:
        roll_2.write("-")

    for count in range(0,15):
        copyfile(f"{maps_path}{count}_default.png", f"{current_output_path}{count}_map.png")

    copyfile(f"{maps_path}/transparant.png", f"{current_output_path}showcase_map.png")

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

        matches = match(f"{frame_count}", selected_country_list[count * 2].get(), selected_country_list[count * 2 + 1].get(), time_input_list[count].get(), check_box_list[count].get(), check_box_conditional_list[count].get(), check_box_current_list[count].get(), score_input_list_1[count].get(), score_input_list_2[count].get(), selected_round_list[count].get())

        schedule(matches, selected_month.get(), selected_day.get(), selected_satsun.get())

root = tk.Tk()

root.title("OBS Schedule Tool")
root.geometry("600x500")

# Creates country_list based on schedule.json
with open(f"{script_path}country_players.json") as file:
    country_data = json.load(file)

country_list = []

for countries in country_data.values():
    country_list.append(countries["Abbreviation"])

with open(f"{script_path}cupinfo.json") as file:
    cupinfo_data = json.load(file)

month_list = []
round_list = []

for months in cupinfo_data["months"]:
    month_list.append(months)

for rounds in cupinfo_data["rounds"]:
    round_list.append(rounds)

day_list = range(1, 32)
satsun_list = ["Sat", "Sun"]
time_list = ["00:00"]
check_box_input = [False]
check_box_conditional_input = [False]
check_box_current_input = [False]
score_list_1 = [""]
score_list_2 = [""]

selected_country_list = []
selected_round_list = []
time_input_list = []
check_box_list = []
check_box_conditional_list = []
check_box_current_list = []
score_input_list_1 = []
score_input_list_2 = []

match_amount = int(input("Match count?:\n"))

for numbers in range(0, match_amount):

    time_input = tk.StringVar()
    time_input.set(time_list[0])
    time_input_list.append(time_input)

for numbers in range(0, match_amount):

    score_input_1 = tk.StringVar()
    score_input_1.set(score_list_1[0])
    score_input_list_1.append(score_input_1)

for numbers in range(0, match_amount):

    score_input_2 = tk.StringVar()
    score_input_2.set(score_list_2[0])
    score_input_list_2.append(score_input_2)

for numbers in range(0, match_amount):

    check_box = tk.IntVar()
    check_box.set(check_box_input[0])
    check_box_list.append(check_box)

for numbers in range(0, match_amount):

    check_box_conditional = tk.IntVar()
    check_box_conditional.set(check_box_conditional_input[0])
    check_box_conditional_list.append(check_box_conditional)

for numbers in range(0, match_amount):

    check_box_current = tk.IntVar()
    check_box_current.set(check_box_current_input[0])
    check_box_current_list.append(check_box_current)

for numbers in range(0, match_amount * 2):

    selected_country = tk.StringVar()
    selected_country.set(country_list[0])
    selected_country_list.append(selected_country)

for numbers in range(0, match_amount):

    selected_round = tk.StringVar()
    selected_round.set(round_list[0])
    selected_round_list.append(selected_round)

# Creates frame count for frames()
frame_count = 0

for count in range(0, match_amount):

    frame_count = frame_count + 1
    frames(count)

frame2 = tk.Frame(root)
frame2.pack()

selected_day = tk.StringVar()
selected_day.set(day_list[0])

selected_month = tk.StringVar()
selected_month.set(month_list[0])

selected_satsun = tk.StringVar()
selected_satsun.set(satsun_list[0])

satsun_menu = tk.OptionMenu(frame2, selected_satsun, *satsun_list)
satsun_menu.pack(side = tk.LEFT)

day_menu = tk.OptionMenu(frame2, selected_day, *day_list)
day_menu.pack(side = tk.LEFT)

month_menu = tk.OptionMenu(frame2, selected_month, *month_list)
month_menu.pack(side = tk.LEFT)

run_btn = tk.Button(root, text = "Run", command = run_button)
run_btn.pack(side = tk.BOTTOM)

reset_btn = tk.Button(root, text = "Reset Schedule", command = reset_button)
reset_btn.pack(side = tk.BOTTOM)

next_match_btn = tk.Button(root, text = "Next Match", command = next_match_button)
next_match_btn.pack(side = tk.BOTTOM)

root.mainloop()

