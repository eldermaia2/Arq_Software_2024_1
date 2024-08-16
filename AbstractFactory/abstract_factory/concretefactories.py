from abstractfactories import ReservaFactory
from products import (QuartoLuxoRegiaoA, QuartoSimplesRegiaoA, 
                      ProcessoReservaRegiaoA, PagamentoRegiaoA, 
                      QuartoLuxoRegiaoB, QuartoSimplesRegiaoB, 
                      ProcessoReservaRegiaoB, PagamentoRegiaoB)

# Fábrica para a Região A
class ReservaFactoryRegiaoA(ReservaFactory):
    def criarQuarto(self):
        return QuartoLuxoRegiaoA()  # ou QuartoSimplesRegiaoA()

    def criarProcessoReserva(self):
        return ProcessoReservaRegiaoA()

    def criarPagamento(self):
        return PagamentoRegiaoA()

# Fábrica para a Região B
class ReservaFactoryRegiaoB(ReservaFactory):
    def criarQuarto(self):
        return QuartoLuxoRegiaoB()  # ou QuartoSimplesRegiaoB()

    def criarProcessoReserva(self):
        return ProcessoReservaRegiaoB()

    def criarPagamento(self):
        return PagamentoRegiaoB()
