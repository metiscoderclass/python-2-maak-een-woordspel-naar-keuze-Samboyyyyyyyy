import random

def tekenGalg(fout_teller):
    if fout_teller == 13:
        print(" ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("--------")
    elif fout_teller == 12:
        print("")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 11:
        print("__________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 10:
        print("__________")
        print("       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 9:
        print("__________")
        print("|       |")
        print("|       0")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-------")
    elif fout_teller == 8:
        print("__________")
        print("|       |")
        print("|       0")
        print("|       +")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 7:
        print("__________")
        print("|       |")
        print("|       0")
        print("|      -+-")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 6:
        print("__________")
        print("|       |")
        print("|       0")
        print("|     /-+-}")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 5:
        print("__________")
        print("|       |")
        print("|       0)")
        print("|     /-+-}")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 4:
        print("__________")
        print("|       |")
        print("|       0")
        print("|     /-+-}")
        print("|       |")
        print("|      ---")
        print("|")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 3:
        print("__________")
        print("|       |")
        print("|       0")
        print("|     /-+-}")
        print("|       |")
        print("|      ---")
        print("|      | |")
        print("|")
        print("|")
        print("--------")
    elif fout_teller == 2:
        print("__________")
        print("|       |")
        print("|       0")
        print("|     /-+-}")
        print("|       |")
        print("|      ---")
        print("|      | |")
        print("|)     | |") 
        print("|")
        print("--------")
    elif fout_teller == 1:
        print("__________")
        print("|       |")
        print("|       0")
        print("|     /-+-}")
        print("|       |")
        print("|      ---")
        print("|      | |")
        print("|      | |") 
        print("|      / |")
        print("--------")
    elif fout_teller == 0:
        print("  _____")
        print(" /|||||\                                         ")
        print("| +   + |")
        print("|   o   |")
        print(" \_____/")
        print("")
        print("game over...")
        print("het woord was: "+ woord)
    else:
        print("")
        
al_gehad=str("")
goed_geraden=str("")
print("welkom bij:")
print("  ___    __    __    ___   ____  ____ ")
print(" / __)  /__\  |  |  / __) (_  _)( ___)")
print("( |_-. /(__)\  )(__( |_-..-_||   )__) ")
print(" \___/(__/\__)(____)\___/\____) (____)")
woord = random.choice([ "hek", "huis","bier","bot","man","mier","lol"])
fout_teller = int(14)
al_gehad = ""
while True:
    lengte = len(woord)
    print()
    print()
    
    letter = str(input("voer een letter in:"))
    if letter == "dev":
        print(woord)
    if letter == ":-)":
        print("0      +")
        print("  ---   |")
        print("0      /")
        print(woord)
    if letter in al_gehad:
        print("die letter heb je al gehad")
    if letter.isalpha() == False:
        print("alleen letters")
        fout_teller-=1
    else:
        if letter in woord:
            goed_geraden= goed_geraden+letter
        else:
            al_gehad = al_gehad+letter
    if letter in woord:
        print("hoera")
    else:
        print("fout")
        fout_teller -=1
    for l in woord:
        if l in goed_geraden:
            print(l, end="")
        else:
            print("_", end="")
    print("")
    tekenGalg(fout_teller)
    if fout_teller==0:
        break
    if letter == woord:
        print("JIJ HEBT GEWONNEN!!!!!!!!!")
        break
    if len(goed_geraden) == len(woord):
        print("JIJ HEBT GEWONNEN!!!!!!!!!")
        break
