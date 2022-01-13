import random
from hangman_ord import ord_lista
import turtle
import pyfiglet # behöver installeras i terminalen genom "pip install pyfiglet" (står i readme)
from hangman_turt import *

logotyp = pyfiglet.figlet_format('Velkommen till hanga gubbe!') # tar inte emot svenska bokstäver 

def meny():
    while True:
        print(logotyp)
        fortsätt = input("***Tryck enter för att spela!***: ")
        if fortsätt == '':
            print("""
                    Du är nu påväg in i ett oerhört spännande spel av hänga gubbe
                    Innan vi börjar vill vi informera dig om följande:
                    Du startar med 6 gissningar.
                    Du kan gissa på ord, men endast ord lika långa som det eftersökta ordet
                    När du gissar rätt görs bokstavens rätta plats synlig.
                    Gissar du rätt behåller du samma antal gissningar.
                    Dina tidigare gissade bokstäver registreras.
                    När du gissar fel så är du ett steg närmre till att bli hängd
                    När du gissar fel minskar även ditt antal försök du har kvar
                    Det var nog allt det väsentliga...
                    Låt oss nu spela hänga gubbe!!""")
            break
        else:
            print("\nenter sa vi faktiskt... vi testar igen då... \n")

def get_ord():
    ord = random.choice(ord_lista) # väljer ett slumpmässigt ord från en lista i filen hangman_ord
    while '-' in ord or ' ' in ord:
        ord = random.choice(ord_lista)
    return ord.upper()

def spela(ord):
    ord_samling = "-" * len(ord) # istället för att skriva ut längden av ordet så visas ogissade bokstäver som understruket tills korrekt gissning sker.
    gissning = False
    gissade_bokstaver = []
    gissade_ord = []
    forsok_antal = 6
    meny()
    start()
    print("\nantal bokstäver i ordet som vi söker är", len(ord))
    print("\n")
    while not gissning and forsok_antal > 0:
        gissningen = input("Gissa på en bokstav eller ett ord:").upper()
        if len(gissningen) == 1 and gissningen.isalpha():
            if gissningen in gissade_bokstaver:
                print("Du har redan gissat på denna bokstaven:", gissningen)
                print("Du har gissat på dessa bokstäver: ", " ".join(gissade_bokstaver))
                print("Dessa har du haft rätt på:"," ".join(ord_samling))
            elif gissningen not in ord:
                print("Bokstaven",gissningen,"finns inte i ordet.")
                felgissning(forsok_antal)
                forsok_antal -= 1
                print("du har",forsok_antal,"gissningar kvar")
                gissade_bokstaver.append(gissningen)
                print("Du har gissat på dessa bokstäver: ", " ".join(gissade_bokstaver))
                print("Dessa har du haft rätt på:"," ".join(ord_samling))
            else:
                print("Bra jobbat! Bokstaven",gissningen, "finns med i ordet!")
                gissade_bokstaver.append(gissningen)
                # ord_samling: en lista som visar vilket det nuvarande ordet är, med utbyte av bokstäverna som är rätt, och resten "-".
                # Gissade bokstaver syns genom letter if letter, annars är det ett "-" för varje bokstav i ordet tills man gissar rätt.
                ord_samling = [bokstav if bokstav in gissade_bokstaver else '-' for bokstav in ord]
                print("Dessa har du haft rätt på:"," ".join(ord_samling))
                if "-" not in ord_samling:
                    gissning = True # om gissningen resulterar i ett fulländat ord och allt är klart så är spelet True och man vinner
        elif len(gissningen) == len(ord) and gissningen.isalpha():
            if gissningen in gissade_ord:
                print("Du har redan gissat på detta ordet:",gissningen)
            elif gissningen != ord:
                print(gissningen, " är inte rätt ord")
                felgissning(forsok_antal)
                forsok_antal -= 1
                print("du har",forsok_antal,"gissningar kvar")
                gissade_ord.append(gissningen)
            else:
                gissning = True
                ord_samling = ord
        else:
            print(gissningen,"är inte en godkänd gissning")
            print("Tänk på att du behöver gissa på bokstäver samt att längden på det gissade ordet behöver vara samma som det sökta ordet") # lägga till: "längden på ordet är:", len(ord))
        print("\n")
    if gissning:
        print("Yay! Du gissade rätt ord, du har vunnit hänga gubbe!")
    else:
        print("Du har tyvärr inga forsök kvar.. Det rätta ordet var:",ord)
        

def spela_igen(): #Om svaret är Ja så kommer hänga gubbe köras igen, annars så avslutas spelet.
    spela = input('Vill du spela igen?').lower()
    if spela == 'ja':
        print("Kul! då kör vi igen!")
        main()
    elif spela == 'nej':
        print('Så tråkigt...Hej då!')
    else:
        print("det verkade inte som att du skrev varken ja eller nej.")
        spela_igen()

def main():
    ord = get_ord()
    spela(ord)
    spela_igen()

main()