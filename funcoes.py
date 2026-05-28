import math
import utils

### USAR utils.carregar_alunos() PARA PUXAR AS INFORMAÇÕES DOS ALUNOS

#UI Inicial

def menu():
    print("""
=================
 Grades Registry
=================
          
Digite o número correspondente para acessar:
1.Registrar um novo aluno
2.Registrar novas notas em um aluno já registrado
3.Pesquisar Nota de Aluno


          
Para sair aperte CTRL+C""")
    while True:
        try:
               r = int(input())
        except ValueError:
               r = int(input("Digite apenas números inteiros"))

        match r:
            case 1:
                      registrar_aluno()
            case 2:
                      registar_nota()
            case 3:
                      pesquisa()
            case _:
                      print("Digite apenas uma das opções dadas. Tente novamente")
        break
                  

"""ESTRUTURA DOS DADOS ARMAZENADOS: ARRAY [X][6]
[NOME][NOTA1][NOTA2][NOTA3][NOTA4][MEDIA]"""

### PRIMEIRA FUNÇÃO PARA REGISTAR ALUNO

def registrar_aluno():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    with open("dados/aluno.txt", 'a') as arquivo:
        arquivo.write(f"{nome},{nota1},{nota2},{nota3},{nota4},{media:.2f}\n")

    print(f"Aluno '{nome}' registrado com média {media:.2f}.")
    print("Aperte ENTER para continuar:")
    input()






### TRANSFORMAR PARA ALTERAR 2o A 5o ITEM DA LINHA PARA ALTERAR APENAS AS NOTAS
def registar_nota():
       nome = input("Nome do aluno:")
       return



### PROCURAR LINHA POR NOME DO ALUNO E EXIBIR O NOME COMPLETO E AS NOTAS + MÉDIAS
def pesquisa():
       
    nome_procurado = input("Digite o nome do aluno: ")

    try:
        with open("dados/aluno.txt", "r") as arquivo:
            encontrado = False

            for linha in arquivo:
                dados = linha.strip().split(",")

                if dados[0].lower() == nome_procurado.lower():
                    encontrado = True

                    print("\n===== DADOS DO ALUNO =====")
                    print(f"Nome: {dados[0]}")
                    print(f"Nota 1: {dados[1]}")
                   
                    print(f"Nota 2: {dados[2]}")
                    print(f"Nota 3: {dados[3]}")
                    print(f"Nota 4: {dados[4]}")
                    print(f"Média : {dados[5]}")
                    print("==========================")

                    break

            if not encontrado:
                print(f"Aluno '{nome_procurado}' não encontrado.")

    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")

    print("\nAperte ENTER para continuar:")
    input()
    return

