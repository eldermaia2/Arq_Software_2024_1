from abstractfactories import Quarto, ProcessoReserva, Pagamento

# Produtos para a Região A
class QuartoLuxoRegiaoA(Quarto):
    def definirDescricao(self):
        print("Quarto de Luxo da Região A")

class QuartoSimplesRegiaoA(Quarto):
    def definirDescricao(self):
        print("Quarto Simples da Região A")

class ProcessoReservaRegiaoA(ProcessoReserva):
    def reservar(self):
        print("Reserva feita com sucesso na Região A")

class PagamentoRegiaoA(Pagamento):
    def efetuarPagamento(self):
        print("Pagamento realizado com cartão na Região A")

# Produtos para a Região B
class QuartoLuxoRegiaoB(Quarto):
    def definirDescricao(self):
        print("Quarto de Luxo da Região B")

class QuartoSimplesRegiaoB(Quarto):
    def definirDescricao(self):
        print("Quarto Simples da Região B")

class ProcessoReservaRegiaoB(ProcessoReserva):
    def reservar(self):
        print("Reserva feita com sucesso na Região B")

class PagamentoRegiaoB(Pagamento):
    def efetuarPagamento(self):
        print("Pagamento realizado com dinheiro na Região B")
