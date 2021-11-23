from adapters.i_adapter import IAdapter
from adapters.listar_declaracoes_ano import ListarDeclaracoes


class GraficoPizzaAdapter(ListarDeclaracoes, IAdapter):

    async def gerar_grafico(self, ano: str, pipeline: list):
        res_aggregate = await self.aggregate(ano, pipeline)
        return res_aggregate
