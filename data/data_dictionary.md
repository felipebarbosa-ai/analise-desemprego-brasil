
# Dicionário de Dados

## Identificação

- **Projeto:** Análise da Evolução da Taxa de Desocupação no Brasil
- **Instituição:** Unilasalle
- **Autores:** Felipe Barbosa da Silva e Luis Fernando Dantas
- **Fonte:** Instituto Brasileiro de Geografia e Estatística (IBGE)
- **Pesquisa:** Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua)
- **Base:** SIDRA, tabela 4099
- **Indicador:** Taxa de desocupação
- **Abrangência:** Brasil
- **Periodicidade:** Trimestral

## Referências oficiais

- [IBGE — Indicadores: Desemprego](https://www.ibge.gov.br/indicadores#desemprego)
- [IBGE — SIDRA, tabela 4099](https://sidra.ibge.gov.br/tabela/4099)

## Arquivos de dados

| Arquivo | Descrição |
|---|---|
| `dados_sidra_4099.json` | Dados originais coletados da API do SIDRA |
| `taxa_desocupacao_brasil.csv.gz` | Dados tratados e organizados em CSV compactado |
| `estatisticas_descritivas.json` | Estatísticas descritivas da série analisada |

## Descrição das variáveis

| Variável | Tipo | Descrição |
|---|---|---|
| `data` | Data | Data de início do trimestre de referência |
| `ano` | Inteiro | Ano de referência |
| `trimestre` | Inteiro | Número do trimestre (1 a 4) |
| `taxa_desocupacao` | Decimal | Taxa de desocupação expressa em porcentagem |

## Tratamento dos dados

O processo de tratamento contempla:

1. Conversão dos dados JSON para uma tabela.
2. Extração do ano e do trimestre a partir do código de período do IBGE.
3. Conversão dos valores para formato numérico.
4. Remoção de registros sem valores válidos.
5. Construção da variável de data.
6. Ordenação cronológica dos registros.
7. Remoção de períodos duplicados.

## Formato e acesso

Os dados processados são disponibilizados em CSV compactado com gzip (`.csv.gz`), formato aberto e adequado para análise em Python.

Os dados originais são preservados em JSON para permitir rastreabilidade e reprodutibilidade da coleta.

## Licença e atribuição

Os dados são provenientes do IBGE. A utilização deve manter a atribuição à instituição responsável pela produção e divulgação das informações.

Fonte: Instituto Brasileiro de Geografia e Estatística (IBGE), Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua).
