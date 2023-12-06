from conta import Conta
from filme import Filme
from serie import Serie 

conta = Conta(titular="Andrei", saldo=50, limite=1500)
conta2 = Conta(titular="Saci", saldo=5, limite=10)


conta.deposita(150)
conta.saca(50)

conta.extrato()

conta.transfere(50, conta2)



conta.extrato()
conta2.extrato()




filme = Filme(nome="A volta dos que não foram", ano=1992, duracao=150 )

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 5)
for i in range(0, 1800):
    atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.tenporadas} - Likes: {atlanta.like}')
