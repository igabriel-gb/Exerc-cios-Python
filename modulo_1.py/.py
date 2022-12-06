valor_passagem = 4.30
valor_corida = input('MODELO 1    qual o valor da corrida?  ')
if float(valor_corida) <= valor_passagem * 5:
    print("pague a corrida")
if float(valor_corida) > valor_passagem * 5:
    print("pegue o ônibus")


valor_passagem = 4.30
valor_corida = input('modelo 2    QUAL O VALOR DA CORRIDA?  ')
if float(valor_corida) <= valor_passagem * 5:
    print("pague a corrida")
else:
    if float(valor_corida) <= valor_passagem * 6:
        print("espere um pouco o valor da corrida pode abaixar")
    else:
        print("pague o ônibus")


        valor_passagem = 4.30
valor_corida = input('Modelo 3    Qual O Valor Da Corrida?  ')
if float(valor_corida) <= valor_passagem * 5:
    print("pague a corrida")
elif float(valor_corida) <= valor_passagem * 6:
    print("espere um pouco o valor da corrida pode abaixar")
else:
    print("pague o ônibus")