class Conta: 
    def __init__(self, titular, saldo, limite):
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property   
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.limite + self.saldo)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R$ {} ultrapssou o limite!".format(valor))
    
    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def extrato(self):
        print("{}, seu saldo é de R$: {}, e o limite disponivel é R$: {}".format(self.__titular, self.__saldo, self.__limite))
    


        
        