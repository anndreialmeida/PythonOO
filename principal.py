from conta import Conta

conta = Conta(titular="Andrei", saldo=50, limite=1500)
conta2 = Conta(titular="Saci", saldo=5, limite=10)


conta.deposita(150)
conta.saca(50)

conta.extrato()

conta.transfere(50, conta2)



conta.extrato()
conta2.extrato()

print(Conta.codigo_banco())

print(Conta.codigo_bancos())

lista_bancos = Conta.codigo_bancos()

print(lista_bancos['BB'])


