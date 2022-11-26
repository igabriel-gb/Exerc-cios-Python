# EXERCICO 1 DO CURSO
# faça um programa que peça um valor monetário e o diminua-o em 15%


valor = input('digite o valor monetario que ser adiminuido em 15%: ')
valor = float(valor)


padrão = 15
padrão = float(padrão)

a = padrão * valor

cem = 100
cem = float(cem)

b = a / cem

somatória = valor - b
print('o valor e de:', somatória)


#meu exercicio para traticar
#quero comprar um carro no valor de 22 mil reais

salario=input('Seu salario mensal aqui: ')
salario=float(salario)

gastos=input('Quanto voce gasta todos os meses? ')
gastos=float(gastos)

outros_gastos_padrões=20
c = 22000
hoje_tenho = 7000
bruto = salario - gastos

a = outros_gastos_padrões * bruto
b = a / 100
somatoria = bruto - b

faltam = c - hoje_tenho

valor= faltam / somatoria
print('exatos ', valor)




#  EXERCICO 2 DO CURSO
#  FAÇA UM PROGRAMA QUE LEIA A VALIDADE DAS INFORMAÇÕES:
# IDADE, SALARIO, SEXO M, F OU OUTROS


Idade = int(input('Qual a Idade: '))
Salatio = int(input('Qual o seu salario mensal: ')) 
Sexo = str( input ('Qual sexo melhor o defini [M | F | OUTROS]: '))

Idade = float, print(Idade, 'anos')
Salatio = float, print("Meu salario mensal e de R$", Salatio,)
Sexo= float, print("Sou do sexo", Sexo,)


#meu exercicio

print ('DIGITE A SEGUINTES INFORMAÇÕES:')
for p in range(1,4):
    print('{}ª PESSOA'. format (p))
    Nome = str(input('Informe o nome: '))
    Idade = int(input('Qual a Idade: ')) 
    Sexo = str( input ('Qual sexo melhor o defini [M | F | OUTROS]: '))
    Natural = str(input('Natural de qual cidade: '))
    estado = str(input("Naturalde qual estado: "))
    Telefone= int(input("Informe um numero para contato: "))
    
    
    print("dados",p,'ª pessoa')
    Nome = float,print ( Nome )
    Iade = float,print ( Idade )
    Sexo = float,print ( Sexo )
    Natural = float,print (Natural,'-', estado)
    Telefone = float,print (Telefone)




#faça um programa para a polícia solucionar um assassinato, para descobrir o assassino a polícia faz um questionario de 5 perguntas, para 4 suspeitos.


print ('REPONDA COM ''SIM'' OU ''NAO'':')
for p in range(1,5):
    print('{}ª PESSOA'. format (p))
    pergunta_1=format(input('1. Mora perto da vítima?'))
    pergunta_2=format(input('2 Ja trabalhou com a vítima?')) 
    pergunta_3=format( input ('3. telefono paara a vítima?'))
    pergunta_4=format(input('4. Esteve com a vítima?'))
    pergunta_5=format(input("5. Devia para a vítima?"))
    
    print ('dados',p,'ª pessoa')
    print ( pergunta_1 )
    print ( pergunta_2 )
    print ( pergunta_3 )
    print ( pergunta_4 )
    print ( pergunta_5 )