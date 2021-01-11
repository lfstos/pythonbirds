class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    ana = Pessoa(nome='Ana')
    fernando = Pessoa(ana, nome='Fernando')
    print(Pessoa.cumprimentar(fernando))
    print(fernando.cumprimentar())
    for filho in fernando.filhos:
        print(filho.nome)

    print(f'antes... {fernando.__dict__}')
    fernando.sobrenome = 'Santos'
    print(fernando.sobrenome)

    print(f'depois .... {fernando.__dict__}')

    del fernando.filhos
    for filho in fernando.filhos:
        print(filho.nome)
