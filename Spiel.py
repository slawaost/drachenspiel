#sollen immer import der klassen aus anderen datei machen
from Held import Held
from Item import Item

class Spiel:
    
    __held: Held
    __shop: list 
    
    def __init__(self):
        #erstelle shop liste
        self.__shop = []
        
        #self.__shop.append(Item("Stock",1,5))
        #grüße aus feature b
        #verwenden append() methode, damit element am ende der liste hinzufügen

        item1 = Item("Stock",1,5)
        self.__shop.append(item1)

        item2 = Item("Axt",10,30)
        self.__shop.append(item2)

        item3 = Item("Schwert",20,40)
        self.__shop.append(item3)
        
    def __einkaufen(self):
        print("*** 🎁 S H O P 🎁 ***")
        #items anzeigen
        i=1
        for item in self.__shop:
            #getName usw. weil es private variable ist
            print(str(i)+ " "+item.getName() + " "+str(item.getPreis()))
            i+=1
            
            #wähle ein item
        try:
            wahl = int(input("Welches Item wollt Ihr kaufen?" ))
        except ValueError:
            wahl = 0 
        #Hier wird geprüft, ob die Wahl gültig ist
        if wahl > len(self.__shop) or (wahl <= 0):
           print("Ungültige Wahl. Bitte verlassen Sie sofort den Shop!")
           return
        
        #Item auswählen
        ausgewaehltes_item = self.__shop[wahl-1]
       
        #prüfen, ob ich genügend Geld habe
        if ausgewaehltes_item.getPreis() > self.__held.getGold():
            print("Ihr habt leider nicht genügend Goldstücke.")
            return
        
        #Item aus dem Shop entfernen
        item = self.__shop.pop(wahl-1)
        self.__held.item_kaufen(item)
        #Item in Inventar aufnehmen
        
        print("Sie haben",item.getName(), "gekauft")
        # dann muss man noch gold minus gold den held
        
           #haupt-spielschleife
    def gameloop(self):
        print("*** Willkommen Abendteuer ***")

        name = input("Wie ist Euer Name? ")
        #erstelle neuen Helden
        self.__held = Held(name)
        print("Ein neuer Held wurde geboren!")
        
        ende = False
        #spiel läuft solange ende False ist
        while ende==False:
            print("** Hauptmenü **")
            print("1 - in den Wald gehen")
            print("2 - Rasten")
            print("3 - Shop")
            print("4 - Heldenstatus ausgeben")
            print("5 - Trainieren")
            print("0 - Beenden")

            wahl = input("Was ist Eure Wahl? ")
            
            #auswahl auswerten
            if wahl=="1":
                self.__held.wald()
            elif wahl =="2":
                self.__held.rasten()
            elif wahl =="3":
                self.__einkaufen()
            elif wahl =="4":
                self.__held.showStatus()
            elif wahl == "5":
                self.__held.trainieren()
            elif wahl == "":
                ende = True
            else:
                print("Das habe ich leider nicht verstanden.")
                
        print("Danke fürs Spielen.")
            
    #Hauptmethode 
  
if __name__ == "__main__":

    spiel = Spiel()
    spiel.gameloop()