import tkinter as tk
import shutil
import math

scriptsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/'
flagsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/'
playersPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/'
matchesPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Matches/'
applicationsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Applications/'

def countryName(color, country):

    # Creates the country.txt files, writes user input into the .txt and closes it
    countryFile = open((f'{scriptsPath}country_file_{color}.txt'), 'w')
    countryFile.write(country)
    countryFile.close()

def flagLocation(color, country):

    # Sets source and destination vars for red and blue flag input and copies it over
    flagSource = (f'{flagsPath}{country}.png')
    flagDestination = (f'{scriptsPath}{color}_flag.png')
    shutil.copyfile(flagSource, flagDestination)

def playerLists(color, country):

    # Adds user_input .txt into memory then reads the lines in the .txt and inputs it into var
    playerList = open((f'{playersPath}{country}.txt'), 'r')
    playerData = playerList.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
    for number in range(4):
        # Ensures that if a country has less than 4 players it creates an empty .txt for each slot
        if number < len(playerData):
            player = playerData[number]

            playerName = open((f'{scriptsPath}{color}_player{str(number + 1)}.txt'), 'w+')

            playerName.write(player)
            
            playerName.close()
        else:
            emptyPlayer = open((f'{scriptsPath}{color}_player{str(number + 1)}.txt'), 'w+')

            emptyPlayer.write('')

            emptyPlayer.close()

    playerList.close()

def matchTimes(month, day, time):

    matchFile = open((f'{scriptsPath}matchTime.txt'), 'w')
    matchFile.write((f'{day} {month} {time} UTC'))
    matchFile.close()

# custom function to allow multiple functions in the button
def multiBtn():

    countryName('red', selectedCountry.get())
    countryName('blue', selectedCountry2.get())

    flagLocation('red', selectedCountry.get())
    flagLocation('blue', selectedCountry2.get())

    playerLists('red', selectedCountry.get())
    playerLists('blue', selectedCountry2.get())

    matchTimes(selectedMonth.get(), str(selectedDay.get()), selectedTime.get())

root = tk.Tk()

# Create window
root.title("World Cup")
root.geometry('500x200')

# Creates a label called team 1 and formats it left
teamLabelRed = tk.Label(root, text='Team Red')
teamLabelRed.pack(side=tk.LEFT)

teamLabelBlue = tk.Label(root, text='Team Blue')
teamLabelBlue.pack(side=tk.RIGHT)

countryList = ['Argentina', 'Australia', 'Brazil', 'Canada', 'Chile', 'China', 'France', 'Germany', 'Indonesia', 'Italy', 'Japan', 'Malaysia', 'Philippines', 'Singapore', 'South Korea', 'United States']
monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dayList = range(1, 32)
timeList = []
for number in range(0, 48):
    hours = math.floor(number/2)
    mins = number % 2
    timeList.append(f'{hours:02}:{mins*30:02}')

# Creates the var and initial selected variable in the list we're creating
selectedCountry = tk.StringVar()
selectedCountry.set(countryList[0])

selectedCountry2 = tk.StringVar()
selectedCountry2.set(countryList[0])

selectedMonth = tk.StringVar()
selectedMonth.set(monthList[0])

selectedDay = tk.StringVar()
selectedDay.set(dayList[0])

selectedTime = tk.StringVar()
selectedTime.set(timeList[0])

# Creates an optionmenu in below vars with root, selection and list
countryMenu = tk.OptionMenu(root, selectedCountry, *countryList)
countryMenu.pack(side=tk.LEFT)

countryMenu2 = tk.OptionMenu(root, selectedCountry2, *countryList)
countryMenu2.pack(side=tk.RIGHT)

monthMenu = tk.OptionMenu(root, selectedMonth, *monthList)
monthMenu.pack(side=tk.TOP)

dayMenu = tk.OptionMenu(root, selectedDay, *dayList)
dayMenu.pack(side=tk.TOP)

timeMenu = tk.OptionMenu(root, selectedTime, *timeList)
timeMenu.pack(side=tk.TOP)

# Create the button that runs most code
runBtn = tk.Button(root, text="Run", command=multiBtn)
runBtn.pack(side=tk.BOTTOM)

root.mainloop()