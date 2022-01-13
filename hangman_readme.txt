
**README**

Om spelet:
Hänga gubben är ett klassiskt spel som oftast brukar utföras med penna och papper.
I denna version sker spelet digitalt.
Spelet går ut på att användaren ska försöka gissa rätt ord
utifrån ett känt antal bokstäver innan försöken tar slut.
För varje felgissning så ritas en del av figuren ut som tillslut ska föreställa en hängd gubbe. 


Hur spelet fungerar:
När användaren skriver in en gissning som antigen kan vara en bokstav eller ett ord så
sparas dessa till en lista. Om användaren gissar på samma ord/bokstav flera gånger så kommer
programmet ge information om att detta sker. Försöken gäller för unika gissningar,
om användaren gissar på samma ord/bokstav flera gånger kvarstår försöken. 

Ordet som används vid spelomgången genereras slumpmässigt från en lista som
består av 200 svenska ord. Hur många bokstäver som det sökta ordet består av får
användaren information om när spelomgången startar. Användaren har 6 försök på sig att
gissa rätt, om användaren gissar fel så försvinner ett försök och användaren får
information i programmet om detta.

När man startar programmet så dyker en ruta upp där själva grafiken för spelomgången skapas.
När man startar spelet så skrivs grafiken för ”hängaren” ut, för varje felgissning så kommer
en ny kroppsdel av gubben att skrivas ut och vid 6e felgissningen så visar grafiken
slutligen en hängd sträckgubbe. 

Om användaren gissar rätt på en bokstav så kommer denna bokstav skrivas ut i programmet
och ersätta det sträck där bokstaven hör hemma. Antalet försök kvarstår vid en korrekt gissning.
Om användaren gissar på ord så måste ordet ha lika många bokstäver som det ord som söks,
annars är det inte en giltig gissning. Om användaren gissar på rätt ord så har denne vunnit
och spelet avslutas. Användaren får då en fråga om denne vill spela igen.
Svarar användaren ja kommer en ny spelomgång startas, annars avslutas spelet.

filer:
hangman_ord.py - fil för ord som används i programmet
hangman_gubbe.py - fil för själva spelet
hangman_turt.py - fil för grafiken till spelet som ritar ut "hänga gubbe"


Moduler:
random - För att kunna slumpmässigt generera fram ord från hangman_ord
turtle - Denna modul används för att grafiskt kunna skriva ut sträckgubben som finns i filen hangman_turt.
pyfiglet - En modul som vi använt i vår meny för att skriva ut titel, modulen skriver ut ASCII-text
i ett visst typsnitt. Pyfiglet är inte en inbyggd modul, denna måste man installera
genom att skriva ’pip install pyfiglet’ i terminalen.

lägga in som:

f = open("readme_hangman.txt","r")

print(f.read())

eller bara ha med i själva mappen?

