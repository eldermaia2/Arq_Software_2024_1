from abc import ABC, abstractmethod

# Interfaces para os produtos
class Quarto(ABC):
    @abstractmethod
    def definirDescricao(self):
        pass

class ProcessoReserva(ABC):
    @abstractmethod
    def reservar(self):
        pass

class Pagamento(ABC):
    @abstractmethod
    def efetuarPagamento(self):
        pass

# Interface para a fábrica
class ReservaFactory(ABC):
    @abstractmethod
    def criarQuarto(self):
        pass
     
    @abstractmethod
    def criarProcessoReserva(self):
        pass
     
    @abstractmethod
    def criarPagamento(self):
        pass
