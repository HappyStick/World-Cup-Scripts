import tkinter as tk

from shutil import copyfile

current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"
maps_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Maps/"

root = tk.Tk()
root.title("Mappool")
root.geometry("500x500")

#Copies over different files depending on drop down menu pick
def picks(option, count):

    if selected_option_list[count].get() == "Unpicked":

        copyfile(f"{maps_path}{count}_default.png", f"{current_path}{count}_map.png")
    
    elif selected_option_list[count].get() == "Red":

        copyfile(f"{maps_path}{count}_red.png", f"{current_path}{count}_map.png")

    elif selected_option_list[count].get() == "Blue":

        copyfile(f"{maps_path}{count}_blue.png", f"{current_path}{count}_map.png")
    
    elif selected_option_list[count].get() == "Banned":

        copyfile(f"{maps_path}{count}_bw.png", f"{current_path}{count}_map.png")

#Creates the appropriate amount of instances for the row of mods & map numbers
def frames(count):
    
    frame = tk.Frame(root)
    frame.pack()

    map_label = tk.Label(frame, text = f"{mod_list[count]} - {count}")
    map_label.pack(side = tk.LEFT)

    pick_menu = tk.OptionMenu(frame, selected_option_list[count], *option_list)
    pick_menu.pack(side = tk.LEFT)

def run_button():

    for count in range(0, 13):
        picks(selected_option_list[count].get(), count)

map_list = []
option_list = ["Unpicked", "Red", "Blue", "Banned"]
mod_list = ["NM", "NM", "NM", "NM", "NM", "HD", "HD", "HR", "HR", "DT", "DT", "FM", "FM"]
selected_option_list = []

for numbers in range(0, 13):
    map_list.append(numbers)

#Stores the selected option for each in a list
for numbers in range(0, 13):

    selected_option = tk.StringVar()
    selected_option.set(option_list[0])
    selected_option_list.append(selected_option)

#Makes frames() run 12 times, equal to the mappool size
frame_count = 0

for count in range(0, 13):

    frame_count = frame_count + 1
    frames(count)

run_btn = tk.Button(root, text = "Run", command = run_button)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()

