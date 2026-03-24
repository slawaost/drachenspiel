#importiere bibliothek für zufallszahlen
import random

class Held:
    #attribute: brauche ich das überhaupt?
    __ausdauer: int
    __tage: int
    __inventar: list
    __gold: int
    __level: int
    __name: str
    
    # konstruktor - wied aufgerufen wenn held erstellt wird
    def __init__(self, name:str):
        self.__name = name
        self.__ausdauer = 20
        self.__tage = 0
        self.__gold = 10
        self.__level = 1
        self.__inventar = []
        
        #wenn held rastet, ausdauer regeneriert
    def rasten(self):
        self.__ausdauer = self.__level * 20
        self.__tage += 1
        print("gerastet")
    #gold zurückgeben
    def getGold(self):
        return self.__gold
        #item ins inventar aufnehmen
    def giveItem(self, item):
        self.__inventar.append(item)
    # status des helden anzeigen
    def showStatus(self):
        print("Name:", self.__name)
        print("Gold:", self.__gold)
        print("Level:", self.__level)
        print("Ausdauer:", self.__ausdauer)
        print("Tage gespielt:", self.__tage)

        print("Inventar:")
        #prüfe ob inventar leer ist
        if len(self.__inventar) == 0:
            print("leer")
        else:
            for item in self.__inventar:
                print("-", item.getName())
    # berechne kampfchance
    def kaempfen(self):
        chance = 50
        #buffs der items erhöhen die gewinnchance
        for item in self.__inventar:
            chance += item.getBuff()
        return chance
    #wald-event (monster begegnen)
    def wald(self):
        #generiere random von 1 bis 3 monsters
        monster  = random.randint(1, 3)
        print("Du triffst", monster, "Monster!")

        entscheidung = input("kaempfen oder fliehen?")

        if entscheidung.lower() == "kaempfen":

            chance = self.kaempfen()
            wurf = random.randint(1, 100)
            # spieler gewinnt
            if wurf <= chance: 
                gold = random.randint(10, 100)
                self.__gold += gold
                print("gewonnen! gold:", gold)
            # spieler verliert
            else:
                schaden = random.randint(5, 15)
                self.__ausdauer -= schaden
                print("verloren! schaden: ", schaden)
                # spieler stirbt
                if self.__ausdauer <= 0:
                    print("du bist gestorben")

                    self.__gold = self.__gold // 2
                    self.__tage += 1
                    self.__ausdauer = self.__level * 20

                    print("du erwachst wieder im Dorf..")

        else:
            print("geflohen")
    #item kaufen
    
    def item_kaufen(self, item):
        print("gold", self.__gold, "preis", item.getPreis())
        if self.__gold >= item.getPreis():
            self.__gold -= item.getPreis()
            self.__inventar.append(item)
            print("self.__gold = ", self.__gold)
            print(item.getName(), "gekauft.")
        else:
            print("nicht genug Gpld")
    # training für level-up
    def trainieren(self):

        if self.__gold >= 10:
            self.__gold -= 10
            self.__level += 1
            print("training erfolgreich! neue level:", self.__level)
        else:
            print("nicht genug gold")
