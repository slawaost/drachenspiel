class Item:
    
    __buff: int
    __name: str
    __preis: int
    # konstruktor
    def __init__(self, name: str, buff: int, preis: int):
        self.__name = name
        self.__buff = buff
        self.__preis = preis
    #name zurückgeben
    def getName(self)->str:
        return self.__name
    #bonus zurückgeben
    def getBuff(self)->int:
        return self.__buff
    # preis zurückgeben
    def getPreis(self)->int:
        return self.__preis
    