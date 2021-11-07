import os
from fastapi import FastAPI
from typing import List, Optional
import motor.motor_asyncio
from dotenv import load_dotenv
from models.declaracao_obito import DeclaracaoObitoModel

load_dotenv('./.env')

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.deathDB


@app.get(
    "/DeclaracoesObito", response_description="Listar todas as declarações de óbito", response_model=List[DeclaracaoObitoModel]
)
async def listar_declaracoes_obito(ano: str, limit: int, skip: int):
    declaracoes_obito = await db[ano].find().skip(skip).limit(limit).to_list(limit)
    return declaracoes_obito
