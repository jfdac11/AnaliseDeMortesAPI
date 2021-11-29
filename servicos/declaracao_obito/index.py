from factory.exibicao_factory import ExibicaoAdapterFactory
from singleton import SingletonMeta
from config.conexao_bd import db


class ServicoDeclaracaoObito(metaclass=SingletonMeta):
    async def listar_declaracoes_obito(self, ano: str, limite: int, pagina: int):
        declaracoes_obito = await db[ano].find().skip(pagina).limit(limite).to_list(limite)
        return declaracoes_obito

    async def listar_declaracoes_ano(self, ano: str, tipo_exibicao: str):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)
        pipeline = [
            {
                '$group': {
                    '_id': '$mes_obito',
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
        exibicao = await adapter.gerar_exibicao(ano, pipeline)
        return exibicao

    async def listar_doencas_que_mais_mataram(self, ano: str, quantidade: int, tipo_exibicao: str):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)
        pipeline = [
            {
                '$group': {
                    '_id': '$cod_causa_basica',
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$sort': {
                    'count': -1
                }
            },
            {
                '$limit': quantidade
            }
        ]
        exibicao = await adapter.gerar_exibicao(ano, pipeline)
        return exibicao
