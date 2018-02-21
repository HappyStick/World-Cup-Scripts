import Tkinter as tk

def countryName(color, country):

    # Creates the country.txt files
    countryFile = open("country_file_" + color + ".txt", "w+")

    # Writes the user input into the above .txt
    countryFile.write(country)

    # Closes the file
    countryFile.close()

def flagLocation(color, country):

    # Sets source and destination vars for red and blue flag input
    flagSource = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/" + country + ".png"
    flagDestination = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/" + color + "_flag.png"

    import shutil

    # Does the actual copying over
    shutil.copyfile(flagSource, flagDestination)

def playerLists(color, country):

    # Adds user_input .txt into memory
    playerList = file("F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/" + country + ".txt", "r")

    # Reads the lines in the .txt and inputs it into var
    playerData = playerList.readlines()

    # For entries 0 - 3 creates player(number).txt reading one line from player_data at a time
    for number in range(4):
        player = playerData[number]

        playerName = open(color + "_player" + str(number + 1) + ".txt", "w+")

        playerName.write(player)

    # Closes the above
    playerList.close()

    playerName.close()

def runList(match):

    # Sets source and destination vars for selected match
    sourceMatch = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/Matches/" + match + ".png"
    destinationMatch = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/current_match.png"

    import shutil

    # Does the actual copying over
    shutil.copyfile(sourceMatch, destinationMatch)

# custom function to allow multiple functions in the button
def multiBtn():
    countryName("red", selectedCountry.get())
    countryName("blue", selectedCountry2.get())

    flagLocation("red", selectedCountry.get())
    flagLocation("blue", selectedCountry2.get())

    playerLists("red", selectedCountry.get())
    playerLists("blue", selectedCountry2.get())

    runList(selectedMatch.get())

root = tk.Tk()

# Create window
root.title("World Cup")
root.geometry('400x100')

# Creates a label called team 1 and formats it left
teamLabelRed = tk.Label(root, text='Team Red')
teamLabelRed.pack(side=tk.LEFT)

teamLabelBlue = tk.Label(root, text='Team Blue')
teamLabelBlue.pack(side=tk.RIGHT)

matchLabel = tk.Label(root, text='Match Number')
matchLabel.pack(side=tk.TOP)

countryList = ["Argentina", "Australia", "Brazil", "Canada", "Chile", "China", "France", "Germany", "Indonesia", "Italy", "Japan", "Malaysia", "Philippines", "Singapore", "South Korea", "United States"]
matchList = ["1", "2", "3", "4", "5", "6", "7", "8"]

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

# Create the button to run all of the above
runBtn = tk.Button(root, text="Run", command=multiBtn)
runBtn.pack(side=tk.BOTTOM)

root.mainloop()


