import tkinter as tk
from tkinter import messagebox
import shutil
import os

scriptsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/'
flagsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/'
playersPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/'
matchesPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Matches/'
applicationsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Applications/'

def countryName(color, country):

    # Creates the country.txt files
    countryFile = open('{0}country_file_{1}.txt'.format(scriptsPath, color), 'w')

    # Writes the user input into the above .txt
    countryFile.write(country)

    # Closes the file
    countryFile.close()

def flagLocation(color, country):

    # Sets source and destination vars for red and blue flag input
    flagSource = '{0}{1}.png'.format(flagsPath, country)
    flagDestination = '{0}{1}_flag.png'.format(scriptsPath, color)

    # Does the actual copying over
    shutil.copyfile(flagSource, flagDestination)

def playerLists(color, country):

    # Adds user_input .txt into memory
    playerList = open('{0}{1}.txt'.format(playersPath, country), 'r')

    # Reads the lines in the .txt and inputs it into var
    playerData = playerList.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
    for number in range(4):
        # Ensures that if a country has less than 4 players it creates an empty .txt for each slot
        if number < len(playerData):
            player = playerData[number]

            playerName = open('{0}{1}_player{2}.txt'.format(scriptsPath, color, str(number + 1)), 'w+')

            playerName.write(player)
            
            playerName.close()
        else:
            emptyPlayer = open('{0}{1}_player{2}.txt'.format(scriptsPath, color, str(number + 1)), 'w+')

            emptyPlayer.write('')

            emptyPlayer.close()

    playerList.close()

def runList(match):

    # Sets source and destination vars for selected match
    sourceMatch = '{0}{1}.png'.format(matchesPath, match)
    destinationMatch = '{0}current_match.png'.format(scriptsPath)

    # Does the actual copying over
    shutil.copyfile(sourceMatch, destinationMatch)

def programsOpen():
    programs = [
      'obs64.lnk',
      'Snaz.lnk',
      'WCplaylist.lnk',
      'Overview.lnk',
      'SndVol.lnk',
      'osu!.lnk',
    ]
    
    try:
        for p in programs:
            os.startfile('{0}{1}'.format(applicationsPath, p))
    except FileNotFoundError as e:
        tk.messagebox.showerror("Error", "Program in list not found.\nError: {0}".format(e))
        

# custom function to allow multiple functions in the button
def multiBtn():

    countryName('red', selectedCountry.get())
    countryName('blue', selectedCountry2.get())

    flagLocation('red', selectedCountry.get())
    flagLocation('blue', selectedCountry2.get())

    playerLists('red', selectedCountry.get())
    playerLists('blue', selectedCountry2.get())

    runList(selectedMatch.get())

def openBtn():

    programsOpen()

root = tk.Tk()

# Create window
root.title("World Cup")
root.geometry('500x200')

# Creates a label called team 1 and formats it left
teamLabelRed = tk.Label(root, text='Team Red')
teamLabelRed.pack(side=tk.LEFT)

teamLabelBlue = tk.Label(root, text='Team Blue')
teamLabelBlue.pack(side=tk.RIGHT)

matchLabel = tk.Label(root, text='Match Number')
matchLabel.pack(side=tk.TOP)

countryList = ['Argentina', 'Australia', 'Brazil', 'Canada', 'Chile', 'China', 'France', 'Germany', 'Indonesia', 'Italy', 'Japan', 'Malaysia', 'Philippines', 'Singapore', 'South Korea', 'United States']
matchList = ['1', '2', '3', '4', '5', '6', '7', '8']

# Creates the var and initial selected variable in the list we're creating
selectedCountry = tk.StringVar()
selectedCountry.set(countryList[0])

selectedCountry2 = tk.StringVar()
selectedCountry2.set(countryList[0])

selectedMatch = tk.StringVar()
selectedMatch.set(matchList[0])

# Creates an optionmenu in below vars with root, selection and list
countryMenu = tk.OptionMenu(root, selectedCountry, *countryList)
countryMenu.pack(side=tk.LEFT)

countryMenu2 = tk.OptionMenu(root, selectedCountry2, *countryList)
countryMenu2.pack(side=tk.RIGHT)

matchMenu = tk.OptionMenu(root, selectedMatch, *matchList)
matchMenu.pack(side=tk.TOP)

# Create the button for opening programs
openBtn = tk.Button(root, text="Open Needed Applications", command=openBtn)
openBtn.pack(side=tk.BOTTOM)

# Create the button that runs most code
runBtn = tk.Button(root, text="Run", command=multiBtn)
runBtn.pack(side=tk.TOP)

root.mainloop()
