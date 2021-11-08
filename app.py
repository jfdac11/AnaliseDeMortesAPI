from fastapi import FastAPI
from typing import List, Optional
from modelos.declaracao_obito import DeclaracaoObitoModel
from config.conexao_bd import db
from servicos.declaracao_obito.index import ServicoDeclaracaoObito

app = FastAPI()


@app.get(
    "/DeclaracoesObito", response_description="Listar todas as declarações de óbito", response_model=List[DeclaracaoObitoModel]
)
async def listar_declaracoes_obito(ano: str, limite: int, pagina: int):
    servico_declaracao_obito = ServicoDeclaracaoObito()
    declaracoes_obito = await servico_declaracao_obito.listar_declaracoes_obito(ano, limite, pagina)
    return declaracoes_obito
