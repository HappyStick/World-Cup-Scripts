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
def schedule(match):

    copyfile(f'{flags_path}{match.team_1}.png', f'{schedule_output_path}{match.number}_flag_1.png')
    copyfile(f'{flags_path}{match.team_2}.png', f'{schedule_output_path}{match.number}_flag_2.png')

    match_time_text = open(f'{schedule_output_path}{match.number}_time.txt', 'w')
    match_time_text.write(f'{match.match_time} UTC')
    match_time_text.close()

def run_button():

    match_1 = match('1', selected_country_1.get(), selected_country_2.get() , '08:00')
    match_2 = match('2', selected_country_3.get(), selected_country_4.get() , '10:00')
    
    schedule(match_1)
    schedule(match_2)

country_list = ['None', 'USA', 'AUS', 'CHN', 'KOR']

root = tk.Tk()

root.title('OBS Schedule Tool')
root.geometry('500x500')

selected_country_1 = tk.StringVar()
selected_country_1.set(country_list[0])

selected_country_2 = tk.StringVar()
selected_country_2.set(country_list[0])

selected_country_3 = tk.StringVar()
selected_country_3.set(country_list[0])

selected_country_4 = tk.StringVar()
selected_country_4.set(country_list[0])

frame_1 = tk.Frame(root)
frame_1.pack()

match_label_1 = tk.Label(frame_1, text = 'Match 1')
match_label_1.pack(side = tk.LEFT)

country_menu_1 = tk.OptionMenu(frame_1, selected_country_1, *country_list)
country_menu_1.pack(side = tk.LEFT)

country_menu_2 = tk.OptionMenu(frame_1, selected_country_2, *country_list)
country_menu_2.pack(side = tk.RIGHT)

frame_2 = tk.Frame(root)
frame_2.pack()

match_label_2 = tk.Label(frame_2, text = 'Match 2')
match_label_2.pack(side = tk.LEFT)

country_menu_3 = tk.OptionMenu(frame_2, selected_country_3, *country_list)
country_menu_3.pack(side = tk.LEFT)

country_menu_4 = tk.OptionMenu(frame_2, selected_country_4, *country_list)
country_menu_4.pack(side = tk.RIGHT)

run_button = tk.Button(root, text = "Run", command = run_button)
run_button.pack(side = tk.BOTTOM)

root.mainloop()


