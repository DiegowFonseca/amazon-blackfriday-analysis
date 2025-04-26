# Análise do Impacto da Black Friday nos Produtos Mais Vendidos da Amazon 

## Descrição  
Este projeto analisa o impacto da Black Friday sobre os produtos mais vendidos na Amazon, investigando variações de preços, mudanças no ranking de vendas e padrões de consumo antes e durante o evento.  

Os dados foram coletados via **web scraping com Selenium**, considerando os **100 produtos mais vendidos de cinco categorias**, durante **14 dias (13 dias antes da Black Friday e no próprio dia da Black Friday)**.  

---

## Problema a ser resolvido  
A Black Friday é um dos eventos de compras mais movimentados do ano, mas como ela realmente afeta os preços e a popularidade dos produtos? Este projeto busca responder perguntas como:  


- **Os preços dos produtos variaram significativamente na Black Friday?**
- **Produtos populares mantêm sua posição no ranking ao longo do tempo?**
- **Algumas categorias se destacam mais na Black Friday?**
- **Existe correlação entre preço e ranking de vendas?**
- **O impacto da Black Friday nos preços é superior ao de outros dias da semana?**

---



## Como executar o projeto 

### **Pré-requisitos**  
Certifique-se de ter o **Python 3.x** instalado, junto com os pacotes necessários.  

Instale as dependências com:  

```bash
pip install -r requirements.txt
```

---

## Como rodar o código

### 1 Coletar dados da Amazon (Web Scraping)
Execute o script de raspagem de dados de livros:

```bash
python src/extraction/books_scraper.py
```

Os dados serão salvos em  **data/data_raw/livros_amazon**

Execute o script de raspagem de dados dos produtos de outras categorias:

```bash
python src/estraction/products_scraper.py
```

Os dados serão salvos em  **data/data_raw/produtos_amazon**


### 2 Fazer a transformação dos dados e o carregamento em um arquivo csv
Execute o script de transformação dos dados:

```bash
python src/main.py
```

Os dados serão salvos em  **data/data_processed/produtos.csv**


### 3 Análise dos dados
Após coletar os dados e transformar, execute a análise exploratória:

```bash
python notebooks/analysis_exploratory.ipynb
```

Isso gerará gráficos e estatísticas para avaliar padrões nos preços, rankings e categorias.

---

## Tecnologias utilizadas

- **Python**
- **Selenium** (Web Scraping)
- **Pandas** (Manipulação de Dados)
- **Matplotlib / Seaborn** (Visualização)
- **Jupyter Notebook** (Análise Exploratória)

---

## Análises e Conclusões

### Variação dos preços

- Quando analisamos todos os produtos, **não houve uma variação significativa nos preços durante a Black Friday**, exceto para **eletrônicos**, onde os preços médios aumentaram nos dias próximos à Black Friday.

- Para os produtos **Top 10**, houve **um aumento significativo nos preços médios na Black Friday**, em várias categorias.

- **Livros foram a única categoria sem grandes variações de preço ao longo dos dias.**


### Popularidade dos produtos

- Alguns produtos mantiveram sua posição de destaque ao longo dos 14 dias analisados. O **Echo Dot 5ª geração** ficou em **1º lugar** na categoria de eletrônicos durante todo o período, enquanto o **Echo Pop** ficou em 2º.

- O **Vonder Banqueta Plástica** subiu no ranking e se tornou o **número 1** na categoria de mobília no dia da Black Friday.


### Categorias mais impactadas

- **A categoria de mobília teve um desempenho melhor na Black Friday**, subindo no ranking médio.

- **Eletrônicos se manteve estável** ao longo do tempo.

- **A categoria de moda perdeu posições** no dia da Black Friday.


### Correlação entre preço e ranking

- Quando analisamos a **correlação de Pearson**, não encontramos uma relação forte entre **preço** e **posição no ranking**.

- **Nos dias antes da Black Friday, os produtos mais baratos tendiam a ocupar posições melhores no ranking**.

- **No dia da Black Friday, essa relação foi menos evidente, com produtos mais caros subindo para posições mais altas**.


### Influência do dia da semana

- A partir do dia **26 de novembro (três dias antes da Black Friday)**, os preços começaram a subir.

- **O maior preço médio de vendas foi registrado no dia da Black Friday**.

---

## Sugestões para os próximos anos

### Análise estratégica por categoria:
- Focar em categorias que tiveram alta estabilidade no ranking (ex: eletrônicos e mobília) para entender como essas marcas promovem seus produtos.

- Estudar o comportamento de categorias que perderam relevância, como fashion, para identificar possíveis fatores que impactaram suas vendas.

### Estudo do impacto do marketing e promoções:
- Explorar quais fatores influenciam produtos a permanecerem no top 10 e como isso pode ser replicado para outras categorias.

- Analisar os produtos que entraram e saíram do ranking para identificar padrões de comportamento dos consumidores.

### Aprofundamento na relação preço vs. ranking:
- Investigar por que produtos mais baratos perderam posições no ranking na Black Friday.

- Testar se descontos agressivos impactam diretamente a colocação no ranking ou se há outros fatores envolvidos.

---

## Referências

- [Amazon Best Sellers](https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers)

- [Documentação Selenium](https://selenium-python.readthedocs.io/)

- [Guia Pandas](https://pandas.pydata.org/docs/)

---

## Licença

Este projeto está sob a licença **MIT**.

---

## Autor

 **Diego Fonseca**

 **diegowfonseca14@gmail.com**