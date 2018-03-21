import tkinter as tk
import json

from shutil import copyfile

flags_path = 'F:/World Cup/2018 - Taiko/Scripts/Flags/'
schedule_output_path = 'F:/World Cup/2018 - Taiko/Scripts/OBS Output/Schedule Files/'
script_path = 'F:/World Cup/2018 - Taiko/Scripts/'

# Each match class instance is assigned a match number, team names and time
class match:

    def __init__(self, number, team_1, team_2, match_time):

        self.number = number
        self.team_1 = team_1
        self.team_2 = team_2
        self.match_time = match_time

# Copies over the flags and outputs time into .txt
def schedule(matches):

    copyfile(f'{flags_path}{matches.team_1}.png', f'{schedule_output_path}{matches.number}_flag_1.png')
    copyfile(f'{flags_path}{matches.team_2}.png', f'{schedule_output_path}{matches.number}_flag_2.png')

    with open(f'{schedule_output_path}{matches.number}_time.txt', 'w') as match_time_text:
        match_time_text.write(f'{matches.match_time} UTC')

# Creates var count instances of frames with Match #, Team 1 / 2 and time
def frames(count):

    frame = tk.Frame(root)
    frame.pack()

    match_label = tk.Label(frame, text = f'Match {frame_count}')
    match_label.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2], *country_list)
    country_menu.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2 + 1], *country_list)
    country_menu.pack(side = tk.LEFT)

    time_box = tk.Entry(frame, textvariable = time_input_list[count], width = '5')
    time_box.pack(side = tk.RIGHT)

def save_button():

    frame_count = 0

    country_1 = []
    country_2 = []
    time_1 = []

    for count in range(0, match_amount):

        frame_count = frame_count + 1

        country_1.append(selected_country_list[count * 2].get())
        country_2.append(selected_country_list[count * 2 + 1].get())
        time_1.append(time_input_list[count].get())

    saved_vars = {"saved_vars" : [{"team_1" : country_1}, {"team_2" : country_2}, {"time" : time_1}]}
    
    with open(f'{script_path}savefile.json', 'w') as file:
        json.dump(saved_vars, file, indent = 4)

# Runs code after new inputs are filled in
def run_button():

    frame_count = 0

    for count in range(0, match_amount):

        frame_count = frame_count + 1

        matches = match(f'{frame_count}', selected_country_list[count * 2].get(), selected_country_list[count * 2 + 1].get(), time_input_list[count].get())

        schedule(matches)

root = tk.Tk()

root.title('OBS Schedule Tool')
root.geometry('500x500')

#creates country_list based on schedule.json
with open(f'{script_path}countries.json') as file:
    country_data = json.load(file)

country_list = []
for countries in country_data['countries']:
    country_list.append(countries['abbreviation'])
time_list = ['00:00']

selected_country_list = []
time_input_list = []

match_amount = int(input('Match count?:\n'))

with open(f'{script_path}savefile.json') as file:
    savedata = json.load(file)

# Creates 12 iterations of time_input to be used by frames() at initial runtime
for numbers in range(0, match_amount):

    time_input = tk.StringVar()
    time_input.set(time_list[0])
    time_input_list.append(time_input)

# Creates 24 iterations of selected_country to be used by frames() at initial runtime
for numbers in range(0, match_amount * 2):

    selected_country = tk.StringVar()
    selected_country.set(country_list[0])
    selected_country_list.append(selected_country)

# Creates frame count for frames()
frame_count = 0

for count in range(0, match_amount):

    frame_count = frame_count + 1
    frames(count)

run_btn = tk.Button(root, text = 'Run', command = run_button)
run_btn.pack(side = tk.BOTTOM)

save_btn = tk.Button(root, text = 'Save', command = save_button)
save_btn.pack(side = tk.BOTTOM)

root.mainloop()

