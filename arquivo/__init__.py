def arquivo_existe(caminho):
    try:
        teste = open(caminho, "r")
        teste.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criar_arquivo(caminho):
    try:
        teste = open(caminho, "w")
        teste.close()
    except Exception:
        print("Erro ao tentar criar o arquivo.")
    else:
        print("Arquivo criado com sucesso.")


def ler_arquivo(caminho):
    try:
        arquivo = open(caminho, "r")
    except Exception:
        print("Erro ao tentar ler o arquivo.")
    else:
        return arquivo.readlines()
        arquivo.close()
    

def cadastrar_pessoa(caminho, nome="Desconhecido", idade=None):
    try:
        teste = open(caminho, "a")
    except Exception:
        print("Erro ao ler o arquivo.")
    else:
        try:
            teste.write(f"{nome};{idade}\n")
        except Exception:
            print(f"Não foi possível cadastrar {nome}!")
        else:
            print(f"Novo registro de {nome} adicionado.")

