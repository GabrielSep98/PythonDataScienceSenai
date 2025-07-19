#%%

import csv
import os

#Biblioteca de Graficos
import matplotlib.pyplot as plt

ARQUIVOS_CSV = 'dados_senai.csv'

#verificar se o arquivo existe 

arquivo_existe = os.path.exists(ARQUIVOS_CSV)

## gera um arquivo true ou false


# FUNÇÃO salvar arquivo

def salvar_em_csv (nome,idade,email):
    # Modo a -> Inserir informação
    # newline -> evitar linhas brancas
    # econding -> codifiCação de teclado BR

    with open (ARQUIVOS_CSV, mode ='a', newline='', encoding='utf-8') as arquivo:

        #escrito para reescrever o arquivo
        escritor  = csv.writer(arquivo)

        #se o arquivo não existir 
        if not arquivo:
            #cria uma nova linha
            escritor.writerow(['nome', 'idade', 'email'])
        
        escritor.writerow([nome,idade,email])

#Função de mostra Grafico
def mostrar_grafico():

    #ler idades
    faixas = {
        '0-17': 0,
        '18-30': 0,
        '31-45': 0,
        '46-60': 0,
        '60+': 0,
    }
    #Modo R -> Read
    with open(ARQUIVOS_CSV, mode ='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        # enquanto tiver linhas ele percorre
        for linha in leitor:
            #try trata erro
            try:
                idade = int(linha['idade'])
                if idade <= 17:
                    faixas['0-17'] += 1
                elif idade <= 30:
                    faixas['18-30'] +=1
                elif idade <= 45:
                    faixas ['31-45'] +=1
                elif idade <=60:
                    faixas ['46-60'] +=1
                else:
                    faixas ['60+'] += 1
            #Caso na linha idade tenha um caracter que não seja int ele continua a leitura
            except ValueError:
                continue

        #Plot do Grafico
        plt.bar(faixas.keys(), faixas.values(), color='skyblue')
        plt.title('Distribuição Faixa Etaria')
        plt.xlabel('Faixa Etaria')
        plt.ylabel('Quantidade de pessoas')

        # Linha do Grid = true
        #tracejado e largura
        plt.grid(True,linestyle='--', alpha=0.5)
        #Ajusta o Grafico
        plt.tight_layout()
        plt.show()


#Função Principal
def main():
    while True:
        print ("\d Digite os dados do Usuario:")
        nome = input("Nome:")
        idade = input("Idade:")
        email = input("E-mail:")

        #chamando a função de salvar no arvquivo csv
        salvar_em_csv(nome,idade,email)
        print ("Dados salvos com sucesso")

        continuar = input("Deseja adicionar outro usuario ? s/n")

        if continuar != 's':
            break
    mostrar_grafico()


if __name__ == '__main__':
    main()

#%%