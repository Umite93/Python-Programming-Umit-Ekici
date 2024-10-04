import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datapoints.txt") # läser in filen genom pandas med hjälp av csv nyckelord
df = df.drop(" 1-pikachu))", axis = 1) # tar bort kolumn, i det här fallet 1-pikachu, axis = 0 betyder raden och axis = 1 betyder kolumnen
df["Pichu_Pikachu"] = df[" label (0-pichu"] # skapar en ny kolumn i träningsdatan, i det här fallet Pichu_Pikachu som ny kolumn
df = df.drop(" label (0-pichu", axis = 1) # tar bort kolumnen (0-pichu
df.columns = df.columns.str.replace("(", "").str.replace(")", "").str.replace("_h", "H").str.capitalize() # rensar/ändrar namnen på kolumnen


pic = df[df["Pichu_pikachu"] == 0] # delar träningsdatan utifrån pichu och pikachu punkter
pika = df[df['Pichu_pikachu'] == 1]

plt.scatter(pic['Width cm'], pic[' height cm'], color = "red") # anger i en graf alla pichu punkter som rött
plt.scatter(pika['Width cm'], pika[' height cm'], color = "green") # anger i en graf alla pikachu punkter som grönt
plt.show()

test_lt=[] # skapar en ny lista för testdatan
with open("testpoints.txt") as file: #läser in testdatan och kallar det file
    test_file = file.readlines() #läser in file rad för rad
    for x in test_file:
        test_lt.append(x) # med hjälp av loopen så lägger den in filen rad för rad i test listan

test_data = pd.DataFrame(test_lt) # visar listan för testdatan tabulärt genom DataFrame
test_data = test_data.drop(0, axis = 0) # tar bort siffran 0 från raden
test_data["Width"] = test_data[0].str.split("(").str.get(1).str.split(",").str.get(0) # sorterar kolumnerna genom att dela upp siffrorna från parentesen och kommatecknen och lägger dom under Width respektive Height kolumnen
test_data["Height"] = test_data[0].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop(0, axis = 1) # tar bort nummer 0 från raden
test_data[["Width", "Height"]] = test_data[["Width", "Height"]].astype(float) # omvandlar text till decimaler


def one_point(wid, hie): # funktion för och klassifiera punkterna för och kunna se fall det är pichu eller Pikachu
   liist = [] # skapa en ny lista
   for x, y in zip(df['Width cm'], df[' height cm']): # loopar genom Width och Height med hjälp av zip för och räkna avståndet mellan inmatade data och träningsdata
      liist.append(np.sqrt(np.power(x-wid, 2)+np.power(y-hie, 2))) # beräkningen av avståndet mellan punkterna som läggs in i listan

   minsta_värde = min(liist) # minsta avstånd i listan
   rade_träning = liist.index(minsta_värde) # hittar nummer på raden
   if df.loc[rade_träning, "Pichu_pikachu"] == 1: # visar i vilken rad minsta avståndet befinner sig i
      print(f"point({wid},{hie}): classified as Pikachu")
   else: 
      print(f"point({wid},{hie}): classified as Pichu")

for x, y in zip(test_data["Width"], test_data["Height"]): # loopar genom testdatan
   one_point(x, y) # funktionen för testdatan (wid, hie)

print() # visar en tom rad i terminalen

def ten_point(wid, hie): # funktion för och klassifiera punkterna för och kunna se fall det är pichu eller Pikachu
   liist = [] # skapa en lista
   for x, y in zip(df['Width cm'], df[' height cm']): # loopar genom Width och Height med hjälp av zip för och räkna avståndet mellan inmatade data och träningsdata
    liist.append(np.sqrt(np.power(x-wid, 2)+np.power(y-hie, 2))) # beräkningen av avståndet mellan punkterna som läggs in i listan

   sortlist = sorted(liist) # sortera listan
   ten_nearest = sortlist[:10] # tar fram de 10 närmaste värden
   index_nearest_point = [liist.index(x) for x in ten_nearest] # visar raderna på de 10 närmsta avstånden
   result = df.loc[index_nearest_point, "Pichu_pikachu"] # 
   if sum(result) >= 5:
      return f"point ({wid},{hie}) classified as Pikachu based on majority of ten point"
   else: 
      return f"point ({wid},{hie}) classified as Pichu based on majority of ten point"

for x, y in zip(test_data["Width"], test_data["Height"]):
   print(ten_point(x, y))

print()

while True: # används när man vill loopa oändligt
    try: # testar när det ej matas in ett positivt nummer så ger den error
        width = input("enter your first positive number") # första värdet som ska matas in
        height = input("enter your second positive number") # andra värdet som ska matas in
        height = height.replace(",", ".") # ersätter kommatecknet med en punkt
        width = height.replace(",", ".") # ersätter kommatecknet med en punkt
        if float(height) < 0 or float(width) < 0: # bestämmer värdet som matas in om värdet är positiv eller ej, då negativa tal är mindre än 0
            print("it is not a positive number") # ger svaret om negativa värden anges
        else: # annars har användaren matat in rätt värde som skrivs ut
            ten_point(float(width), float(height))
            one_point(float(width), float(height))
            break
    except ValueError: # ger error utifrån felvärdet som matas in
        print("you have given a false value") # ger svaret när ett värde som ej finns med anges, som t.ex. ensiffrigt tal eller en bokstav

