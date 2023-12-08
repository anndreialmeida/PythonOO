class Midia: 
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano 
        self._likes = 0

    @property
    def likes (self):
        return self._likes
    
    def dar_like (self):
        self._likes +=1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome_atualizado):
        self._nome = nome_atualizado
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano