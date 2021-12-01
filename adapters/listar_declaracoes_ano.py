from config.conexao_bd import db


class ListarDeclaracoes:

    async def aggregate(self, ano: str, pipeline: list):
        data = []
        async for item in db[ano].aggregate(pipeline):
            data.append(item)
        return data
