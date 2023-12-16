import datetime


comprimento = "ola"
nome = "Ana"
turno = "Bom dia"

print (len(comprimento + nome + turno))

print(2*1**2)

"""
temperaturaF = float(input("Digite a tempoeratura em F: "))

temperaturaC = (temperaturaF - 32 ) * 5 / 9

print("A temperatura em celsius é: ", temperaturaC)
"""
print("ola")
print()
print("Bom dia!")

print("----------------------------------")

a = 10
b = 20
c = a
b = c
a = b
print(a,b,c)


print("----------------------------------")

a = 10
b = 5
c = a + b
b = 20
print(a,b,c)

print("----------------------------------")

A = 10
a = 20
a = 2 * a
A = a + A
print(a)

print("----------------------------------")
print ("olá" 'mundo')

print("----------------------------------")
"""
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)
"""

x = 10
y = 20
z = 30
print(x == z - y and z != y - x or not y != z - x)

print("----------------------------------")

print(  not y >  10 or not z >10 )


print(1 + 1 + 1 == 3)

is_Ready = False 

if(is_Ready):
    print("Verdadeira!")
else:
    print("False ")

print("--------------Ultimo--------------------")
texto = "computação"
print(len(texto))
if len(texto) > 10:
    print ("texto com mais de 10 caracteres")
else:
    print ("texto com 10 ou menos caracteres")



# ----------  While / List -  Soma os números  ------------ # 
'''
soma = 0
sair  = ""
numeros = []

while(sair != "s" and sair!= "S" and not "s" in sair ):
    
    numero = float(input("Digite um numero para somar: "))
    numeros.append(numero)
    soma  += numero
    print("\n-------------------")

    sair =  input("Dseja Sair? digite s ou S: ")

# Lista os numeros digitados: 
print(numeros)

# Lista a soma dos numeros digitados:
print("Soma dos numeros: ", soma)

# Ordena a lista dos numeros: 
numeros.sort(reverse=True)
print(numeros)

'''



# ----------  Listas / List - list -  ------------ # 


alunos = [
        {"nome": "João", "idade": 30, "dataMatricula": "19/04/2023"},
        {"nome": "Maria", "idade": 18, "dataMatricula": "01/01/2018"},
        {"nome": "Pedro", "idade": 22, "dataMatricula": "23/12/2022"}, 
        {"nome": "Elisete", "idade": 54, "dataMatricula": "29/06/2019"}
        ]

for aluno in alunos:
    print(aluno)


# Ordena os alunos pela idade: 
print("# Ordena os alunos pela idade: ")
alunos.sort(key=lambda pessoa: pessoa["idade"] )
print(alunos)

# soma a e media de idade dos alunos: 
print("# soma a e media de idade dos alunos: ")
mediaIdade = sum(aluno["idade"] for aluno in alunos) / len(alunos)
print(mediaIdade)

# Ordena os alunos pela data da matricula: 
print("# Ordena os alunos pela data da matricula:")
alunosOrdenados = sorted(alunos, key=lambda x: x['idade'])
print(alunosOrdenados)

# Buscar o aluno mais velho: 
print("# Buscar o aluno mais velho: ")
alunosMaisVelho = max(alunos, key=lambda x:x['idade']) 
print(alunosMaisVelho)

# Busca o aluno mais novo: 
print("# Busca o aluno mais novo: ")
alunosMaisNovo = min(alunos, key=lambda x:x['idade']) 
print(alunosMaisNovo)

# Bsuca aluno pelo nome: 
print("# Bsuca aluno pelo nome: ")
nome_aluno = "Pedro"
aluno_encontrado = next(filter(lambda x: x['nome'] == nome_aluno, alunos), None)

# Verificar se o aluno foi encontrado
if aluno_encontrado:
    print(f"Aluno encontrado: {aluno_encontrado}")
else:
    print(f"Aluno com o nome '{nome_aluno}' não encontrado.")







