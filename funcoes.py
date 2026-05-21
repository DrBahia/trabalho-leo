import math




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
                  


def registrar_aluno():
    print("bruh")
    with open("dados/aluno.txt", 'a') as arquivo:
           arquivo.write("Nome Nota \n")
        
    return




def registar_nota():
          print("Bruh")
          return


def pesquisa():
        print("Bruh")
        return

