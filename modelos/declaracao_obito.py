from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from modelos.py_object_id import PyObjectId


class DeclaracaoObitoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    idade: Optional[int] = Field(None)
    sexo: Optional[str] = Field(None)
    mes_obito: Optional[str] = Field(None)
    raca_cor: Optional[str] = Field(None)
    escolaridade: Optional[str] = Field(None)
    estado: Optional[str] = Field(None)
    codigo_estado: Optional[str] = Field(None)
    cod_grupo_causa_basica: Optional[str] = Field(None)
    cod_causa_basica: Optional[str] = Field(None)
    cod_capitulo_causa_basica: Optional[str] = Field(None)
    codigo_grupo_ocupacao: Optional[str] = Field(None)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
