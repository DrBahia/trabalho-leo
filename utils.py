import math



def carregar_alunos(materia):
    alunos = []

    try:
        with open(f"{materia}", 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    alunos.append(linha.strip().split(','))
    except FileNotFoundError:
        pass
    return alunos