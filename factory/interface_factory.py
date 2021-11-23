from adapters.grafico_eixos_adapter import GraficoEixosAdapter
from adapters.grafico_pizza_adapter import GraficoPizzaAdapter
from adapters.i_adapter import IAdapter
from fastapi import HTTPException


class InterfaceFactory:

    def gerar_interface(self, tipo_interface: str) -> IAdapter:
        if tipo_interface == "GraficoEixos":
            return GraficoEixosAdapter()
        elif tipo_interface == "GraficoPizza":
            return GraficoPizzaAdapter()
        else:
            raise HTTPException(
                status_code=400, detail="Não existe nenhum adaptador de interface chamado " + tipo_interface)
