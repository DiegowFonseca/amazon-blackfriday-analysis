from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import os
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

urls = [
    'https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_electronics_sm',
    'https://www.amazon.com.br/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm',
    'https://www.amazon.com.br/gp/bestsellers/fashion/ref=zg_bs_fashion_sm',
    'https://www.amazon.com.br/gp/bestsellers/furniture/ref=zg_bs_furniture_sm'
]

# Inicializa um DataFrame vazio
df_produtos = pd.DataFrame(columns=['nome', 'preco', 'classificado', 'categoria', 'site', 'data_raspagem'])

for url in urls:
    driver.get(url)

    categoria = url.split('/')[-2]
    site = 'Amazon'

    while True:
        # Rolando a página para carregar mais produtos
        for _ in range(5):  # Ajuste o número de rolagens
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        # Aguarda que os produtos sejam carregados
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.ID, "gridItemRoot")))

        # Localiza os o conteiners dos produtos
        itens = driver.find_elements(By.XPATH, '//*[@id="gridItemRoot"]')

        for item in itens:
            try:
                nome_produto = item.find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text
                preco_produto = item.find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-price_3mJ9Z').text
                classificado = item.find_element(By.CLASS_NAME, 'zg-bdg-text').text
                data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                df_produtos = pd.concat([df_produtos, pd.DataFrame({
                    'nome': [nome_produto],
                    'preco': [preco_produto],
                    'classificado': [classificado],
                    'categoria': [categoria],
                    'site': [site],
                    'data_raspagem': [data_hora]
                })], ignore_index=True)
                
            except Exception as e:
                print(f"Erro para encontrar item {e}")

        # Tenta encontrar o botão "Próxima página"
        try:
            botao_proxima_pagina = driver.find_element(By.XPATH, '//li[@class="a-last"]/a')
            if not botao_proxima_pagina.is_displayed():
                break
            botao_proxima_pagina.click()
            time.sleep(3)
        except:
            print("Não foi possível encontrar o botão da próxima página!")
            break

driver.close()

diretorio = '../../data/data_raw/produtos_amazon'
os.makedirs(diretorio, exist_ok=True)

df_produtos.to_csv(f"{diretorio}/produtos_amazon_{datetime.now().strftime('%Y-%m-%d')}.csv", index=False, encoding='utf-8')

print("Raspagem concluida e salvo em arquivo CSV.")



