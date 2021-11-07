from pydantic import BaseModel, Field

from app import PyObjectId


class DeclaracaoObito(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    idade: int = Field(...)
    sexo: chr = Field(...)
    raca_cor: str = Field(...)
    escolaridade: str = Field(...)
    local_ocorrencia: str = Field(...)
    teve_assistencia_medica: bool = Field(...)
    dia_obito: int = Field(...)
    mes_obito: int = Field(...)
    ano_obito: int = Field(...)
    estado: str = Field(...)
    grupo_causa_basica: str = Field(...)
    causa_basica: str = Field(...)
    ocupacao: str = Field(...)
    grupo_ocupacao: str = Field(...)
