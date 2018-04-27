import tkinter as tk
from shutil import copyfile

current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"
showcase_maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/Showcase/"
script_path = "F:/World Cup/2018 - Taiko/Scripts/"

#Takes in the team number and their selected ban, then moves appropriate files
def maps(selected_map):

    copyfile(f"{maps_path}{selected_map}_default.png", f"{current_path}showcase_map.png")

#Runs bans()
def multi_btn():

    maps(selected_map.get())

root = tk.Tk()
root.title("Showcase")
root.geometry("200x100")

map_list = []

for numbers in range(0,17):
    map_list.append(numbers)

#Grabs var to hold the selected map from map_list
selected_map = tk.StringVar()
selected_map.set(map_list[0])

#Creates Option Menu with map list
map_menu = tk.OptionMenu(root, selected_map, *map_list)
map_menu.pack(side = tk.TOP)

run_btn = tk.Button(root, text = "Run", command = multi_btn)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()