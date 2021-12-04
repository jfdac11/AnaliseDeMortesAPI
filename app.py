from fastapi import FastAPI
from typing import List
from modelos.declaracao_obito import DeclaracaoObitoModel
from servicos.declaracao_obito.index import ServicoDeclaracaoObito
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/DeclaracoesObito", response_description="Listar todas as declarações de óbito", response_model=List[DeclaracaoObitoModel]
)
async def listar_declaracoes_obito(ano: str, limite: int, pagina: int):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_obito(ano, limite, pagina)
    return declaracoes_obito


@app.get(
    "/NumDeclaracoesObitoMensais", response_description="Listar numero de declarações mensais"
)
async def num_declaracoes_obito(ano: str, tipo_exibicao: str, sexo: str = None, raca_cor: str = None, escolaridade: str = None, estado: str = None, capitulo_cb: str = None, idade_inf: int = None, idade_sup: int = None):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    num_declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_ano(ano, tipo_exibicao, sexo, raca_cor, escolaridade, estado, capitulo_cb, idade_inf, idade_sup)
    return num_declaracoes_obito


@app.get(
    "/DoencasQueMaisMataram", response_description="Listar as doenças que mais mataram"
)
async def listar_doencas_que_mais_mataram(ano: str, quantidade: int, tipo_exibicao: str, sexo: str = None, raca_cor: str = None, escolaridade: str = None, estado: str = None, capitulo_cb: str = None, idade_inf: int = None, idade_sup: int = None, mes_obito_inf: int = None, mes_obito_sup: int = None):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    doencas_letais = await servico_declaracao_obito.listar_doencas_que_mais_mataram(ano, quantidade, tipo_exibicao, sexo, raca_cor, escolaridade, estado, capitulo_cb, idade_inf, idade_sup, mes_obito_inf, mes_obito_sup)
    return doencas_letais


@app.get(
    "/MortesPorEstado", response_description="Listar a quantidade de mortes por estado"
)
async def listar_mortes_por_estado(ano: str, tipo_exibicao: str, sexo: str = None, raca_cor: str = None, escolaridade: str = None, capitulo_cb: str = None, idade_inf: int = None, idade_sup: int = None, mes_obito_inf: int = None, mes_obito_sup: int = None):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    mortes_estado = await servico_declaracao_obito.listar_mortes_por_estado(ano, tipo_exibicao, sexo, raca_cor, escolaridade, capitulo_cb, idade_inf, idade_sup, mes_obito_inf, mes_obito_sup)
    return mortes_estado


@app.get(
    "/MortesPorRacaCor", response_description="Listar a quantidade de mortes por raça ou cor"
)
async def listar_mortes_por_raca_cor(ano: str, tipo_exibicao: str, sexo: str = None, escolaridade: str = None, estado: str = None, capitulo_cb: str = None, idade_inf: int = None, idade_sup: int = None, mes_obito_inf: int = None, mes_obito_sup: int = None):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    mortes_raca_cor = await servico_declaracao_obito.listar_mortes_por_raca_cor(ano, tipo_exibicao, sexo, escolaridade, estado, capitulo_cb, idade_inf, idade_sup, mes_obito_inf, mes_obito_sup)
    return mortes_raca_cor


@app.get(
    "/DiferencaMortes", response_description="Procura as doenças com maior diferença nas taxas de mortalidade entre os anos de 2019 e 2020"
)
async def diferenca_mortes(quantidade: int):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    doencas_diferentes = await servico_declaracao_obito.diferenca_mortes(quantidade)
    return doencas_diferentes
