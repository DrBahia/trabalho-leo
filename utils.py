import math



def carregar_alunos():
    alunos = []
    try:
        with open("dados/aluno.txt", 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    alunos.append(linha.strip().split(','))
    except FileNotFoundError:
        pass
    return alunos