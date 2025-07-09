#script que lê data de nascimento e imprime a data formatada

nome = input('Qual o seu nome? ')
dia = int(input('Qual o dia de seu nascimento?'))
mes = int(input('Qual o mês de seu nascimento?'))
ano = int(input('Qual o ano de seu nascimento?'))

print(f'Olá {nome}! Seja bem vindo ao mundo Python!')
print(f'Você nasceu em {dia}/{mes}/{ano}, correto?')
