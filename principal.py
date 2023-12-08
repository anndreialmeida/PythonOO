from conta import Conta
from filme import Filme
from serie import Serie 

conta = Conta(titular="Andrei", saldo=50, limite=1500)
conta2 = Conta(titular="Saci", saldo=5, limite=10)


conta.deposita(150)
conta.saca(50)
conta.transfere(50, conta2)
"""
conta.extrato()
conta2.extrato()

"""


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('atlanta', 2018, 5)
for i in range(0, 1800):
    atlanta.dar_like()
#print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.tenporadas} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    ## verifica se possui o atributo duracao no objeto programa, se não imprime temporadas em vez de duracao
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - T: {detalhes} - Likes: {programa.likes}')
    