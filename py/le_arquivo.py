import csv

nome_arquivo = 'diario_bordo.csv'
nome_coluna = 'Sistema'
analistas = set([])

with open(nome_arquivo, 'r', encoding = 'utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=';')
    
    # Certifique-se de que a coluna existe no arquivo
    if nome_coluna not in leitor_csv.fieldnames:
        print(f"A coluna {nome_coluna} não foi encontrada no arquivo.")
    else:
        # Itera sobre as linhas e imprime os dados da coluna específica
        for linha in leitor_csv:
            if (linha[nome_coluna]  == "" and len(linha[nome_coluna]) == 0):
                continue
            else:
                analistas.add((linha[nome_coluna]))


print(analistas)


def procura_elemento(nome):
     if (nome in analistas):
         return nome
     else:
         None

""" 
for analista in analistas:
        if (analista == nome ):
            return analista
            break
    else:
        None

""" 
nome_pocurado = "promax"
nome_analistas_encontrado = procura_elemento(nome_pocurado)
if (nome_analistas_encontrado != None):
    print(" ||{}|| esta na lista! ".format(nome_analistas_encontrado))
else:
    print("elemento não encontrado!")


