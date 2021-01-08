class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    fernando_filho = Pessoa(nome='Fernando Filho')
    fernando = Pessoa(fernando_filho, nome='Fernando')
    print(Pessoa.cumprimentar(fernando))
    print(fernando.cumprimentar())
    for filho in fernando.filhos:
        print(filho.nome)
