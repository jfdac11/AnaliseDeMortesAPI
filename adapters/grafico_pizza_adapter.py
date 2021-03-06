from adapters.i_adapter import IAdapter
from adapters.listar_declaracoes_ano import ListarDeclaracoes


class GraficoPizzaAdapter(ListarDeclaracoes, IAdapter):

    def gerar_eixo(self, lista, chave):
        eixo = []
        for item in lista:
            eixo.append(item[chave])
        return eixo

    async def gerar_exibicao(self, ano: str, pipeline: list):
        eixos = []
        res_aggregate = await self.aggregate(ano, pipeline)
        if(res_aggregate):
            chaves = res_aggregate[0].keys()
            for chave in chaves:
                eixo = self.gerar_eixo(res_aggregate, chave)
                eixos.append(eixo)
        return eixos
