import random
import time
import os, platform
import pickle
import string

wepLongs = ["longsword","rusty longsword","silver longsword","bronze longsword","gold longsword","hard steel longsword","ancient longsword"]
wepShort = ["shortsword","rusty shortsword","silver shortsword","bronze shortsword","gold shortsword","hard steel shortsword","ancient shortsword"]

clear, passR = "cls" if platform.system() == "Windows" else "clear", False
os.system(clear)

alive = True
ltr = string.ascii_lowercase

towns = []
avbNames = []

def routineCheck():
    pass

def nameCreation():

    word = []
    for _ in range(random.randint(3,10)):
        word.append(random.choice(ltr))
    global avbNames
    avbNames.append("".join(word))


def title():

    global loaded, agl, mas, bra, gut, towns, worSize, ownName, race, loaded, year, day, month, tG

    print("Hoy there, buddy! Before we start the game and everything, you should check your savefiles! If you have any, you may want to load them by typing 'load'.\nIn case you don't you may want to make a new one. Type 'new'.")
    inTitle = input("Make your choice now. >> ")

    if inTitle == "wordmaker":
        while True:
            nameCreation()
            print(avbNames)
            input()

    if inTitle == "placeholder load":
        agl = 10
        mas = 20
        bra = 30
        gut = 40
        race = 3
        worSizeParam = 3
        worSize = 100 * worSizeParam
        ownName = "debug"
        year = 1
        month = 1
        day = 1
        new = "x"
        stage = 1

        loaded = True
        for tG in range(1, 5):
            nameCreation()
            selAvb = random.choice(avbNames)

            if 1 == 9:
                towns[f"settle_{tG}"] = {                            
                "name":selAvb,
                "pop":random.randint(3,50)*worSizeParam,
                "size":random.randint(30,60)*worSizeParam}
                
            towns.append[f"settle_{tG}"] = {                            
                "name":selAvb,
                "pop":random.randint(3,50)*worSizeParam,
                "size":random.randint(30,60)*worSizeParam}

    if inTitle == "new":

        print("Great choice buddy. Welcome to Saga of Rucw!")
        time.sleep(2)
        new = True

    if inTitle == "load":
        
        pass
        new = False

    if new == True:

        os.system(clear)

        print("\nNow you'll have to roll your character, and name em'.\nYou have 4 stats: Agility, Mass, Brains and Guts. These will be explained in detail later on, but now, let's start with Agility.\n\nThis one is rather obvious. It's how fast you are, how good you dodge and flee. Basically, you should start with 5-10 but if you want a challenge you can set it lower. Can't set it higher than 10 though.")
        inAglDec = input("Alright. Would you like it [random]ized? Or would you like to [set] it? >> ")
        if inAglDec == "random":
            while passR == False:        
                agl = random.randint(5,10)
                print("Your agility ==",agl,"\nDo you accept that? [Y/N] >> ",end="")
                inEmp1 = input("")
                if inEmp1.lower() == "n": 
                    print("Try again!")
                if inEmp1.lower() == "y": 
                    with open("player.dat","wb") as f:
                        pickle.dump([agl], f, protocol=2)
                    break

        if inAglDec == "set":
            while True:
                agl = input("Make your choice now. ")
                print("Your agility ==",agl,"\nDo you accept that? [Y/N] >> ",end="")
                inEmp2 = input("")
                if inEmp2.lower() == "n": 
                    print("Try again!")
                if inEmp2.lower() == "y": 
                    with open("player.dat","wb") as f:
                        pickle.dump([agl], f, protocol=2)
                    break

        time.sleep(2)
        os.system(clear)

        print("Next up is mass. This is basically your hp. If it's high, your healthpoints are higher, however, your ability to dodge will be lower (doesn't apply to fleeing though).")
        inMasDec = input("This one, it's recommended to be higher than 10 but lower than 20. Alright. Would you like it [random]ized? Or would you like to [set] it? >>")
        if inMasDec == "random":
            while True:
                mas = random.randint(10,20)
                maxHp = mas * 2
                print("Your mass ==",mas,"which means your hp is",maxHp,"\nDo you accept that? [Y/N] >>",end="")
                inEmp3 = input("")
                if inEmp3.lower() == "n":
                    print("Try again!")
                if inEmp3.lower() == "y":
                    with open("player.dat","wb") as f:
                        pickle.dump([mas, maxHp], f, protocol=2)
                    break

        if inMasDec == "set":
            while True:
                mas = int(input("Make your choice now. >> "))
                if not mas > 20:
                    maxHp = mas * 2
                    print("Your mass ==",mas,"which means your hp is",maxHp,"\nDo you accept that? [Y/N] >> ",end="")
                    inEmp4 = input("")
                    if inEmp4.lower() == "n": 
                        print("Try again!")
                    if inEmp4.lower() == "y": 
                        with open("player.dat","wb") as f:
                            pickle.dump([mas, maxHp], f, protocol=2)
                        break
                else:
                    print("Too high.")

        time.sleep(2)
        os.system(clear)

        print("The next is brains. Yet again, pretty straightforward, this is how smart you are. Being all smart and wise is surely great, but it can negatively affect your muscles.")
        inBraDec = input("For beginners, it can be kept under 30. Alright. Would you like it [random]ized? Or would you like to [set] it? >> ")
        if inBraDec.lower() == "random":
            while True:
                bra = random.randint(10,30)
                print("Your Brains is",bra,"\nDo you accept that? [Y/N] >> ",end="")
                inEmp5 = input("")
                if inEmp5.lower() == "y":
                    with open("player.dat","wb") as f:
                        pickle.dump([bra], f, protocol=2)
                    break
                if inEmp5.lower() == "n":
                    print("Try again!")
        if inBraDec.lower() == "set":
            while True:
                bra = int(input("Make you choice now. "))
                if not bra > 30:
                    print("Your Brains is",bra,"\nDo you accept that? [Y/N] >> ",end="")
                    inEmp6 = input("")
                    if inEmp6.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([bra], f, protocol=2)
                        break
                    if inEmp6.lower() == "n":
                        print("Try again!")
                else:
                    print("Too high!")

        time.sleep(2)
        os.system(clear)


        print("The last one is guts. It's best to keep this one balanced, as it's a high risk high reward kind of stat, but whatever pal.")
        inGutDec = input("It's best kept under 40. Alright. Would you like it [random]ized? Or would you like to [set] it? >> ")
        if inGutDec.lower() == "random":
            while True:
                gut = random.randint(10,40)
                print("Your Guts is",gut,"\nDo you accept that? [Y/N] >> ")
                inEmp7 = input("")
                if inEmp7.lower() == "y":
                    with open("player.dat","wb") as f:
                        pickle.dump([gut],f,protocol=2)
                    break
                if inEmp7.lower() == "n":
                    print("Try again!")
        if inGutDec.lower() == "set":
            while True:
                gut = int(input("Make your choice now. "))
                if not gut > 40:
                    print("Your guts is",gut,"\nDo you accept this? [Y/N] >> ")
                    inEmp8 = input("")
                    if inEmp8.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([gut],f,protocol=2)
                        break
                    if inEmp8.lower() == "n":
                        print("Try again!")
                else:
                    print("Too high!")

        time.sleep(2)
        os.system(clear)

        print("Now, you must pick a race for your character.\nThere are four races in total: Human, Elf, Ork and Goblin.\nIf you choose to be a human, you will have better brains.\nIf you choose to be an elf, you will have better agility.\nIf you choose to be an ork, you will have better mass.\nIf you choose to be a goblin, you will have better guts.")
        raceDec = input("You can either let the system pick one for you, or you can pick one yourself. >> ")
        if raceDec == "random":
            while True:
                race = random.randint(1,4)
                if race == 1:
                    print("You are an elf. Do you accept that? [Y/N] >> ")
                    inEmp9 = input(" ")
                    if inEmp9.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([race],f,protocol=2)
                        break
                    if inEmp9.lower() == "n":
                        print("Try again!")
                if race == 2:
                    print("You are an ork. Do you accept that? [Y/N] >> ")
                    inEmp9 = input(" ")
                    if inEmp9.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([race],f,protocol=2)
                        break
                    if inEmp9.lower() == "n":
                        print("Try again!")
                if race == 3:
                    print("You are a human. Do you accept that? [Y/N] >> ")
                    inEmp9 = input(" ")
                    if inEmp9.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([race],f,protocol=2)
                        break
                    if inEmp9.lower() == "n":
                        print("Try again!")
                if race == 4:
                    print("You are a goblin. Do you accept that? [Y/N] >> ")
                    inEmp9 = input(" ")
                    if inEmp9.lower() == "y":
                        with open("player.dat","wb") as f:
                            pickle.dump([race],f,protocol=2)
                        break
                    if inEmp9.lower() == "n":
                        print("Try again!")
        if raceDec == "set":
            while True:
                race = int(input("1 is Elf, 2 is Ork, 3 is Human, 4 is Goblin. Make your choice now. >> "))
                if race > 4 or race < 0:
                    print("That's not a valid race.")
                else:
                    if race == 1:
                        print("You are an elf. Do you accept that? [Y/N] >> ")
                        inEmp9 = input(" ")
                        if inEmp9.lower() == "y":
                            with open("player.dat","wb") as f:
                                pickle.dump([race],f,protocol=2)
                            break
                        if inEmp9.lower() == "n":
                            print("Try again!")
                    if race == 2:
                        print("You are an ork. Do you accept that? [Y/N] >> ")
                        inEmp9 = input(" ")
                        if inEmp9.lower() == "y":
                            with open("player.dat","wb") as f:
                                pickle.dump([race],f,protocol=2)
                            break
                        if inEmp9.lower() == "n":
                            print("Try again!")
                    if race == 3:
                        print("You are a human. Do you accept that? [Y/N] >> ")
                        inEmp9 = input(" ")
                        if inEmp9.lower() == "y":
                            with open("player.dat","wb") as f:
                                pickle.dump([race],f,protocol=2)
                            break
                        if inEmp9.lower() == "n":
                            print("Try again!")
                    if race == 4:
                        print("You are a goblin. Do you accept that? [Y/N] >> ")
                        inEmp9 = input(" ")
                        if inEmp9.lower() == "y":
                            with open("player.dat","wb") as f:
                                pickle.dump([race],f,protocol=2)
                            break
                        if inEmp9.lower() == "n":
                            print("Try again!")

        time.sleep(2)
        os.system(clear)

        print("Now you must name your character. Either that, or let the system generate a word for em'.")
        if input("Set or Random? ").lower() == "random":
            while True:
                nameCreation()
                selAvb = random.choice(avbNames)
                ownName = selAvb
                avbNames.remove(selAvb)
                print("You are called",ownName,"\nDo you accept that?")
                inEmp10 = input("")
                if inEmp10.lower() == "y":
                    with open("player.dat","wb") as f:
                        pickle.dump([ownName],f,protocol=2)
                    break
                if inEmp10.lower() == "n":
                    print("Try again!")
        if input("Set or Random? ").lower() == "set":
            while True:
                ownName = input("Your name: ")
                print("You are called",ownName,"\nDo you accept that?")
                inEmp10 = input("")
                if inEmp10.lower() == "y":
                    with open("player.dat","wb") as f:
                        pickle.dump([ownName],f,protocol=2)
                    break
                if inEmp10.lower() == "n":
                    print("Try again!")

        time.sleep(2)
        os.system(clear)

        print("Before we go on, I'll let you review your character!",
            "Their name is",ownName,
            "\n\nTheir race is ",end="")
        if race == 1:
            print("elf")
        if race == 2:
            print("ork")
        if race == 3:
            print("human")
        if race == 4:
            print("goblin")
        print("\nTheir agility is",agl,
            "\nTheir mass is",mas,
            "\nTheir brains is",bra,
            "\nTheir guts is",gut,
            "\n\nThis is your character.")
        input("Press any key to continue.")
                    
        race = race
        ownName = ownName
        agl = agl
        mas = mas
        bra = bra
        gut = gut
        
        time.sleep(2)
        os.system(clear)

        print("Now, you'll have to create the world. It won't be hard, trust me.\nFirst of all, you should set the world size. This goes from 1 to 5.")
        if input("Random / Set. >> ").lower() == "set":
            while True:
                worSizeParam = int(input("1 - 5: "))
                if worSizeParam > 5 or worSizeParam < 1:
                    print("Incorrect. Try again.")
                else:
                    worSizeParam = worSizeParam
                    print("The world size is",worSizeParam,"\nDo you accept that? [Y/N] >> ",end="")
                    if input("").lower() == "y":
                        worSize = random.randint(95,115) * worSizeParam
                        break
                    if input("").lower() == "n":
                        print("Try again!")
        if input("Random / Set. >> ").lower() == "random":
            while True:
                worSizeParam = random.randint(1,5)
                print("The world size is",worSizeParam,"\nDo you accept that? [Y/N] >>",end="")  
                if input("").lower() == "y":
                    worSize = random.randint(95,115) * worSizeParam
                    break
                if input("").lower() == "n":
                    print("Try again!")

        time.sleep(2)
        os.system(clear)

        print("Now, you should set the number of settlements. The minimum number is 5, max is 10.")
        
        if input("Random / Set. >> ").lower == "random":
            while True:
                setsInt = random.randint(5,10)
                for tG in range(1, setsInt):
                    nameCreation()
                    selAvb = random.choice(avbNames)
                    towns[f"settle_{tG}"] = {                            
                        "name":selAvb,
                        "pop":random.randint(3,50)*worSizeParam,
                        "size":random.randint(30,60)*worSizeParam}
                    avbNames.remove(selAvb)

        if input("Random / Set. >> ").lower == "set":
                setsInt = random.randint(5,10)
                for _ in range(setsInt):
                    nameCreation()
                    selAvb = random.choice(avbNames)
                    towns[f"settle_{tG}"] = {                            
                        "name":selAvb,
                        "pop":random.randint(3,50)*worSizeParam,
                        "size":random.randint(30,60)*worSizeParam}
                    avbNames.remove(selAvb)

        towns = towns
        worSize = worSize
        with open("world.dat","wb") as f:
            pickle.dump([towns,worSize],f,protocol = 2)
        print("Before we end the world generation, you should review your world.\nYour world size is",worSizeParam,"\nThe number of settlements is",len(towns))
        input("Press any key...")

        time.sleep(2)
        os.system(clear)

        print("Saving some more objects...")
        year, month, day = 1, random.randint(1,12), random.randint(1,29)
        stage = 1
        with open("world.dat","wb") as f:
            pickle.dump([year, month, day, stage],f,protocol=2)
        print("You should be ready with the preparations. To start the game, exit this window, open the game again, and load the file.")


    elif new == False:
        print("Loading your player data...")
        if not os.path.isfile("./player.dat") == True:
            print("Can't find file! Quitting in 3 secs.")
            time.sleep(3)
            quit()
        else:
            print("File found!")
            with open("player.dat","rb") as f:
                agl, mas, bra, gut, race, ownName, year, month, day, stage, towns, worSize = pickle.load(f)

        if not os.path.isfile("./world.dat") == True:
            print("Can't find file! Quitting in 3 secs.")
            time.sleep(3)
            quit()
        else:
            print("File found!")
            with open("world.dat","rb") as f:
                towns, worSize = pickle.load(f)
            
        input("Press any key to load this file.")
        loaded = True

def newGameLoader():

    global curTown, clock, location
    try:
        location = random.choice(towns)
    except KeyError:
        print("No key")
    #startTown = startTown["name"]
    clock = 8

def printDate():
    global year, month, day


    if month == 1:
        print("Jan.",end=" ")
    if month == 2:
        print("Feb.",end=" ")
    if month == 3:
        print("Mar.",end=" ")
    if month == 4:
        print("Apr.",end=" ")
    if month == 5:
        print("May.",end=" ")
    if month == 6:
        print("Jun.",end=" ")
    if month == 7:
        print("Jul.",end=" ")
    if month == 8:
        print("Aug.",end=" ")
    if month == 9:
        print("Sep.",end=" ")
    if month == 10:
        print("Oct.",end=" ")
    if month == 11:
        print("Nov.",end=" ")
    if month == 12:
        print("Dec.",end=" ")
    print(day,sep=". ",end="")

    weather = random.randint(1,5)

    print(" @ ",clock,":00",sep="")

    if weather == 1:
        print("The sky is clear.")
    if weather == 2:
        print("The sun is bright.")
    if weather == 3:
        print("The sky is cloudy.")
    if weather == 4:
        print("It's raining.")
    if weather == 5:
        print("It's foggy.")

    print(towns)

def task():


    os.system(clear)

    global location

    location = location
    curTName = location["name"]
    curTPop = location["pop"]

    global day, month, year
    while alive == True:
        day = day + 1
        if day >= 31:
            day = 1
            month += 1
        if month >= 13:
            month = 1
            year += 1
        printDate()
        hand = input("")
        if hand == "":
            nValue = True
            print("asd" if nValue == False else "",end="")
        if hand == "self":
            print("You are",ownName)
            try:
                print("\nYou are currently residing in",curTName,"a town with",curTPop,"residents.\n")
            except KeyError:
                print("The program could not retrieve your town.")
            print("Your agility is",agl,"\nYour mass is",mas,"\nYour brains is",bra,"\nYour guts is",gut)

        else:
            print("That's incorrect.")


if __name__ == "__main__":
    
    #year, month, day = title.year, title.month, title.day


    title()
    

    if loaded == True:
        
        newGameLoader()
        task()
