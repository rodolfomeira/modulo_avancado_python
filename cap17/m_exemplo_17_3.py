class Veiculo:
    def __init__(self, placa, modelo, ano, km):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def exibe(self):
        print(f'Veículo placa {self.placa}')
        print(f'  {self.modelo}, ano: {self.ano} - km: {self.km}')
