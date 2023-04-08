import os, math

os.system('cls')

class Country:
    def __init__(self, opcao: int,
                 pais: str,
                 alimentacao: int,
                 passeio: int,
                 hospedagem: int,
                 passagem: int):
        self.opcao = opcao
        self.pais = pais
        self.alimentacao = alimentacao
        self.passeio = passeio
        self.hospedagem = hospedagem
        self.passagem = passagem

paises = [
    Country(
    opcao = 1,
    pais= "Brasil",
        alimentacao= 165,
        passeio= 150,
        hospedagem= 350,
        passagem= 1700    
    ),
    Country(
        opcao= 2,
        pais= "Estados Unidos",
        alimentacao= 180,
        passeio= 120,
        hospedagem= 200,
        passagem= 2700
    ),
    Country(
        opcao= 3,
        pais= "Alemanha",
        alimentacao= 95,
        passeio= 30,
        hospedagem= 200,
        passagem= 4000
    ),
    Country(
        opcao= 4,
        pais= "Itália",
        alimentacao= 250,
        passeio= 130,
        hospedagem= 400,
        passagem= 3000
    ),
]
nome = input("Qual seu nome?: ")
orcamento = float(input("Qual o orçamento total disponível para a viagem?: "))

print('''
Escolha na lista um destino para a viagem:

[1] Brasil
[2] Estados Unidos
[3] Alemanha
[4] Itália
''')

escolhido = int(input("Digite a opção de destino: "))

print('''\n\n
Estimativa de gastos com base nos dias para viajar:

1 dia:

Alimentação (Café, Almoço, Janta/Café da tarde): R$ 130/200
Passeio (Museus, Praias, Parques de Diversão, Compras): R$ 100/200
Hospedagem (4 estrelas / 5 estrelas): R$ 100/600
Passagem (Ônibus/Avião - Ida e volta): R$ 400/3000

1 semana (7 dias)

Alimentação (Café, Almoço, Janta/Café da tarde): R$ 900/3000
Passeio (Museus, Praias, Parques de Diversão, Compras): R$ 700/2300
Hospedagem (4 estrelas / 5 estrelas): R$ 750/3500
Passagem (Ônibus/Avião - Ida e volta): R$ 500/3100

1 Mês (30 dias)

Alimentação (Café, Almoço, Janta/Café da tarde): R$ 3900/7000
Passeio (Museus, Praias, Parques de Diversão, Compras): R$ 1500/3000
Hospedagem (4 estrelas / 5 estrelas): R$ 3100/15000
Passagem (Ônibus/Avião): R$ 600/3300
\n\n''')

dias = int(input("Com base nas informações prescritas, quantos dias de viagem pretende fazer?: "))

for option in paises:
    if option.opcao == escolhido:
        gastos = (option.hospedagem + option.alimentacao + option.passeio + option.passagem)*dias
        sobra = math.ceil(float(orcamento - gastos))

        if (sobra > 0):
            print(f'{nome}, com base nos cálculos, no seu orçamento e nos dias de viagem\n')
            print(f'Você pode realizar a viagem para {option.pais} sem se preocupar com nada!\n')
            print(f'O total de gastos com base nos nossos cálculos é de R$ {gastos:.2f} e ainda te restará R$ {sobra:.2f}!\n')
            print("Está esperando pelo quê?! Vamos!\n")
        else:
            print(f'{nome}, com base nos cálculos, no seu orçamento e nos dias de viagem\n')
            print(f'Você não pode realizar a viagem para {option.pais} sugerimos que espere mais um pouco!\n')
            print('Junte mais um pouco na base do seu orçamento para a viagem, e retorne para cá!')
            print(f'Estaremos esperando por você, {nome}\n!')

