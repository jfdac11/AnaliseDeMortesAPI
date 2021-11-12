from adapters.listar_declaracoes_ano import ListarDeclaracoes

class GraficoEixosAdapter(ListarDeclaracoes):

    def gerar_eixo(self, lista, chave):
        eixo = []
        for item in lista:
            eixo.append(item[chave])
        return eixo

    async def gerar_grafico(self, ano: str, match: object = None):
        eixos = []
        res_aggregate = await self.aggregate(ano, match)
        chaves = res_aggregate[0].keys();
        for chave in chaves:
            eixo = self.gerar_eixo(res_aggregate, chave)
            eixos.append(eixo)
        return eixos
