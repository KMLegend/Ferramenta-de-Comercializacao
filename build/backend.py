import pandas as pd

class Backend:
    def __init__(self):
        # Inicialização da classe, se necessário
        pass

    def buscar_planilha_cadastro(self):
        # Método que retorna os dados solicitados pelo botão
        # Pode consultar um banco de dados, realizar cálculos, etc.
        dados = print("dados foi solicitados")
        return dados

    def buscar_planilha_excecao(self):
        df = pd.read_excel("C:\\Users\\kevin.maykel\\OneDrive - CITY INCORP LTDA\\Documentos\\Meus Projetos\\Ferramenta Comercialização\\Ferramenta-de-Comercializacao\\build\\teste1.xlsx")
        
        dados = print(df)
        return dados