import math
import utils
import os

### USAR utils.carregar_alunos() PARA PUXAR AS INFORMAÇÕES DOS ALUNOS

#UI Inicial

def menu():
    print("""
=================
 Grades Registry
=================

Digite o número correspondente para acessar:
1.Registrar um novo aluno
2.Pesquisar Nota de Aluno/Alterar Notas



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
                    pesquisa()
            case _:
                      print("Digite apenas uma das opções dadas. Tente novamente")
        break


"""ESTRUTURA DOS DADOS ARMAZENADOS: ARRAY [X][6]
[NOME][NOTA1][NOTA2][NOTA3][NOTA4][MEDIA]"""



### PRIMEIRA FUNÇÃO PARA REGISTAR ALUNO

def registrar_aluno():
    nome = input("Nome do aluno: ")
    #Carrega local das notas em uma array [1][5]
    arquivo = utils.carregar_alunos("dados/0materias.txt")
    for materia in arquivo:
        #Mostra a materia que as notas estão sendo colocadas
        match materia[0]:
              case "dados/humanas.txt":
                    print("Notas de Humanas")
              case "dados/linguagens.txt":
                    print("Notas de Linguagens")
              case "dados/matematica.txt":
                    print("Notas de Matematica")
              case "dados/naturezas.txt":
                    print("Notas de Naturezas")
              case "dados/redacao.txt":
                    print("Notas de Redação")
        #Recebe notas da materia
        while True:
            try:
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
                nota3 = float(input("Nota 3: "))
                nota4 = float(input("Nota 4: "))
                media = (nota1 + nota2 + nota3 + nota4) / 4
                break
            except ValueError:
                print("Digite apenas números. Tente novamente")
        #Registra as notas nos respectivos arquivos
        with open(f"{materia[0]}", 'a') as file:
            file.write(f"{nome},{nota1},{nota2},{nota3},{nota4},{media:.2f}\n")


    os.system('cls' if os.name == 'nt' else 'clear')
    #Exibe as medias de cada matéria
    print(f"Aluno(a) '{nome}' registrado com médias:")
    for materia in arquivo:
          alunos = utils.carregar_alunos(materia[0])
          # O aluno recém-registrado é o último da lista; a média é a 6ª coluna
          media_aluno = alunos[-1][5]
          match materia[0]:
              case "dados/humanas.txt":
                    print(f"Humanas: {media_aluno}")
              case "dados/linguagens.txt":
                    print(f"Linguagens: {media_aluno}")
              case "dados/matematica.txt":
                    print(f"Matematica: {media_aluno}")
              case "dados/naturezas.txt":
                    print(f"Naturezas: {media_aluno}")
              case "dados/redacao.txt":
                    print(f"Redação: {media_aluno}")
    print("\nAperte ENTER para continuar:")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')




### TRANSFORMAR PARA ALTERAR 2o A 5o ITEM DA LINHA PARA ALTERAR APENAS AS NOTAS
def registar_nota(nome_procurado):
    try:
        #Menu de escolha de notas para alterar
            materia = int(input('''
Digite o número correspondente da matéria que deseja alterar as notas:
1.Humanas
2.Linguagens
3.Matematica
4.Naturezas
5.Redação
                  '''))
    except ValueError:
            materia = int(input("Digite apenas números inteiros"))
    #Diz local do arquivo a ser utilizado dependendo do input do usuario
    match materia:
        case 1:
                materia = "dados/humanas.txt"
        case 2:
                materia = "dados/linguagens.txt"
        case 3:
                materia = "dados/matematica.txt"
        case 4:
                materia = "dados/naturezas.txt"
        case 5:
                materia = "dados/redacao.txt"
        case _:
                print("Digite apenas uma das opções dadas. Tente novamente")
    arquivo = utils.carregar_alunos(materia)
    encontrou = False

    for aluno in arquivo:

        if aluno[0] == nome_procurado:
            # Exibe as notas antigas antes de alterar
            print("Aluno encontrado!")
            print("\n===== NOTAS ANTIGAS =====")
            print(f"Nota 1: {aluno[1]}")
            print(f"Nota 2: {aluno[2]}")
            print(f"Nota 3: {aluno[3]}")
            print(f"Nota 4: {aluno[4]}")
            print(f"Média : {aluno[5]}")
            print("=========================")

            # Recebe as notas novas
            print("\nDigite as novas notas:")
            while True:
                try:
                    n1 = float(input("Nota 1: "))
                    n2 = float(input("Nota 2: "))
                    n3 = float(input("Nota 3: "))
                    n4 = float(input("Nota 4: "))
                    media = (n1 + n2 + n3 + n4) / 4
                    break
                except ValueError:
                    print("Digite apenas números. Tente novamente")

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
        # Salva de volta no arquivo da matéria selecionada (pasta dados)
        # Não pode ser "as arquivo" porque se não o python substitui a lista inteira
        with open(materia, "w", encoding="utf-8") as f:
            for aluno in arquivo:
                f.write(f"{aluno[0]},{aluno[1]},{aluno[2]},{aluno[3]},{aluno[4]},{aluno[5]}\n")
        print("Notas atualizadas com sucesso!")
    else:
        print("Aluno não encontrado.")

    print("\nAperte ENTER para continuar:")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')



### PROCURAR LINHA POR NOME DO ALUNO E EXIBIR O NOME COMPLETO E AS NOTAS + MÉDIAS
def pesquisa():

    nome_procurado = input("Digite o nome do aluno: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    # As notas ficam separadas por matéria; percorre cada arquivo de matéria
    materias = utils.carregar_alunos("dados/0materias.txt")
    encontrado = False
    nome_completo = nome_procurado

    print("\n===== DADOS DO ALUNO =====")
    for materia in materias:
        alunos = utils.carregar_alunos(materia[0])
        for aluno in alunos:
            if aluno[0].lower() == nome_procurado.lower():
                encontrado = True
                nome_completo = aluno[0]

                match materia[0]:
                    case "dados/humanas.txt":
                        nome_materia = "Humanas"
                    case "dados/linguagens.txt":
                        nome_materia = "Linguagens"
                    case "dados/matematica.txt":
                        nome_materia = "Matematica"
                    case "dados/naturezas.txt":
                        nome_materia = "Naturezas"
                    case "dados/redacao.txt":
                        nome_materia = "Redação"
                    case _:
                        nome_materia = materia[0]

                print(f"\n{nome_materia}:")
                print(f"  Nota 1: {aluno[1]}")
                print(f"  Nota 2: {aluno[2]}")
                print(f"  Nota 3: {aluno[3]}")
                print(f"  Nota 4: {aluno[4]}")
                print(f"  Média : {aluno[5]}")
                break

    if encontrado:
        print(f"\nNome: {nome_completo}")
        print("==========================")
    else:
        print(f"Aluno '{nome_procurado}' não encontrado.")
        print("==========================")
    try:
            r = int(input('''
Digite o número correspondente para acessar:
1.Voltar ao menu inicial
2.Alterar Notas do Aluno Selecionado
                  '''))
    except ValueError:
            r = int(input("Digite apenas números inteiros"))

    match r:
        case 1:
                print("\nAperte ENTER para continuar:")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        case 2:
                registar_nota(nome_procurado)
        case _:
                print("Digite apenas uma das opções dadas. Tente novamente")
