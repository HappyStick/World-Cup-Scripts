import requests
import json
import time
import tkinter as tk
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import decimal

def frames(count):

    frame = tk.Frame(root)
    frame.pack()

    map_label = tk.Label(frame, text = f"Map {count + 1}")
    map_label.pack(side = tk.LEFT)

    map_id_entry = tk.Entry(frame, textvariable = map_id_list[count], width = "20")
    map_id_entry.pack(side = tk.LEFT)

    mod_entry = tk.OptionMenu(frame, mod_pick_list[count], *mods)
    mod_entry.pack(side = tk.LEFT)

def get_values(count, map_id, mod, mappoolfile):

    r = requests.get(f"http://osu.ppy.sh/beatmaps/{map_id}")
    r = r.text
    soup = BeautifulSoup(r, "lxml")
    soup.prettify()
    soup = soup.find_all(id = "json-beatmapset")
    soup = str(soup)
    soup = soup[63:-15]

    with open("F:/World Cup/2018 - Current cup/Scripts/html_file.txt", "w") as json_file:
        json_file.write(soup)

    with open("F:/World Cup/2018 - Current cup/Scripts/html_file.txt", "r") as json_file:
        content = json.load(json_file)

    with open("F:/World Cup/2018 - Current cup/Scripts/map_info.json", "w") as json_file:
        json.dump(content, json_file, indent = 1)
        
    with open("F:/World Cup/2018 - Current cup/Scripts/map_info.json") as json_file:
        map_data = json.load(json_file)

    bpm_value = round(map_data["bpm"], 1)

    i = 0

    for maps in map_data["beatmaps"]:

        if map_data["beatmaps"][i]["id"] == int(map_id):
            time_value = map_data["beatmaps"][i]["total_length"]
            ar_value = map_data["beatmaps"][i]["ar"]
            cs_value = map_data["beatmaps"][i]["cs"]
            drain_value = map_data["beatmaps"][i]["drain"]
        
        i = i + 1

    for maps in map_data["converts"]:

        if map_data["converts"][i]["id"] == int(map_id):
            time_value = map_data["converts"][i]["total_length"]
            ar_value = map_data["converts"][i]["ar"]
            cs_value = map_data["converts"][i]["cs"]
            drain_value = map_data["converts"][i]["drain"]

        i = i + 1

    ar_value = ar_value + 0.0
    cs_value = cs_value + 0.0
    drain_value = drain_value + 0.0
    
    mappool = {"map_number" : str(count + 1),
                "mod" : str(mod),
                "length" : str(time_value),
                "bpm" : str(bpm_value),
                "ar" : str(ar_value),
                "cs" : str(cs_value),
                "hp" : str(drain_value)}
    
    mappool_list.append(mappool)

def run_button():

    frame_count = 0

    for count in range(0, map_amount):

        get_values(frame_count, map_id_list[count].get(), mod_pick_list[count].get(), mappool_list)

        frame_count = frame_count + 1

def export_button():

    mappool_final = {"mappool" : mappool_list}

    with open("F:/World Cup/2018 - Current cup/Scripts/showcase.json", "w") as json_file:
        json.dump(mappool_final, json_file, indent = 4)

map_amount = int(input("Mappool Size?:\n"))

root = tk.Tk()
root.title("Mappool Info")
root.geometry("500x600")

id_list = ["id"]
mappool_list = []
mods = ["NM", "HD", "HR", "DT", "FM", "TB"]
map_id_list = []
mod_pick_list = []

for numbers in range(0, map_amount):
    map_id = tk.StringVar()
    map_id.set(id_list[0])
    map_id_list.append(map_id)

for numbers in range(0, map_amount):
    mod_pick = tk.StringVar()
    mod_pick.set(mods[0])
    mod_pick_list.append(mod_pick)

frame_count = 0

for count in range(0, map_amount):

    frame_count = frame_count + 1
    frames(count)

run_btn = tk.Button(root, text = "Run", command = run_button)
run_btn.pack(side = tk.BOTTOM)

export_btn = tk.Button(root, text = "Export", command = export_button)
export_btn.pack(side = tk.BOTTOM)

root.mainloop()