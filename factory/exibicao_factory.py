from adapters.grafico_eixos_adapter import GraficoEixosAdapter
from adapters.grafico_pizza_adapter import GraficoPizzaAdapter
from adapters.i_adapter import IAdapter
from fastapi import HTTPException


class ExibicaoAdapterFactory:

    def gerar_exibicao_adapter(self, tipo_exibicao: str) -> IAdapter:
        if tipo_exibicao == "GraficoEixos":
            return GraficoEixosAdapter()
        elif tipo_exibicao == "GraficoPizza":
            return GraficoPizzaAdapter()
        else:
            raise HTTPException(
                status_code=400, detail="Não existe nenhum adaptador de exibição chamado " + tipo_exibicao)
