from midia import Midia

class Serie (Midia): 
    def __init__(self, nome, ano, tenporadas):
        super().__init__(nome, ano)
        self.__tenporadas = tenporadas
        
    @property
    def tenporadas(self):
        return self.__tenporadas
    
    @tenporadas.setter
    def temporadas(self, temporadas):
        self.__tenporadas = temporadas
    
 

