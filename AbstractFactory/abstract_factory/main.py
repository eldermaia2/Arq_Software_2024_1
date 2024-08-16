from concretefactories import ReservaFactoryRegiaoA, ReservaFactoryRegiaoB
from client import SistemaReservas

def main():
    print("Reserva na Região A:")
    factory_regiao_a = ReservaFactoryRegiaoA()
    sistema_regiao_a = SistemaReservas(factory_regiao_a)
    sistema_regiao_a.realizarReserva()
    
    print("\nReserva na Região B:")
    factory_regiao_b = ReservaFactoryRegiaoB()
    sistema_regiao_b = SistemaReservas(factory_regiao_b)
    sistema_regiao_b.realizarReserva()

if __name__ == "__main__":
    main()
