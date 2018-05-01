import tkinter as tk
import asyncio

from shutil import copyfile
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetSourceRenderRequest

current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
schedule_output_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Schedule Files/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"
script_path = "F:/World Cup/2018 - Taiko/Scripts/"

root = tk.Tk()
root.title("Mappool")
root.geometry("300x550")

#Copies over different files depending on drop down menu pick
def picks(option, count):

    if selected_option_list[count].get() == "Unpicked":

        copyfile(f"{maps_path}{count}_default.png", f"{current_path}{count}_map.png")
    
    elif selected_option_list[count].get() == "Red":

        copyfile(f"{maps_path}{count}_red.png", f"{current_path}{count}_map.png")

    elif selected_option_list[count].get() == "Blue":

        copyfile(f"{maps_path}{count}_blue.png", f"{current_path}{count}_map.png")
    
    elif selected_option_list[count].get() == "Red Ban":

        copyfile(f"{maps_path}{count}_bw.png", f"{current_path}{count}_map.png")
        copyfile(f"{maps_path}{count}_default.png", f"{current_path}banned_map_1.png")
    
    elif selected_option_list[count].get() == "Blue Ban":

        copyfile(f"{maps_path}{count}_bw.png", f"{current_path}{count}_map.png")
        copyfile(f"{maps_path}{count}_default.png", f"{current_path}banned_map_2.png")

# Writes the rolls into the appropriate files
def rolls(team_number, selected_roll):

    with open(f"{current_path}roll_{team_number}.txt", "w") as roll:
        roll.write(selected_roll)

# Creates the appropriate amount of instances for the row of mods & map numbers
def frames(count):
    
    frame = tk.Frame(root)
    frame.pack()

# These statements give the mods their specific colour, ensuring ease of use
    if mod_list[count] == "NM":

        map_label = tk.Label(frame, bg = "#FFFFFF", font = "exo2.0", text = f"{mod_list[count]} - {count + 1}")
        map_label.pack(side = tk.LEFT)
        pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
        pick_menu.config(bg = "#FFFFFF", font = "exo2.0")
        pick_menu.pack(side = tk.LEFT)

    if mod_list[count] == "HD":

        map_label = tk.Label(frame, bg = "#FFFF66", font = "exo2.0", text = f"{mod_list[count]} - {count + 1}")
        map_label.pack(side = tk.LEFT)
        pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
        pick_menu.config(bg = "#FFFF66", font = "exo2.0")
        pick_menu.pack(side = tk.LEFT)
    
    if mod_list[count] == "HR":

        map_label = tk.Label(frame, bg = "#F08080", font = "exo2.0", text = f"{mod_list[count]} - {count + 1}")
        map_label.pack(side = tk.LEFT)
        pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
        pick_menu.config(bg = "#F08080", font = "exo2.0")
        pick_menu.pack(side = tk.LEFT)
    
    if mod_list[count] == "DT": 

        map_label = tk.Label(frame, bg = "#6495ED", font = "exo2.0", text = f"{mod_list[count]} - {count + 1}")
        map_label.pack(side = tk.LEFT)
        pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
        pick_menu.config(bg = "#6495ED", font = "exo2.0")
        pick_menu.pack(side = tk.LEFT)

    if mod_list[count] == "FM": 

        map_label = tk.Label(frame, bg = "#BA55D3", font = "exo2.0", text = f"{mod_list[count]} - {count + 1}")
        map_label.pack(side = tk.LEFT)
        pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
        pick_menu.config(bg = "#BA55D3", font = "exo2.0")
        pick_menu.pack(side = tk.LEFT)

def run_button():

    for count in range(0, map_amount):
        picks(selected_option_list[count].get(), count)
    
    rolls("1", selected_roll_1.get())
    rolls("2", selected_roll_2.get())

    # Unhide Tourney Client from Mappool Selection screen when any mappool-related action is taken
    def tourney_client_unhide():

        async def tourney_client_unhide_2():

            await asyncio.sleep(0.01)
            async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                await asyncio.wait( [
                    obsws.require(SetSourceRenderRequest(source=f"Tourney Client", render=True, scene_name="Mappool")),
                ] )
        
        tourney_client_unhide_2()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(tourney_client_unhide_2())    
    
    tourney_client_unhide()

map_list = []
option_list = ["Unpicked", "Red", "Blue", "Red Ban", "Blue Ban"]
mod_list = ["NM", "NM", "NM", "NM", "NM", "NM", "HD", "HD", "HR", "HR", "DT", "DT", "FM", "FM", "FM"]
selected_option_list = []

#Grabs vars from user input
selected_roll_1 = tk.StringVar()
selected_roll_1.set("-")

selected_roll_2 = tk.StringVar()
selected_roll_2.set("-")

roll_box_1 = tk.Entry(root, font = "exo2.0", justify = tk.CENTER, bg = "#F08080", textvariable = selected_roll_1, width = "6")
roll_box_1.pack(side = tk.LEFT)

roll_box_2 = tk.Entry(root, font = "exo2.0", justify = tk.CENTER, bg = "#87CEFA", textvariable = selected_roll_2, width = "6")
roll_box_2.pack(side = tk.RIGHT)

map_amount = int(input("Mappool size?:\n"))

for numbers in range(0, map_amount):
    map_list.append(numbers)

#Stores the selected option for each in a list
for numbers in range(0, map_amount):

    selected_option = tk.StringVar()
    selected_option.set(option_list[0])
    selected_option_list.append(selected_option)

#Runs frames() equal to the mappool size
frame_count = 0

for count in range(0, map_amount):

    frames(count)
    frame_count = frame_count + 1

run_btn = tk.Button(root, text = "Run", command = run_button)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()

