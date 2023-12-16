import os 

nome_diretorio = 'pedidosFiltrados'
diretorio_atual = os.getcwd()


caminho_diretorio = os.path.join(diretorio_atual, nome_diretorio)

if not os.path.exists(caminho_diretorio):
    os.makedirs(caminho_diretorio)
    print(f"Diretorio '{caminho_diretorio}' criado com sucesso")
else:
    print(f"Diretorio '{caminho_diretorio}' ja existe")


for i in range(5):
    nome_arquivo = f'arquivo{i}.txt'
    caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(f"Conteúdo do arquivo {i}\n")
    print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")