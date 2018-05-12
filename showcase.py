import tkinter as tk
import json
import asyncio
import datetime
import urllib.request
import os

from shutil import copyfile
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetSourceRenderRequest
from PIL import Image

current_path = "F:/World Cup/2018 - Current Cup/Scripts/OBS Output/Current Files/"
maps_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Maps/"
mappool_cards = "F:/World Cup/2018 - Current Cup/Scripts/mappool_cards/"
showcase_maps_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Maps/Showcase/"
showcase_images_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Maps/Showcase Images/"
showcase_replays_path = "F:/World Cup/2018 - Current Cup/Scripts/Resources/Maps/Showcase Replays/"
script_path = "F:/World Cup/2018 - Current Cup/Scripts/"

#This allows for clearing of the scene if there's nothing to show
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

        with open(f"{current_path}map_adjusted_value_ar.txt", "w") as value:
            value.write("-")

    else:
        copyfile(f"{maps_path}showcase/{int(selected_map) - 1}_default.png", f"{current_path}showcase_map.png")

#This entire section ensures output of appropriate values into .txt files based on showcase.json
def values(selected_map):

    #If there are no adjusted values necessary (in None or HD situations) it hides the extra value graphics
    def hide_adjusted():

            async def hide_adjusted_2():

                await asyncio.sleep(0.01)
                async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                    await asyncio.wait( [
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values HR", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values DT", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values FM", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map AR Value Adjusted HR DT", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map CS Value Adjusted HR", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map HP Value Adjusted HR", render=False, scene_name="Mappool Showcase"))
                    ] )
            
            hide_adjusted_2()
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(hide_adjusted_2())

    if selected_map == "None":

        hide_adjusted()

    #In case of a map being HR or FM it sets up the scene with the right graphics and pulls the basic values as well as converts them to the HR values
    elif (map_mod_list[int(selected_map) - 1] == "HR") or (map_mod_list[int(selected_map) - 1] == "FM"):

        def unhide_adjusted_hr():

            async def unhide_adjusted_hr_2():

                await asyncio.sleep(0.01)
                async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                    await asyncio.wait( [
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values FM", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values HR", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values DT", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map AR Value Adjusted HR DT", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map CS Value Adjusted HR", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map HP Value Adjusted HR", render=True, scene_name="Mappool Showcase"))
                    ] )
            
            unhide_adjusted_hr_2()
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(unhide_adjusted_hr_2())
        
        def unhide_adjusted_fm():

            async def unhide_adjusted_fm_2():

                await asyncio.sleep(0.01)
                async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                    await asyncio.wait( [
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values FM", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values HR", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values DT", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map AR Value Adjusted HR DT", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map CS Value Adjusted HR", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map HP Value Adjusted HR", render=True, scene_name="Mappool Showcase"))
                    ] )
            
            unhide_adjusted_fm_2()
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(unhide_adjusted_fm_2())

        with open(f"{current_path}map_value_ar.txt", "w") as value:
            value.write(map_ar_list[int(selected_map) - 1])

        adjusted_value_hr = float(map_ar_list[int(selected_map) - 1]) * 1.4
        if adjusted_value_hr > 10.0:
            adjusted_value_hr = 10.0
        with open(f"{current_path}map_adjusted_value_ar.txt", "w") as value:
            value.write(str("%.1f" % adjusted_value_hr))
        
        with open(f"{current_path}map_value_hp.txt", "w") as value:
            value.write(map_hp_list[int(selected_map) - 1])

        adjusted_value_hp = float(map_hp_list[int(selected_map) - 1]) * 1.3
        if adjusted_value_hp > 10.0:
            adjusted_value_hp = 10.0
        with open(f"{current_path}map_adjusted_value_hp.txt", "w") as value:
            value.write(str("%.1f" % adjusted_value_hp))

        with open(f"{current_path}map_value_cs.txt", "w") as value:
            value.write(map_cs_list[int(selected_map) - 1])

        adjusted_value_cs = float(map_cs_list[int(selected_map) - 1]) * 1.4
        with open(f"{current_path}map_adjusted_value_cs.txt", "w") as value:
            value.write(str("%.1f" % adjusted_value_cs))
        
        adjusted_length_value = map_length_list[int(selected_map) - 1]
        adjusted_length_value = str(datetime.timedelta(seconds = int(adjusted_length_value)))

        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write(adjusted_length_value[2:])
        
        rounded_bpm = float(map_bpm_list[int(selected_map) - 1])
        float(rounded_bpm)
        rounded_bpm = rounded_bpm * 1.0

        with open(f"{current_path}map_value_bpm.txt", "w") as value:
            value.write(str("%.0f" % rounded_bpm))
        
        if map_mod_list[int(selected_map) - 1] == "HR":
            unhide_adjusted_hr()
        
        if map_mod_list[int(selected_map) - 1] == "FM":
            unhide_adjusted_fm()

    #In case of a map being DT it sets up the scene with the right graphics and pulls the basic values as well as converts them to the DT values
    elif map_mod_list[int(selected_map) - 1] == "DT":

        def unhide_adjusted_dt():

            async def unhide_adjusted_dt_2():

                await asyncio.sleep(0.01)
                async with OBSWS("localhost", 4444, "PIqDeb0q7QYCNunQUMyC") as obsws:
                    await asyncio.wait( [
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values FM", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values DT", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Mappool Showcase Values HR", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map AR Value Adjusted HR DT", render=True, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map CS Value Adjusted HR", render=False, scene_name="Mappool Showcase")),
                        obsws.require(SetSourceRenderRequest(source=f"Map HP Value Adjusted HR", render=False, scene_name="Mappool Showcase"))
                    ] )
            
            unhide_adjusted_dt_2()
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(unhide_adjusted_dt_2())

        with open(f"{current_path}map_value_ar.txt", "w") as value:
            value.write(map_ar_list[int(selected_map) - 1])
        
        adjusted_value_ar_dt = (1950 - ((1950 -  (150 * float(map_ar_list[int(selected_map) - 1]))) / 1.5)) / 150
        if adjusted_value_ar_dt > 11.0:
            adjusted_value_ar_dt = 11.0
        with open(f"{current_path}map_adjusted_value_ar.txt", "w") as value:
            value.write(str("%.1f" % adjusted_value_ar_dt))
        
        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write(map_length_list[int(selected_map) - 1])
        
        adjusted_length_value = float(map_length_list[int(selected_map) - 1])
        float(adjusted_length_value)
        adjusted_length_value = adjusted_length_value / 1.5
        int(adjusted_length_value)
        adjusted_length_value = str(datetime.timedelta(seconds = int(adjusted_length_value)))

        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write(str(adjusted_length_value[2:]))

        adjusted_bpm_value = float(map_bpm_list[int(selected_map) - 1])
        float(adjusted_bpm_value)
        adjusted_bpm_value = adjusted_bpm_value * 1.5
        with open(f"{current_path}map_value_bpm.txt", "w") as value:
            value.write(str("%.0f" % adjusted_bpm_value))
        
        with open(f"{current_path}map_value_cs.txt", "w") as value:
            value.write(map_cs_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_hp.txt", "w") as value:
            value.write(map_hp_list[int(selected_map) - 1])

        unhide_adjusted_dt()

    #Pulls all data in case it's Nomod or HD and displays the base values
    else:

        hide_adjusted()

        adjusted_length_value = map_length_list[int(selected_map) - 1]
        adjusted_length_value = str(datetime.timedelta(seconds = int(adjusted_length_value)))

        with open(f"{current_path}map_value_length.txt", "w") as value:
            value.write(str(adjusted_length_value[2:]))
        
        rounded_bpm = float(map_bpm_list[int(selected_map) - 1])
        float(rounded_bpm)
        rounded_bpm = rounded_bpm * 1.0

        with open(f"{current_path}map_value_bpm.txt", "w") as value:
            value.write(str("%.0f" % rounded_bpm))

        with open(f"{current_path}map_value_ar.txt", "w") as value:
            value.write(map_ar_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_cs.txt", "w") as value:
            value.write(map_cs_list[int(selected_map) - 1])

        with open(f"{current_path}map_value_hp.txt", "w") as value:
            value.write(map_hp_list[int(selected_map) - 1])

def multi_btn():

    maps(selected_map.get())

    values(selected_map.get())

    #Runs each .osr based on script input rather than added manual input 
    if selected_map.get() != "None":

        os.chdir('F:\\World Cup\\2018 - Current Cup\\Scripts\\Resources\\Maps\\Showcase Replays')
        os.system(f'"F:\\World Cup\\2018 - Current Cup\\Scripts\\Resources\\Maps\\Showcase Replays\\{int(selected_map.get())}.osr"')

#Pulls all jpg images in <diffID>.jpg format from the full cover links in the .json
def image_btn():

    i = 0
    for count in range(0, map_amount - 1):
        if map_jpg_list[count - 1].endswith("jpg?0"):
            copyfile(f"{maps_path}replacement.png", f"{mappool_cards}{i + 1}.png")
        else:
            urllib.request.urlretrieve(map_jpg_list[count], f"{mappool_cards}{i + 1}.png")
        i += 1
    
    i = 0
    for count in range(0, map_amount - 1):
        basewidth = 940
        img = Image.open(f"{mappool_cards}{i + 1}.png")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(f"{mappool_cards}{i + 1}.png")
        i += 1

#map_amount = int(input("Mappool size?:\n"))

root = tk.Tk()
root.title("Showcase")
root.geometry("200x100")

map_list = ["None"]
map_diff_id_list = []
map_jpg_list = []
map_length_list = []
map_mod_list = []
map_bpm_list = []
map_ar_list = []
map_cs_list = []
map_hp_list = []

with open(f"{script_path}showcase.json") as file:
    showcase_data = json.load(file)

#Assigns all .json values to lists to later loop through
for maps_amount in showcase_data:
    map_list.append(maps_amount["map_number"])
    map_diff_id_list.append(maps_amount["diff_id"])
    map_jpg_list.append(maps_amount["mapset_jpg"])
    map_mod_list.append(maps_amount["mod"])
    map_length_list.append(maps_amount["length"])
    map_bpm_list.append(maps_amount["bpm"])
    map_ar_list.append(maps_amount["ar"])
    map_cs_list.append(maps_amount["cs"])
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

img_btn = tk.Button(root, text = "Images", command = image_btn)
img_btn.pack(side = tk.BOTTOM)

root.mainloop()