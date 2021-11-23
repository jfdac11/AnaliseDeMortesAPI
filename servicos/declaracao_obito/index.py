from factory.interface_factory import InterfaceFactory
from singleton import SingletonMeta
from config.conexao_bd import db


class ServicoDeclaracaoObito(metaclass=SingletonMeta):
    async def listar_declaracoes_obito(self, ano: str, limite: int, pagina: int):
        declaracoes_obito = await db[ano].find().skip(pagina).limit(limite).to_list(limite)
        return declaracoes_obito

    async def listar_declaracoes_ano(self, ano: str, tipo_grafico: str):
        factory = InterfaceFactory()
        adapter = factory.gerar_interface(tipo_grafico)
        pipeline = [
            {
                '$group': {
                    '_id': '$MES_OBITO',
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$sort': {
                    '_id': 1
                }
            }
        ]
        grafico = await adapter.gerar_grafico(ano, pipeline)
        return grafico
