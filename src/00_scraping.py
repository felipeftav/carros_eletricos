import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from urllib.parse import urlparse

anos = ['2024', '2025', '2026']

for ano in anos:
    url = f"https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-Senatran/frota-de-veiculos-{ano}" 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # CORREÇÃO 1: Nome único para a sua lista final de download
    links_filtrados = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        titulo_pagina = soup.find("title").text
        print(f"Título do Site: {titulo_pagina}\n")

        # O BeautifulSoup usa esta variável para controlar o loop
        links_do_site = soup.find_all("a", class_="internal-link")
        
        for i, link in enumerate(links_do_site, 1):
            href = link.get('href')
            href_text = str(href)
            # 
            # Verifica se começa exatamente com essa base
            # base_url = 'https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-Senatran/D_Frota_por_UF_Municipio_COMBUSTIVEL'
            # if href_text.startswith(base_url):
            #     print("É um link oficial do Gov.br")
            #     nome_link = link.text.strip() 
            #     print(f"Link {i} [{nome_link}]: {href}")
                
            #     # Alimenta a lista correta sem quebrar o loop
            #     links_filtrados.append(href)
                
            base_url = 'D_Frota_por_UF_Municipio_COMBUSTIVEL'
            
            if base_url in href_text:
                print("É um link oficial do Gov.br")
                nome_link = link.text.strip() 
                print(f"Link {i} [{nome_link}]: {href}")
                
                # Alimenta a lista correta sem quebrar o loop
                links_filtrados.append(href)

    else:
        print(f"Erro ao acessar o site. Status code: {response.status_code}")
        
    for url_planilha in links_filtrados:
        # Pega o segundo link da lista (Novembro_2024.xlsx)
        print(f"\nBaixando a planilha de forma segura: {url_planilha}")

        # 1. Extrai o nome do arquivo diretamente da URL de forma automática
        # urlparse(".../arquivo.xlsx").path vai dar "/.../arquivo.xlsx"
        # os.path.basename pega só o final: "D_Frota_por_UF_Municipio_COMBUSTIVEL_Novembro_2024.xlsx"
        nome_arquivo = os.path.basename(urlparse(url_planilha).path)

        # 2. Garante que a pasta 'data' existe no seu projeto (se não existir, ele cria)
        pasta_destino = "data"
        os.makedirs(pasta_destino, exist_ok=True)

        # 3. Define o caminho completo onde o arquivo será salvo
        caminho_salvamento = os.path.join(pasta_destino, nome_arquivo)

        # Faz o download dos bytes
        response_excel = requests.get(url_planilha, headers=headers)

        if response_excel.status_code == 200:
            # 4. Salva o arquivo baixado diretamente na pasta 'data'
            with open(caminho_salvamento, "wb") as f:
                f.write(response_excel.content)
            print(f"Arquivo salvo com sucesso em: {caminho_salvamento}")
            
            # # 5. Carrega no Pandas lendo direto do arquivo local que acabou de ser salvo
            # df = pd.read_excel(caminho_salvamento)
            # print("\nPlanilha carregada no DataFrame!")
            # print(df.head())
        else:
            print(f"Não foi possível baixar a planilha. Status: {response_excel.status_code}")