from fastapi import FastAPI
from typing import List
from modelos.declaracao_obito import DeclaracaoObitoModel
from servicos.declaracao_obito.index import ServicoDeclaracaoObito

app = FastAPI()


@app.get(
    "/DeclaracoesObito", response_description="Listar todas as declarações de óbito", response_model=List[DeclaracaoObitoModel]
)
async def listar_declaracoes_obito(ano: str, limite: int, pagina: int):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_obito(ano, limite, pagina)
    return declaracoes_obito


@app.get(
    "/NumDeclaracoesObitoMesais", response_description="Listar numero de declarações mensais"
)
async def num_declaracoes_obito(ano: str):
    print(ano)
    servico_declaracao_obito = ServicoDeclaracaoObito()
    num_declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_ano(ano)
    return num_declaracoes_obito


