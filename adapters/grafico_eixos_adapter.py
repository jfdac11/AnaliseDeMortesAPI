from adapters.i_adapter import IAdapter
from adapters.listar_declaracoes_ano import ListarDeclaracoes


class GraficoEixosAdapter(ListarDeclaracoes, IAdapter):

    def gerar_eixo(self, lista, chave):
        eixo = []
        for item in lista:
            eixo.append(item[chave])
        return eixo

    async def gerar_exibicao(self, ano: str, pipeline: list):
        eixos = {
            "x": [],
            "y": []
        }
        res_aggregate = await self.aggregate(ano, pipeline)
        eixos["x"] = self.gerar_eixo(res_aggregate, "_id")
        eixos["y"] = self.gerar_eixo(res_aggregate, "count")
        return eixos
