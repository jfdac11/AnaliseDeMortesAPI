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
async def num_declaracoes_obito(ano: str, tipo_grafico: str):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    num_declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_ano(ano, tipo_grafico)
    return num_declaracoes_obito
