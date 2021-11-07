from fastapi import FastAPI
from typing import List, Optional
from models.declaracao_obito import DeclaracaoObitoModel
from config.conexao_bd import db

app = FastAPI()


@app.get(
    "/DeclaracoesObito", response_description="Listar todas as declarações de óbito", response_model=List[DeclaracaoObitoModel]
)
async def listar_declaracoes_obito(ano: str, limit: int, skip: int):
    declaracoes_obito = await db[ano].find().skip(skip).limit(limit).to_list(limit)
    return declaracoes_obito
