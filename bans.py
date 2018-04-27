import tkinter as tk
from shutil import copyfile

current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"
script_path = "F:/World Cup/2018 - Taiko/Scripts/"

def bans(team_number, selected_ban):

    copyfile(f"{maps_path}{selected_ban}_default.png", f"{current_path}banned_map_{team_number}.png")

def multi_btn():

    bans("1", selected_ban_1.get())
    bans("2", selected_ban_2.get())

root = tk.Tk()
root.title("Bans")
root.geometry("200x100")

map_list = []

for numbers in range(0,14):
    map_list.append(numbers)

selected_ban_1 = tk.StringVar()
selected_ban_1.set(map_list[0])

selected_ban_2 = tk.StringVar()
selected_ban_2.set(map_list[0])

map_menu_1 = tk.OptionMenu(root, selected_ban_1, *map_list)
map_menu_1.pack(side = tk.LEFT)

map_menu_2 = tk.OptionMenu(root, selected_ban_2, *map_list)
map_menu_2.pack(side = tk.RIGHT)

run_btn = tk.Button(root, text = "Run", command = multi_btn)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()