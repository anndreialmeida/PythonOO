class Serie: 
    def __init__(self, nome, ano, tenporadas):
        self.__nome = nome.title()
        self.__ano = ano 
        self.__tenporadas = tenporadas
        self.__likes = 0
    
    @property
    def like (self):
        return self.__likes
    
    def dar_like (self):
        self.__likes +=1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_atualizado):
        self.__nome = nome_atualizado
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano_atualizado):
        self.__ano = ano_atualizado

    @property
    def tenporadas(self):
        return self.__tenporadas

