import marshal
import os.path
import csv
import matplotlib.pyplot as plt
def fileopener(playerdictionary, filepath, name, season):
    with open(filepath, newline='') as csvfile:
        playerfile = csv.reader(csvfile, delimiter= ",", quotechar='|')
        for row in playerfile:
                stats = []
                if row[1] != "Inactive" and row[1] != "G" and row[1] != "Did Not Dress" and row[1]: 
                    z = round((int(row[1])), 1)
                else:
                    continue
                if name in playerdictionary:
                    seasondict = playerdictionary[name]
                    if season in seasondict:
                        gamedict = seasondict[season]
                        if z in gamedict:
                            gamedict[z] = stats
                        else:
                            gamedict.update({z:stats})      
                    else:
                        gamedict = {z:stats}
                        seasondict.update({season:gamedict})                               
                else:
                    gamedict = {z:stats}
                    seasondict = {season:gamedict}
                    playerdictionary.update({name:seasondict})
                if row[27] != "Inactive" and row[27] != "PTS" and row[27] != "Did Not Dress":
                    stats.append(int(row[27]))
                if row[21] != "Inactive" and row[21] != "TRB" and row[21] != "Did Not Dress":
                    stats.append(int(row[21]))
                if row[22] != "Inactive" and row[22] != "AST" and row[22] != "Did Not Dress":
                    stats.append(int(row[22]))
                if row[23] != "Inactive" and row[23] != "STL" and row[23] != "Did Not Dress":
                    stats.append(int(row[23]))
                if row[24] != "Inactive" and row[24] != "BLK" and row[24] != "Did Not Dress":
                    stats.append(int(row[24]))
def getstats(p, playerdict):
    seasondict = playerdict[p]
    l = input("Enter which season: ")
    if l.isdigit():
        l = int(l)
    else:
        print("Invalid response")
    gamedict = seasondict[l]
    q = [item[0] for item in gamedict.values()]
    r = [item[1] for item in gamedict.values()]
    s = [item[2] for item in gamedict.values()]
    t = [item[3] for item in gamedict.values()]
    k = [item[4] for item in gamedict.values()]
    print(str (round (sum(q) / len(q), 1)) + " PTS " + (str (round (sum(r) / len(r), 1)) + " REB " + (str (round (sum(s) / len(s), 1)) + " AST " + (str (round (sum(t) / len(t), 1)) + " STL " + (str (round (sum(k) / len(k), 1)) + " BLK")))))
def playerlist(nbafile):
    for key in playerdict.keys():
        print(key)
def nbafile(dictionary):
    y = input("Enter Player Name: ")
    f = input("Enter Season: ")
    if f.isdigit():
        f = int(f)
    else:
        print("Invalid response")
    z = input("Enter Game Number: ")
    if z.isdigit():
        z = int(z)
    else:
        print("Invalid response")
        z = 0
    stats = []
    if y in dictionary:
        seasondict = dictionary[y]
        if f in seasondict:
            gamedict = seasondict[f]
            if z in gamedict:
                gamedict[z] = stats
            else:
                gamedict.update({z:stats})      
        else:
            gamedict = {z:stats}
            seasondict.update({f:gamedict})                               
    else:
        gamedict = {z:stats}
        seasondict = {f:gamedict}
        dictionary.update({y:seasondict})                  
    a = input("Enter Points: ")
    if a.isdigit():
        a = int(a)
    else:
        print("Invalid response")
        a = 0
    stats.append(a)
    b = input("Enter Rebounds: ")
    if b.isdigit():
        b = int(b)
    else:
        print("Invalid response")
        b = 0
    stats.append(b)
    c = input("Enter Assists: ")
    if c.isdigit():
        c = int(c)
    else:
        print("Invalid response")
        c = 0
    stats.append(c)
    d = input("Enter Steals: ")
    if d.isdigit():
        d = int(d)
    else:
        print("Invalid response")
        d = 0
    stats.append(d)
    e = input("Enter Blocks: ")
    if e.isdigit():
        e = int(e)
    else:
        print("Invalid response")
        e = 0
    stats.append(e)
if os.path.isfile("nba.data"):
    u = open("nba.data", "rb")
    data = marshal.load(u)
    if data is None:
        playerdict = {}
    else:
        playerdict = data
    u.close()
else:
    playerdict = {}
while True:   
    choice = input("Would you like to edit, view, quit, stats, fileload, playerlist, or plot: ")
    if choice == "quit":
        file = open("nba.data", "wb")
        marshal.dump(playerdict, file)
        file.close()
        quit()
    elif choice == "view":
        print(playerdict)
    elif choice == "edit":
        nbafile(playerdict)
    elif choice == "stats":
        p = input("Enter player who you want stats from: ")
        getstats(p, playerdict)
    elif choice == "fileload":
        filepath = str("C:/Users/aniru/Documents/") + input("enter file path: ")
        name = input("enter player name: ")
        season = input("enter season: ")
        if season.isdigit():
            season = int(season)
        else:
            print("invalid response")
        fileopener(playerdict, filepath, name, season)
    elif choice == "playerlist":
        playerlist(nbafile)
    elif choice == "plot":
        playernames = input("whose points would you like to plot: ").split(', ')
        year = input("which season would you like to plot: ")
        for player in playernames:
            gamelist = playerdict[player][int(year)]
            game_number = []
            all_stats = []
            for key, value in gamelist.items():
                game_number.append(key)
                all_stats.append(value)
            points = [item[0] for item in all_stats]
            plt.plot(game_number, points, label = str(player) +'\'s stats in ' + str(year))
            plt.xlabel =('Game Number')
            plt.ylabel =('Points')
            plt.title(str(playernames) + '\'s stats')
            plt.legend()
        plt.show()    
    else:
        print("Invalid response")

  

