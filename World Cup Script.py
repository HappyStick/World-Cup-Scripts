import tkinter as tk
import shutil

scriptsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/'
flagsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/'
playersPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/'
matchesPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Matches/'
applicationsPath = 'F:/World Cup/2018 - Mania 7K/Stream/Scripts/Applications/'


def countryName(color, country):

    # Creates the country.txt files
    countryFile = open((f'{scriptsPath}country_file_{color}.txt'), 'w')

    # Writes the user input into the above .txt
    countryFile.write(country)

    # Closes the file
    countryFile.close()


<<<<<<< HEAD
def flagLocation(color, country):

    # Sets source and destination vars for red and blue flag input and copies
    # it over
=======
    # Sets source and destination vars for red and blue flag input and copies it over
>>>>>>> upstream/master
    flagSource = (f'{flagsPath}{country}.png')
    flagDestination = (f'{scriptsPath}{color}_flag.png')
    shutil.copyfile(flagSource, flagDestination)


<<<<<<< HEAD
def playerLists(color, country):

    # Adds user_input .txt into memory then reads the lines in the .txt and
    # inputs it into var
=======
    # Adds user_input .txt into memory then reads the lines in the .txt and inputs it into var
>>>>>>> upstream/master
    playerList = open((f'{playersPath}{country}.txt'), 'r')
    playerData = playerList.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from
    # player_data at a time
    for number in range(4):
        # Ensures that if a country has less than 4 players it creates an empty
        # .txt for each slot
        if number < len(playerData):
            player = playerData[number]

<<<<<<< HEAD
            playerName = open(
                (f'{scriptsPath}{color}_player{str(number + 1)}.txt'),
                'w+'
            )
=======
            playerName = open((f'{scriptsPath}{color}_player{str(number + 1)}.txt'), 'w+')
>>>>>>> upstream/master

            playerName.write(player)

            playerName.close()
        else:
<<<<<<< HEAD
            emptyPlayer = open(
                (f'{scriptsPath}{color}_player{str(number + 1)}.txt'),
                'w+'
            )
=======
            emptyPlayer = open((f'{scriptsPath}{color}_player{str(number + 1)}.txt'), 'w+')
>>>>>>> upstream/master

            emptyPlayer.write('')

            emptyPlayer.close()

    playerList.close()


<<<<<<< HEAD
def runList(match):

=======
>>>>>>> upstream/master
    # Sets source and destination vars for selected match and copies it over
    sourceMatch = (f'{matchesPath}{match}.png')
    destinationMatch = (f'{scriptsPath}current_match.png')
    shutil.copyfile(sourceMatch, destinationMatch)

<<<<<<< HEAD

=======
>>>>>>> upstream/master
# custom function to allow multiple functions in the button
def multiBtn():
    # Countries
    countryName('red', selectedCountry.get())
    countryName('blue', selectedCountry2.get())
    # Flags
    flagLocation('red', selectedCountry.get())
    flagLocation('blue', selectedCountry2.get())
    # Players
    playerLists('red', selectedCountry.get())
    playerLists('blue', selectedCountry2.get())

    runList(selectedMatch.get())

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

<<<<<<< HEAD
countryList = [
    'Argentina',
    'Australia',
    'Brazil',
    'Canada',
    'Chile',
    'China',
    'France',
    'Germany',
    'Indonesia',
    'Italy',
    'Japan',
    'Malaysia',
    'Philippines',
    'Singapore',
    'South Korea',
    'United States'
]
=======
countryList = ['Argentina', 'Australia', 'Brazil', 'Canada', 'Chile', 'China', 'France', 'Germany', 'Indonesia', 'Italy', 'Japan', 'Malaysia', 'Philippines', 'Singapore', 'South Korea', 'United States']
>>>>>>> upstream/master
matchList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

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

# Create the button that runs most code
runBtn = tk.Button(root, text="Run", command=multiBtn)
runBtn.pack(side=tk.TOP)

root.mainloop()
