# analise-desemprego-brasil
Análise da evolução da taxa de desocupação no Brasil utilizando dados da PNAD Contínua/IBGE. Visibility
# Análise da Evolução da Taxa de Desocupação no Brasil

## 1. Sobre o projeto

Este projeto tem como objetivo analisar a evolução da taxa de desocupação no Brasil, utilizando dados oficiais da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua), disponibilizados pelo Instituto Brasileiro de Geografia e Estatística (IBGE).

A análise busca identificar tendências históricas, variações ao longo dos anos e a distribuição da taxa de desocupação no período estudado.

## 2. Autores

- Felipe Barbosa da Silva
- Luis Fernando Dantas

**Instituição:** Unilasalle  
**Curso:** Sistemas de Informação

## 3. Fonte dos dados

Os dados utilizados foram obtidos por meio da API SIDRA do IBGE.

- **Instituição:** Instituto Brasileiro de Geografia e Estatística (IBGE).
- **Pesquisa:** PNAD Contínua.
- **Tabela:** 4099.
- **Indicador:** Taxa de desocupação.

Fonte: https://www.ibge.gov.br/indicadores#desemprego

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
4. **Armazenamento processado:** exportação dos dados tratados em CSV compactado.
5. **Análise exploratória:** cálculo de estatísticas descritivas e análise da evolução histórica.
6. **Visualização:** elaboração de gráficos para facilitar a interpretação dos resultados.

## 7. Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
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

A análise exploratória identificou:

- 58 registros trimestrais.
- Média geral da taxa de desocupação de aproximadamente 9,57%.
- Maior taxa observada de 14,9%.
- Menor taxa observada de 5,1%.

Os resultados e gráficos completos estão disponíveis no artigo acadêmico em HTML, localizado em `docs/index.html`.

## 9. Dicionário de dados

As informações sobre as variáveis utilizadas, seus significados e formatos estão documentadas no arquivo:

`data/data_dictionary.md`

## 10. Licença

Este projeto utiliza a licença MIT para o código-fonte. Consulte o arquivo `LICENSE` para mais informações.

## 11. Reprodutibilidade e princípios FAIR

O projeto busca seguir os princípios FAIR, promovendo a localização, acessibilidade, interoperabilidade e reutilização dos dados e códigos utilizados.

O código, os dados processados e a documentação estão organizados no repositório para facilitar a reprodução da análise.

## 12. Publicação

O artigo acadêmico pode ser acessado pelo arquivo ``. A publicação online será disponibilizada por meio do GitHub Pages.