contador = 0
while contador < 10:
    contador = contador  + 1
    if contador == 1:
        print(contador, "item conferido")
    else:
        print( contador, "intens conferidos")
print("chegamos ao fim da repetição deste bloco")




contador = 0
while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "item conferido")
        else:
            print( contador, "intens conferidos")
    else:
        break
print("chegamos ao fim da repetição do bloco 2")




texto = input('digite sua senha')
while texto != 'gabriel':
    texto = input('Senha incorreta. Tente novamente')

print('acesso permitido')




contador = 0
while contador < 10:
    contador = contador  + 1
    if contador == 1:
        continue
        print(contador, "item conferido")
    else:
        print( contador, "intens conferidos")
print("chegamos ao fim da repetição deste bloco")