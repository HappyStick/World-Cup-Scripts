# Asks for user input of Country Names
country_red = raw_input("Red Country Name?: ")
country_blue = raw_input("Blue Country Name?: ")

def country_name():

    # Creates the country.txt files
    country_file_red = open("country_file_red.txt", "w+")
    country_file_blue = open("country_file_blue.txt", "w+")

    # Writes the user input into the above .txt
    country_file_red.write(country_red)
    country_file_blue.write(country_blue)

    # Closes the files
    country_file_red.close()
    country_file_blue.close()

def flag_location():

    # Sets source and destination vars for red and blue flag input
    source_red = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/" + country_red + ".png"
    destination_red = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/red_flag.png"

    source_blue = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/Flags/" + country_blue + ".png"
    destination_blue = "F:/World Cup/2018 - Mania 7K/Stream/Scripts/blue_flag.png"

    import shutil

    # Does the actual copying over
    shutil.copyfile(source_red, destination_red)
    shutil.copyfile(source_blue, destination_blue)

def player_list():

    # Adds user_input .txt into memory
    playerlist_red = file("F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/" + country_red + ".txt", "r")
    playerlist_blue = file("F:/World Cup/2018 - Mania 7K/Stream/Scripts/Country Players/" + country_blue + ".txt", "r")

    # Opens colour_player#.txt with the ability to write to it
    red_playername1 = open("red_player1.txt", "w+")
    red_playername2 = open("red_player2.txt", "w+")
    red_playername3 = open("red_player3.txt", "w+")
    red_playername4 = open("red_player4.txt", "w+")

    blue_playername1 = open("blue_player1.txt", "w+")
    blue_playername2 = open("blue_player2.txt", "w+")
    blue_playername3 = open("blue_player3.txt", "w+")
    blue_playername4 = open("blue_player4.txt", "w+")

    # Creates the colour_data variables containing the user_input values
    red_data = playerlist_red.readlines()
    blue_data = playerlist_blue.readlines()

    # Adds each line to an individual variable
    red_player1 = red_data[0]
    red_player2 = red_data[1]
    red_player3 = red_data[2]
    red_player4 = red_data[3]

    blue_player1 = blue_data[0]
    blue_player2 = blue_data[1]
    blue_player3 = blue_data[2]
    blue_player4 = blue_data[3]

    # Writes the value of each line into the colour_playername# using .write()
    red_playername1.write(red_player1)
    red_playername2.write(red_player2)
    red_playername3.write(red_player3)
    red_playername4.write(red_player4)

    blue_playername1.write(blue_player1)
    blue_playername2.write(blue_player2)
    blue_playername3.write(blue_player3)
    blue_playername4.write(blue_player4)

    # Closes all files
    playerlist_red.close()
    playerlist_blue.close()

    red_playername1.close()
    red_playername2.close()
    red_playername3.close()
    red_playername4.close()

    blue_playername1.close()
    blue_playername2.close()
    blue_playername3.close()
    blue_playername4.close()

country_name()
flag_location()
player_list()