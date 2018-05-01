import tkinter as tk
import json

from shutil import copyfile

current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"
showcase_maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/Showcase/"
script_path = "F:/World Cup/2018 - Taiko/Scripts/"


#Takes in the team number and their selected ban, then moves appropriate files
def maps(selected_map):

    if selected_map == "None":
        copyfile(f"{showcase_maps_path}/transparant.png", f"{current_path}showcase_map.png")

        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write("-")

        with open(f"{current_path}map_value_bpm.txt", "w") as value:
            value.write("-")

        with open(f"{current_path}map_value_ar.txt", "w") as value:
            value.write("-")

        with open(f"{current_path}map_value_cs.txt", "w") as value:
            value.write("-")

        with open(f"{current_path}map_value_hp.txt", "w") as value:
            value.write("-")

    else:
        copyfile(f"{maps_path}showcase/{int(selected_map) - 1}_default.png", f"{current_path}showcase_map.png")

def values(selected_map):

    if selected_map == "None":
        pass
    else:
        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write(map_length_list[int(selected_map) - 1])
        
        with open(f"{current_path}map_value_bpm.txt", "w") as value:
            value.write(map_bpm_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_ar.txt", "w") as value:
            value.write(map_ar_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_cs.txt", "w") as value:
            value.write(map_cs_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_hp.txt", "w") as value:
            value.write(map_hp_list[int(selected_map) - 1])

#Runs bans()
def multi_btn():

    maps(selected_map.get())

    values(selected_map.get())

#map_amount = int(input("Mappool size?:\n"))

root = tk.Tk()
root.title("Showcase")
root.geometry("200x100")

map_list = ["None"]
map_length_list = []
map_bpm_list = []
map_ar_list = []
map_cs_list = []
map_hp_list = []

with open(f"{script_path}showcase.json") as file:
    showcase_data = json.load(file)

for maps_amount in showcase_data["mappool"]:
    map_list.append(maps_amount["map_number"])

for maps_amount in showcase_data["mappool"]:
    map_length_list.append(maps_amount["length"])

for maps_amount in showcase_data["mappool"]:
    map_bpm_list.append(maps_amount["bpm"])

for maps_amount in showcase_data["mappool"]:
    map_ar_list.append(maps_amount["ar"])

for maps_amount in showcase_data["mappool"]:
    map_cs_list.append(maps_amount["cs"])

for maps_amount in showcase_data["mappool"]:
    map_hp_list.append(maps_amount["hp"])

map_amount = 0
while map_amount != len(map_list):
    map_amount += 1

#Grabs var to hold the selected map from map_list
selected_map = tk.StringVar()
selected_map.set(map_list[0])

#Creates Option Menu with map list
map_menu = tk.OptionMenu(root, selected_map, *map_list)
map_menu.pack(side = tk.TOP)

run_btn = tk.Button(root, text = "Run", command = multi_btn)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()