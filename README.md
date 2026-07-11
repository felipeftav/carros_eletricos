# ⚡ Análise da Evolução e Modelagem Preditiva da Frota Eletrificada (SP)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-darkblue.svg)](https://pandas.pydata.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)](https://scikit-learn.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-purple.svg)](https://plotly.com)

![Evolução da Frota Elétrica em SP](Electric_fleet_growth_SP.jpeg)

Este projeto realiza o pipeline completo de dados — desde a coleta automatizada (*Web Scraping*) até a modelagem preditiva (*Forecasting*) — para analisar o crescimento de veículos híbridos e elétricos na cidade de São Paulo. O objetivo é transformar dados públicos brutos em insights estratégicos sobre transição energética e infraestrutura urbana.

---

## 📌 Contexto de Negócio

A cidade de São Paulo vive uma transição energética acelerada, impulsionada por incentivos fiscais (como a restituição da quota municipal do IPVA e a isenção do rodízio para veículos eletrificados). 

Para montadoras, empresas de energia e gestores públicos, entender a velocidade desse crescimento é crucial para prever a demanda por eletropostos, planejar a infraestrutura de recarga urbana e mitigar o risco de sobrecarga na rede elétrica local.

---

## 🛠️ Arquitetura do Projeto & Pipeline

O projeto foi dividido de forma modular, seguindo as melhores práticas de organização de repositórios de Ciência de Dados:

1. **`src/00_scraping.py`**: Script automatizado utilizando `BeautifulSoup` e `Requests` para varrer o portal da Senatran, contornar mudanças dinâmicas de URLs usando validação por substrings (`in`), identificar e baixar os arquivos brutos `.xlsx`.
2. **`notebooks/01_eda.ipynb`**: Notebook responsável pelo pipeline de ETL, engenharia de atributos temporais, cálculo de métricas de aceleração de mercado (**MoM** e **YoY**), visualização interativa com `Plotly` e o modelo preditivo.
3. **`data/`**: Diretório local (ignorado no Git) que armazena os arquivos históricos consolidados mensais.

---

## 📈 Principais Insights de Negócio (Storytelling)

### 1. Aceleração Exponencial do Mercado
A frota total de veículos eletrificados na capital paulista apresentou um crescimento agressivo e sem sinais de estagnação, saltando de **31.656 veículos em Janeiro de 2024** para **107.519 veículos em Junho de 2026**. Isso representa que a frota **mais que triplicou (um aumento de ~240%)** em um intervalo de apenas 30 meses.

### 2. Dominância Tecnológica e Transição Energética
Através do gráfico de áreas empilhadas (`Plotly`), conseguimos identificar o comportamento de adoção do consumidor paulistano:
* Os veículos **Híbridos** e **Híbridos Plug-in** ainda funcionam como a principal tecnologia de transição por mitigarem a ansiedade de autonomia (*range anxiety*) gerada pela atual escassez de carregadores rápidos nas rodovias.
* Contudo, a curva de crescimento de veículos **Elétricos Puros (BEV)** apresenta uma inclinação mais acentuada nos últimos meses, indicando que o ganho de eficiência e a expansão de carregadores privados (em condomínios e shoppings) começam a acelerar a substituição dos híbridos convencionais.

### 3. Previsão de Impacto na Infraestrutura Urbana (Forecasting)
Utilizando um modelo de **Regressão Linear** treinado com a série histórica cronológica, projetamos a demanda da frota até **Dezembro de 2027**:

* **O Marco dos 150K:** O modelo projeta com precisão matemática em qual trimestre de 2027 a capital paulista romperá a barreira histórica de **150.000 veículos eletrificados ativos nas ruas**.
* **Alerta de Negócio:** Esse crescimento linearizado serve como um indicador de urgência para concessionárias de energia e empresas de carregamento rápido: a velocidade de implementação de eletropostos públicos precisa acompanhar essa inclinação, sob o risco de estrangulamento da infraestrutura de recarga da cidade.

---

## 💻 Tecnologias e Técnicas Utilizadas

* **Manipulação de Dados Avançada:** `Pandas` (uso de indexação booleana bitwise, operações vetorizadas com `.isin()`, agrupamentos complexos com `.groupby()` e cálculos de taxas com `.pct_change(periods=12)`).
* **Gestão de Caminhos Robusta:** `pathlib` para garantir a portabilidade do código entre diferentes sistemas operacionais (Windows/Linux) sem quebrar caminhos relativos de pastas (`../data`).
* **Visualização Dinâmica:** `Plotly Express` e `Graph Objects` para gerar gráficos interativos ideais para apresentações executivas.
* **Ciência de Dados / ML:** `Scikit-Learn` para modelagem estatística e projeção de tendências lineares.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)