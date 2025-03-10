from transformation.transformer_loader import TransformerLoader
import pandas as pd

arquivos_livro = [
    'livros_amazon_2024-11-16.csv',
    'livros_amazon_2024-11-17.csv',
    'livros_amazon_2024-11-18.csv',
    'livros_amazon_2024-11-19.csv',
    'livros_amazon_2024-11-20.csv',
    'livros_amazon_2024-11-21.csv',
    'livros_amazon_2024-11-22.csv',
    'livros_amazon_2024-11-23.csv',
    'livros_amazon_2024-11-24.csv',
    'livros_amazon_2024-11-25.csv',
    'livros_amazon_2024-11-26.csv',
    'livros_amazon_2024-11-27.csv',
    'livros_amazon_2024-11-28.csv',
    'livros_amazon_2024-11-29.csv'
]

arquivos_produtos = [
    'produtos_amazon_2024-11-16.csv',
    'produtos_amazon_2024-11-17.csv',
    'produtos_amazon_2024-11-18.csv',
    'produtos_amazon_2024-11-19.csv',
    'produtos_amazon_2024-11-20.csv',
    'produtos_amazon_2024-11-21.csv',
    'produtos_amazon_2024-11-22.csv',
    'produtos_amazon_2024-11-23.csv',
    'produtos_amazon_2024-11-24.csv',
    'produtos_amazon_2024-11-25.csv',
    'produtos_amazon_2024-11-26.csv',
    'produtos_amazon_2024-11-27.csv',
    'produtos_amazon_2024-11-28.csv',
    'produtos_amazon_2024-11-29.csv'
]

# Instanciando a classe de tranformação e carga
df = TransformerLoader()

# Juntar os arquivos de produtos da categoria livros
livros = df.join(arquivos_livro, 'livro')

# Juntar os arquivos de produtos de outras categorias
produtos = df.join(arquivos_produtos, 'produto')

# Juntando os dataframes da categoria livro e outros produtos
dataframe = pd.concat([livros, produtos], axis=0)

# Fazendo as transformações dos dados do dataframe
base = df.transformer(dataframe)

# Fazendo a carga dos dados, transformando o dataframe em um arquivo csv
df.loader(base)