import tkinter as tk
import shutil
import math
import json

scripts_path = "F:/World Cup/2018 - Taiko/Scripts/"
flags_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Flags/"
players_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Country Players/"
rounds_path = "F:/World Cup/2018 - Taiko/Scripts/Resources/Round Name Files/"
matches_path = "F:/World Cup/2018 - Taiko/Scripts/Matches/"
current_path = "F:/World Cup/2018 - Taiko/Scripts/OBS Output/Current Files/"

def country_name(color, country):

    # Creates the country.txt files, writes user input into the .txt and closes it
    country_file = open((f"{current_path}country_file_{color}.txt"), "w")
    country_file.write(country)
    country_file.close()

def flag_location(color, country):

    # Sets source and destination vars for red and blue flag input and copies it over
    flag_source = (f"{flags_path}{country}.png")
    flag_destination = (f"{current_path}{color}_flag.png")
    shutil.copyfile(flag_source, flag_destination)

def player_lists(color, country):

    # Adds user_input .txt into memory then reads the lines in the .txt and inputs it into var
    player_list = open((f"{players_path}{country}.txt"), "r")
    player_data = player_list.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
    for number in range(4):
        # Ensures that if a country has less than 4 players it creates an empty .txt for each slot
        if number < len(player_data):
            player = player_data[number]

            player_name = open((f"{current_path}{color}_player{str(number + 1)}.txt"), "w+")

            player_name.write(player)
            
            player_name.close()
        else:
            empty_player = open((f"{current_path}{color}_player{str(number + 1)}.txt"), "w+")

            empty_player.write("")

            empty_player.close()

    player_list.close()

# Writes the match time in matchTime.txt
def match_times(month, day, time):

    match_file = open((f"{current_path}match_time.txt"), "w")
    match_file.write((f"{day} {month} {time} UTC"))
    match_file.close()

def round_names(round_name):

    round_source = (f"{rounds_path}{round_name}.png")
    round_destination = (f"{current_path}current_round.png")
    shutil.copyfile(round_source, round_destination)

    intro_round_source = (f"{rounds_path}intro {round_name}.png")
    intro_round_destination = (f"{current_path}current_round_intro.png")
    shutil.copyfile(intro_round_source, intro_round_destination)

def check_box(check_box):

    if check_box == 0:
        
        warmup_trans_source = (f"{rounds_path}wu trans.png")
        warmup_trans_destination = (f"{current_path}warmup.png")
        shutil.copyfile(warmup_trans_source, warmup_trans_destination)

    elif check_box == 1:

        warmup_source = (f"{rounds_path}wu.png")
        warmup_destination = (f"{current_path}warmup.png")
        shutil.copyfile(warmup_source, warmup_destination)

# Allows multiple functions in the button
def multi_btn():

    country_name("red", selected_country.get())
    country_name("blue", selected_country2.get())

    flag_location("red", selected_country.get())
    flag_location("blue", selected_country2.get())

    player_lists("red", selected_country.get())
    player_lists("blue", selected_country2.get())

    match_times(selected_month.get(), str(selected_day.get()), selected_time.get())

    round_names(selected_round.get())

    check_box(checkbox_select.get())

root = tk.Tk()

# Create window
root.title("World Cup")
root.geometry("500x200")

# Creates a label called team 1 and formats it left
team_label_red = tk.Label(root, text="Team Red")
team_label_red.pack(side=tk.LEFT)

team_label_blue = tk.Label(root, text="Team Blue")
team_label_blue.pack(side=tk.RIGHT)

country_list = []
month_list = []
day_list = range(1, 32)
round_list = []
checkbox_state = False

with open(f"{scripts_path}countries.json") as file:
    country_data = json.load(file)

with open(f"{scripts_path}months.json") as file:
    month_data = json.load(file)

with open(f"{scripts_path}rounds.json") as file:
    round_data = json.load(file)

for countries in country_data["countries"]:
    country_list.append(countries["abbreviation"])

for months in month_data["months"]:
    month_list.append(months)

for rounds in round_data["rounds"]:
    round_list.append(rounds)

# Creates the var and initial selected variable in the list we"re creating
selected_country = tk.StringVar()
selected_country.set(country_list[0])

selected_country2 = tk.StringVar()
selected_country2.set(country_list[0])

selected_month = tk.StringVar()
selected_month.set(month_list[0])

selected_day = tk.StringVar()
selected_day.set(day_list[0])

selected_time = tk.StringVar()
selected_time.set("00:00")

selected_round = tk.StringVar()
selected_round.set(round_list[0])

checkbox_select = tk.IntVar()
checkbox_select.set(checkbox_state)

# Creates an optionmenu in below vars with root, selection and list
country_menu = tk.OptionMenu(root, selected_country, *country_list)
country_menu.pack(side = tk.LEFT)

country_menu2 = tk.OptionMenu(root, selected_country2, *country_list)
country_menu2.pack(side = tk.RIGHT)

month_menu = tk.OptionMenu(root, selected_month, *month_list)
month_menu.pack(side = tk.TOP)

day_menu = tk.OptionMenu(root, selected_day, *day_list)
day_menu.pack(side = tk.TOP)

time_menu = tk.Entry(root, textvariable = selected_time, width = "5")
time_menu.pack(side = tk.TOP)

round_input = tk.OptionMenu(root, selected_round, *round_list)
round_input.pack(side = tk.TOP)

checkbox_input = tk.Checkbutton(root, text = "Warmup", variable = checkbox_select)
checkbox_input.pack(side = tk.TOP)

run_btn = tk.Button(root, text = "Run", command = multi_btn)
run_btn.pack(side = tk.BOTTOM)

root.mainloop()