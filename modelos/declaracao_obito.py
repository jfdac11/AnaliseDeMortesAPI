from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from modelos.py_object_id import PyObjectId


class DeclaracaoObitoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    SEXO: Optional[str] = Field(None)
    RACACOR: Optional[str] = Field(None)
    ESC2010: Optional[str] = Field(None)
    LOCOCOR: Optional[str] = Field(None)
    CODMUNOCOR: Optional[str] = Field(None)
    DIA_OBITO: Optional[str] = Field(None)
    MES_OBITO: Optional[str] = Field(None)
    ANO_OBITO: Optional[str] = Field(None)
    ESTADO: Optional[str] = Field(None)
    GRUPO_CAUSA_BASICA: Optional[str] = Field(None)
    CAUSA_BASICA: Optional[str] = Field(None)
    OCUPACAO: Optional[str] = Field(None)
    GRUPO_OCUPACAO: Optional[str] = Field(None)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# class DeclaracaoObitoModel(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     idade: Optional[str] = Field(None)
#     sexo: Optional[str] = Field(None)
#     raca_cor: Optional[str] = Field(None)
#     escolaridade: Optional[str] = Field(None)
#     local_ocorrencia: Optional[str] = Field(None)
#     teve_assistencia_medica: Optional[str] = Field(None)
#     dia_obito: Optional[str] = Field(None)
#     mes_obito: Optional[str] = Field(None)
#     ano_obito: Optional[str] = Field(None)
#     estado: Optional[str] = Field(None)
#     grupo_causa_basica: Optional[str] = Field(None)
#     causa_basica: Optional[str] = Field(None)
#     ocupacao: Optional[str] = Field(None)
#     grupo_ocupacao: Optional[str] = Field(None)
