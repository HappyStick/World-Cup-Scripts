import tkinter as tk
import math
import json

from shutil import copyfile

script_path = "F:/World Cup/2018 - Taiko/Scripts/"
flags_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Flags/"
players_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Country Players/"
rounds_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Round Name Files/"
matches_path = "F:/World Cup/2018 - Taiko/Scripts/Matches/"
current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"

def country_name(color, country, country_short):

    # Creates the country.txt files, writes user input into the .txt and closes it
    with open(f"{current_path}country_file_{color}.txt", "w") as country_file:
        country_file.write(country)
    with open(f"{current_path}country_file_{color}_short.txt", "w") as country_file_short:
        country_file_short.write(country_short)

def flag_location(color, country):

    # Sets source and destination vars for red and blue flag input and copies it over
    copyfile(f"{flags_path}{country}.png", f"{current_path}{color}_flag.png")

def player_lists(color, country):

    # Adds user_input .txt into memory then reads the lines in the .txt and inputs it into var
    player_list = open((f"{players_path}{country}.txt"), "r")
    player_data = player_list.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
    for number in range(5):
        # Ensures that if a country has less than 4 players it creates an empty .txt for each slot
        if number < len(player_data):
            player = player_data[number]

            with open(f"{current_path}{color}_player{str(number + 1)}.txt", "w+") as player_name:
                player_name.write(player)
        else:
            with open(f"{current_path}{color}_player{str(number + 1)}.txt", "w+") as empty_name:
                empty_name.write("")

    player_list.close()

# Writes the match time in matchTime.txt
def match_times(month, day, time):

    with open(f"{current_path}match_time.txt", "w") as match_file:
        match_file.write(f"{day} {month} {time} UTC")
    with open(f"{current_path}match_time_short.txt", "w") as match_time:
        match_time.write(f"{time} UTC")

def round_names(round_name):

    copyfile(f"{rounds_path}{round_name}.png", f"{current_path}current_round.png")
    copyfile(f"{rounds_path}intro {round_name}.png", f"{current_path}current_round_intro.png")

# Allows multiple functions in the button
def multi_btn():

    country_name("red", selected_country.get(), selected_country_short.get())
    country_name("blue", selected_country2.get(), selected_country_short2.get())

    flag_location("red", selected_country.get())
    flag_location("blue", selected_country2.get())

    player_lists("red", selected_country.get())
    player_lists("blue", selected_country2.get())

    match_times(selected_month.get(), str(selected_day.get()), selected_time.get())

    round_names(selected_round.get())

root = tk.Tk()

# Create window
root.title("World Cup")
root.geometry("450x200")

country_list = []
country_list_short = []
month_list = []
day_list = range(1, 32)
round_list = []

with open(f"{script_path}countries.json") as file:
    country_data = json.load(file)

with open(f"{script_path}months.json") as file:
    month_data = json.load(file)

with open(f"{script_path}rounds.json") as file:
    round_data = json.load(file)

for countries in country_data["countries"]:
    country_list.append(countries["full_name"])

for countries in country_data["countries"]:
    country_list_short.append(countries["abbreviation"])

for months in month_data["months"]:
    month_list.append(months)

for rounds in round_data["rounds"]:
    round_list.append(rounds)

# Creates the var and initial selected variable in the list we're creating
selected_country = tk.StringVar()
selected_country.set(country_list[0])

selected_country_short = tk.StringVar()
selected_country_short.set(country_list_short[0])

selected_country2 = tk.StringVar()
selected_country2.set(country_list[0])

selected_country_short2 = tk.StringVar()
selected_country_short2.set(country_list_short[0])

selected_month = tk.StringVar()
selected_month.set(month_list[0])

selected_day = tk.StringVar()
selected_day.set(day_list[0])

selected_time = tk.StringVar()
selected_time.set("00:00")

selected_round = tk.StringVar()
selected_round.set(round_list[0])

# Creates an optionmenu in below vars with root, selection and list
country_menu = tk.OptionMenu(root, selected_country, *country_list)
country_menu.pack(side = tk.LEFT)

country_menu2 = tk.OptionMenu(root, selected_country2, *country_list)
country_menu2.pack(side = tk.RIGHT)

country_menu_short = tk.OptionMenu(root, selected_country_short, *country_list_short)
country_menu_short.pack(side = tk.LEFT)

country_menu_short2 = tk.OptionMenu(root, selected_country_short2, *country_list_short)
country_menu_short2.pack(side = tk.RIGHT)

month_menu = tk.OptionMenu(root, selected_month, *month_list)
month_menu.pack(side = tk.TOP)

day_menu = tk.OptionMenu(root, selected_day, *day_list)
day_menu.pack(side = tk.TOP)

time_menu = tk.Entry(root, textvariable = selected_time, width = "5")
time_menu.pack(side = tk.TOP)

round_input = tk.OptionMenu(root, selected_round, *round_list)
round_input.pack(side = tk.TOP)

run_btn = tk.Button(root, text = "Run", command = multi_btn)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()