# Análise da Evolução da Taxa de Desocupação no Brasil

Projeto acadêmico desenvolvido em Python para analisar a evolução da taxa de desocupação no Brasil, utilizando dados oficiais da PNAD Contínua, disponibilizados pelo Instituto Brasileiro de Geografia e Estatística (IBGE).

## 1. Sobre o projeto

Este projeto tem como objetivo analisar a evolução da taxa de desocupação no Brasil, identificando tendências históricas, variações ao longo dos anos e a distribuição dos valores observados.

A análise utiliza dados trimestrais da PNAD Contínua, obtidos por meio da API SIDRA do IBGE, tabela 4099.

## 2. Autores

- Felipe Barbosa da Silva
- Luis Fernando Dantas

**Instituição:** Unilasalle  
**Curso:** Sistemas de Informação  
**Disciplina:** Linguagens de Programação — 6º Período

## 3. Fonte dos dados

Os dados utilizados foram obtidos por meio da API SIDRA do IBGE.

- **Instituição:** Instituto Brasileiro de Geografia e Estatística (IBGE).
- **Pesquisa:** PNAD Contínua.
- **Tabela:** 4099.
- **Indicador:** Taxa de desocupação.
- **Abrangência:** Brasil.
- **Periodicidade:** Trimestral.

Fonte: [IBGE — Indicadores de Desemprego](https://www.ibge.gov.br/indicadores#desemprego)

Tabela utilizada: [SIDRA — Tabela 4099](https://sidra.ibge.gov.br/tabela/4099)

## 4. Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Requests
- Jupyter Notebook
- Git e GitHub

## 5. Estrutura do projeto

```text
analise-desemprego-brasil/
├── data/
│   ├── raw/
│   ├── processed/
│   └── data_dictionary.md
├── docs/
│   ├── assets/
│   └── index.html
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   └── etl.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 6. Metodologia

O desenvolvimento foi dividido nas seguintes etapas:

1. **Coleta:** obtenção dos dados da PNAD Contínua por meio da API SIDRA.
2. **Armazenamento bruto:** salvamento dos dados originais em formato JSON.
3. **Tratamento:** organização dos dados, conversão dos tipos e identificação dos períodos.
4. **Armazenamento processado:** exportação dos dados tratados em CSV compactado com gzip.
5. **Análise exploratória:** cálculo de estatísticas descritivas e análise da evolução histórica.
6. **Visualização:** elaboração de gráficos para facilitar a interpretação dos resultados.

## 7. Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/felipebarbosa-ai/analise-desemprego-brasil.git
```

Entre na pasta do projeto:

```bash
cd analise-desemprego-brasil
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline ETL:

```bash
python src/etl.py
```

Para visualizar a análise exploratória, abra o arquivo:

```text
notebooks/analise_exploratoria.ipynb
```

## 8. Resultados

A análise exploratória contemplou 58 registros trimestrais, abrangendo o período do primeiro trimestre de 2012 ao segundo trimestre de 2026.

Principais resultados:

- **Média geral:** 9,57%.
- **Mediana:** 8,75%.
- **Desvio padrão:** aproximadamente 2,87 pontos percentuais.
- **Maior taxa:** 14,9%, no terceiro trimestre de 2020.
- **Menor taxa:** 5,1%, no quarto trimestre de 2025.

Os resultados foram apresentados por meio de gráficos de evolução histórica, médias anuais e distribuição das taxas.

Observação: o ano de 2026 contempla apenas os dois primeiros trimestres da série analisada.

## 9. Dicionário de dados

As informações sobre as variáveis utilizadas, seus significados, formatos e origem estão documentadas no arquivo:

`data/data_dictionary.md`

## 10. Licença

Este projeto utiliza a licença MIT para o código-fonte. Consulte o arquivo `LICENSE` para mais informações.

## 11. Reprodutibilidade e princípios FAIR

O projeto busca seguir os princípios FAIR:

- **Findable (Localizável):** organização e identificação dos arquivos e documentação.
- **Accessible (Acessível):** disponibilização pública do código e dos dados no GitHub.
- **Interoperable (Interoperável):** utilização de formatos como JSON, CSV e Markdown.
- **Reusable (Reutilizável):** disponibilização dos scripts, notebook, documentação e dependências para facilitar a reprodução da análise.

## 12. Publicação

O artigo acadêmico está publicado no GitHub Pages e pode ser acessado pelo link:

**[Acessar artigo acadêmico — Análise da Evolução da Taxa de Desocupação no Brasil](https://felipebarbosa-ai.github.io/analise-desemprego-brasil/)**

O código-fonte, os dados e a documentação estão disponíveis no repositório:

[https://github.com/felipebarbosa-ai/analise-desemprego-brasil](https://github.com/felipebarbosa-ai/analise-desemprego-brasil)
