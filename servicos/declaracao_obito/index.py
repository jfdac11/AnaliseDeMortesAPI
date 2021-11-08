from singleton import SingletonMeta
from config.conexao_bd import db


class ServicoDeclaracaoObito(metaclass=SingletonMeta):
    async def listar_declaracoes_obito(self, ano: str, limite: int, pagina: int):
        declaracoes_obito = await db[ano].find().skip(pagina).limit(limite).to_list(limite)
        return declaracoes_obito
