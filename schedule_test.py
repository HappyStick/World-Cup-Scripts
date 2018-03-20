import tkinter as tk

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

    match_time_text = open(f'{schedule_output_path}{matches.number}_time.txt', 'w')
    match_time_text.write(f'{matches.match_time} UTC')
    match_time_text.close()


# Creates var count instances of frames with Match #, Team 1 and 2
def frames(count):

    frame = tk.Frame(root)
    frame.pack()

    match_label = tk.Label(frame, text = f'Match {frame_count}')
    match_label.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2], *country_list)
    country_menu.pack(side = tk.LEFT)

    country_menu = tk.OptionMenu(frame, selected_country_list[count * 2 + 1], *country_list)
    country_menu.pack(side = tk.RIGHT)

# Runs code after new inputs are filled in
def run_button():

    frame_count = 0

    for count in range(0,12):

        frame_count = frame_count + 1

        matches = match(f'{frame_count}', selected_country_list[count * 2].get(), selected_country_list[count * 2 + 1].get(), '08:00')

        schedule(matches)

country_list = ['None', 'USA', 'AUS', 'CHN', 'KOR']

root = tk.Tk()

root.title('OBS Schedule Tool')
root.geometry('500x500')

selected_country_list = []

# Creates 24 iterations of selected_country to be used by frames() at initial runtime
for numbers in range(0,24):

    selected_country = tk.StringVar()
    selected_country.set(country_list[0])
    selected_country_list.append(selected_country)

run_button = tk.Button(root, text = "Run", command = run_button)
run_button.pack(side = tk.BOTTOM)

# Creates frame count for frames()
frame_count = 0

for count in range(0,12):

    frame_count = frame_count + 1
    frames(count)

root.mainloop()


