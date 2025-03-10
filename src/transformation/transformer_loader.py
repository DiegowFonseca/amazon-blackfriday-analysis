import pandas as pd

class TransformerLoader:
    
    def __init__(self):
        pass

    def join(self, nome_arquivos, tipo):
        if len(nome_arquivos) == 0:
            print("Não possui nenhum arquivo.")
            return
        
        if tipo == 'livro':
            caminho_diretorio = "C:/Users/Mestre/Desktop/Intensivão Python/Python Impressionador/ciencia de dados/Web Screping/Amazon/data/data_raw/livros_amazon"

        elif tipo == 'produto':
            caminho_diretorio = "C:/Users/Mestre/Desktop/Intensivão Python/Python Impressionador/ciencia de dados/Web Screping/Amazon/data/data_raw/produtos_amazon"

        else:
            print("Tipo não informado")
            return

        df_produtos = pd.DataFrame(columns=['nome', 'preco', 'classificado', 'categoria', 'site', 'data_raspagem'])
        
        for arquivo in nome_arquivos:
            caminho = f"{caminho_diretorio}/{arquivo}"
        
            base = pd.read_csv(caminho)

            df_produtos = pd.concat([df_produtos, base], axis=0)

        return df_produtos
    
    def transformer(self, df):

        # Trocar o nome da coluna de classificado para ranking
        nome_colunas = {
            'nome': 'nome', 
            'preco': 'preco', 
            'classificado': 'ranking', 
            'categoria': 'categoria',
            'site': 'site',
            'data_raspagem': 'data_raspagem'
        }

        df = df.rename(columns=nome_colunas)

        # Transformação da coluna 'preco', tirando o cifrão, trocando o separador decimal e transformando ela em float
        df['preco'] = df['preco'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype('float64')

        # Tranformação da coluna 'ranking', tirando a # e deixando como um object
        df['ranking'] = df['ranking'].str.replace('#', '').astype('object')

        # Transformação da coluna 'data_raspagem' em uma coluna de datetime
        df['data_raspagem'] = pd.to_datetime(df['data_raspagem'])

        # Eliminando a coluna 'site'
        df = df.drop('site', axis=1)

        return df
    
    def loader(self, df, nome_arquivo='produtos.csv'):

        caminho = "C:/Users/Mestre/Desktop/Intensivão Python/Python Impressionador/ciencia de dados/Web Screping/Amazon/data/data_processed"

        # Transformar o dataframe em um arquivo csv
        df.to_csv(f"{caminho}/{nome_arquivo}", index=False)

        print("Dataframe armazenado em um arquivo csv.")

