from adapters.listar_declaracoes_ano import ListarDeclaracoes


class GraficoPizzaAdapter(ListarDeclaracoes):

    async def gerar_grafico(self, ano: str, match: object = None):
        res_aggregate = await self.aggregate(ano, match)
        return res_aggregate
