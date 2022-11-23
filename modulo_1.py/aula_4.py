idade = input('me conta aí quantos anos você tem?  ')
print(idade, type(idade))

idade = int(idade)
print(idade, type(idade))

print(float('123.12'))
print(str('123.12'))
print(bool(''))
print(bool('abcdef'))
print(bool('0'))
print(bool('-2'))
print(bool('10000'))
print(bool('+24'))
print(bool('50'))

meu_salario=input('digite o valor do seu salario mensal:  ')
meu_salario=float(meu_salario)

gasto_mensal=input('digite aqui seu gasto mensal:  ')
gasto_mensal=float(gasto_mensal)

meu_salario_total=meu_salario * 12
meu_gasto_total=gasto_mensal * 12

montante_economizado=meu_salario_total - meu_gasto_total
print('O montante economizado de um amo sera de:  ', montante_economizado)