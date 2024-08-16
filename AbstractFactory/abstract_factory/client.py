class SistemaReservas:
    def __init__(self, factory):
        self.factory = factory

    def realizarReserva(self):
        quarto = self.factory.criarQuarto()
        processo_reserva = self.factory.criarProcessoReserva()
        pagamento = self.factory.criarPagamento()

        quarto.definirDescricao()
        processo_reserva.reservar()
        pagamento.efetuarPagamento()
