
"""
Projeto: Análise da Evolução da Taxa de Desocupação no Brasil
Autores: Felipe Barbosa da Silva e Luis Fernando Dantas
Instituição: Unilasalle

Fonte de referência:
IBGE - Indicador de Desemprego
https://www.ibge.gov.br/indicadores#desemprego

Fonte de dados:
IBGE - PNAD Contínua / SIDRA
Tabela 4099
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd
import requests


ROOT = Path(__file__).resolve().parents[1]

URL = "https://apisidra.ibge.gov.br/values/t/4099/n1/1/v/4099/p/all"

PASTA_RAW = ROOT / "data" / "raw"
PASTA_PROCESSED = ROOT / "data" / "processed"

PASTA_RAW.mkdir(parents=True, exist_ok=True)
PASTA_PROCESSED.mkdir(parents=True, exist_ok=True)


def coletar_dados():
    print("Coletando dados oficiais do IBGE...")

    resposta = requests.get(URL, timeout=120)
    resposta.raise_for_status()

    dados = resposta.json()

    if not dados or len(dados) < 2:
        raise ValueError("A API não retornou dados suficientes.")

    arquivo = PASTA_RAW / "dados_sidra_4099.json"

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"Dados originais salvos em: {arquivo}")

    return dados


def tratar_dados(dados):
    df = pd.DataFrame(dados[1:]).rename(columns=dados[0])

    coluna_periodo = "Trimestre (Código)"
    coluna_valor = "Valor"

    if coluna_periodo not in df.columns or coluna_valor not in df.columns:
        raise ValueError(
            "Estrutura inesperada da API. "
            f"Colunas recebidas: {list(df.columns)}"
        )

    codigo = df[coluna_periodo].astype(str)

    df["ano"] = pd.to_numeric(
        codigo.str[:4], errors="coerce"
    )

    df["trimestre"] = pd.to_numeric(
        codigo.str[4:], errors="coerce"
    )

    df["taxa_desocupacao"] = pd.to_numeric(
        df[coluna_valor].astype(str).str.replace(",", ".", regex=False),
        errors="coerce"
    )

    df = df.dropna(
        subset=["ano", "trimestre", "taxa_desocupacao"]
    ).copy()

    df["ano"] = df["ano"].astype(int)
    df["trimestre"] = df["trimestre"].astype(int)

    df = df[df["trimestre"].between(1, 4)]

    df["data"] = pd.to_datetime(
        df["ano"].astype(str)
        + "-"
        + ((df["trimestre"] - 1) * 3 + 1).astype(str).str.zfill(2)
        + "-01"
    )

    df = df[
        ["data", "ano", "trimestre", "taxa_desocupacao"]
    ]

    df = df.sort_values("data").reset_index(drop=True)
    df = df.drop_duplicates(subset=["data"])

    return df


def salvar_dados(df):
    destino = (
        PASTA_PROCESSED
        / "taxa_desocupacao_brasil.csv.gz"
    )

    df.to_csv(
        destino,
        index=False,
        encoding="utf-8",
        compression="gzip"
    )

    print(f"Base tratada salva em: {destino}")


def gerar_estatisticas(df):
    estatisticas = {
        "quantidade_registros": int(len(df)),
        "primeiro_periodo": str(df["data"].min().date()),
        "ultimo_periodo": str(df["data"].max().date()),
        "media": float(df["taxa_desocupacao"].mean()),
        "mediana": float(df["taxa_desocupacao"].median()),
        "desvio_padrao": float(df["taxa_desocupacao"].std()),
        "menor_taxa": float(df["taxa_desocupacao"].min()),
        "maior_taxa": float(df["taxa_desocupacao"].max()),
        "data_menor_taxa": str(
            df.loc[df["taxa_desocupacao"].idxmin(), "data"].date()
        ),
        "data_maior_taxa": str(
            df.loc[df["taxa_desocupacao"].idxmax(), "data"].date()
        ),
        "data_coleta": datetime.now().astimezone().isoformat()
    }

    destino = (
        PASTA_PROCESSED
        / "estatisticas_descritivas.json"
    )

    with open(destino, "w", encoding="utf-8") as f:
        json.dump(
            estatisticas,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("\nESTATÍSTICAS DESCRITIVAS")

    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")


def executar_pipeline():
    dados = coletar_dados()

    df = tratar_dados(dados)

    if df.empty:
        raise ValueError("Nenhum dado válido foi encontrado.")

    salvar_dados(df)
    gerar_estatisticas(df)

    print("\nPipeline executado com sucesso!")
    print(f"Total de registros: {len(df)}")


if __name__ == "__main__":
    executar_pipeline()
