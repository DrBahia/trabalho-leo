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
   # Pra atualizar os dados em arquivo
            aluno[1] = str(n1)
            aluno[2] = str(n2)
            aluno[3] = str(n3)
            aluno[4] = str(n4)
            aluno[5] = f"{media:.2f}"
                
                
            encontrou = True
            break
    
    # Pra salvar
    if encontrou:
        # Não pode ser as arquivo porque se não o python substitui a lista inteira
        # Pode ser qualquer coisa no lugar de f
        with open("dados/aluno.txt", "w", encoding="utf-8") as f:
            for aluno in arquivo:
                f.write(f"{aluno[0]},{aluno[1]},{aluno[2]},{aluno[3]},{aluno[4]},{aluno[5]}\n")
        print("Notas atualizadas com sucesso!")
    else:
        print("Alunos não encontrado.")
        
    print("Aperte ENTER para continuar:")
    input()



### PROCURAR LINHA POR NOME DO ALUNO E EXIBIR O NOME COMPLETO E AS NOTAS + MÉDIAS
def pesquisa():
        print("Bruh")
        return

