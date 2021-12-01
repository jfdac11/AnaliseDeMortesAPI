from factory.exibicao_factory import ExibicaoAdapterFactory
from singleton import SingletonMeta
from config.conexao_bd import db


class ServicoDeclaracaoObito(metaclass=SingletonMeta):
    async def listar_declaracoes_obito(self, ano: str, limite: int, pagina: int):
        declaracoes_obito = await db[ano].find().skip(pagina).limit(limite).to_list(limite)
        return declaracoes_obito

    async def listar_declaracoes_ano(self, ano: str, tipo_exibicao: str, sexo: str, raca_cor: str, escolaridade: str, estado: str, capitulo_cb: str, idade_inf: int, idade_sup: int):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)

        match = {}
        if (sexo):
            match["sexo"] = sexo
        if (raca_cor):
            match["raca_cor"] = raca_cor
        if (escolaridade):
            match["escolaridade"] = escolaridade
        if (estado):
            match["estado"] = estado
        if (capitulo_cb):
            match["cod_capitulo_causa_basica"] = capitulo_cb
        if (idade_inf):
            match["idade"] = {
                '$gte': idade_inf
            }
        if (idade_sup):
            match["idade"] = {
                '$lte': idade_sup
            }

        pipeline = [
            {
                '$match': match
            },
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

    async def listar_doencas_que_mais_mataram(self, ano: str, quantidade: int, tipo_exibicao: str, sexo: str, raca_cor: str, escolaridade: str, estado: str, capitulo_cb: str, idade_inf: int, idade_sup: int, mes_obito_inf: int, mes_obito_sup: int):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)

        match = {}
        if (sexo):
            match["sexo"] = sexo
        if (raca_cor):
            match["raca_cor"] = raca_cor
        if (escolaridade):
            match["escolaridade"] = escolaridade
        if (estado):
            match["estado"] = estado
        if (capitulo_cb):
            match["cod_capitulo_causa_basica"] = capitulo_cb
        if (idade_inf):
            match["idade"] = {
                '$gte': idade_inf
            }
        if (idade_sup):
            match["idade"] = {
                '$lte': idade_sup
            }
        if (mes_obito_inf):
            match["mes_obito"] = {
                '$gte': mes_obito_inf
            }
        if (mes_obito_sup):
            match["mes_obito"] = {
                '$lte': mes_obito_sup
            }

        pipeline = [
            {
                '$match': match
            },
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

    async def listar_mortes_por_estado(self, ano: str, tipo_exibicao: str, sexo: str, raca_cor: str, escolaridade: str, capitulo_cb: str, idade_inf: int, idade_sup: int, mes_obito_inf: int, mes_obito_sup: int):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)

        match = {}
        if (sexo):
            match["sexo"] = sexo
        if (raca_cor):
            match["raca_cor"] = raca_cor
        if (escolaridade):
            match["escolaridade"] = escolaridade
        if (capitulo_cb):
            match["cod_capitulo_causa_basica"] = capitulo_cb
        if (idade_inf):
            match["idade"] = {
                '$gte': idade_inf
            }
        if (idade_sup):
            match["idade"] = {
                '$lte': idade_sup
            }
        if (mes_obito_inf):
            match["mes_obito"] = {
                '$gte': mes_obito_inf
            }
        if (mes_obito_sup):
            match["mes_obito"] = {
                '$lte': mes_obito_sup
            }

        pipeline = [
            {
                '$match': match
            },
            {
                '$group': {
                    '_id': '$estado',
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$sort': {
                    'count': -1
                }
            }
        ]
        exibicao = await adapter.gerar_exibicao(ano, pipeline)
        return exibicao

    async def listar_mortes_por_raca_cor(self, ano: str, tipo_exibicao: str, sexo: str, escolaridade: str, estado: str, capitulo_cb: str, idade_inf: int, idade_sup: int, mes_obito_inf: int, mes_obito_sup: int):
        factory = ExibicaoAdapterFactory()
        adapter = factory.gerar_exibicao_adapter(tipo_exibicao)

        match = {}
        if (sexo):
            match["sexo"] = sexo
        if (escolaridade):
            match["escolaridade"] = escolaridade
        if (estado):
            match["estado"] = estado
        if (capitulo_cb):
            match["cod_capitulo_causa_basica"] = capitulo_cb
        if (idade_inf):
            match["idade"] = {
                '$gte': idade_inf
            }
        if (idade_sup):
            match["idade"] = {
                '$lte': idade_sup
            }
        if (mes_obito_inf):
            match["mes_obito"] = {
                '$gte': mes_obito_inf
            }
        if (mes_obito_sup):
            match["mes_obito"] = {
                '$lte': mes_obito_sup
            }

        pipeline = [
            {
                '$match': match
            },
            {
                '$group': {
                    '_id': '$raca_cor',
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$sort': {
                    'count': -1
                }
            }
        ]
        exibicao = await adapter.gerar_exibicao(ano, pipeline)
        return exibicao
