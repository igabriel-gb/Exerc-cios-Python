sim = 0
nao = 0
print ('REPONDA COM ''sim'' OU ''não'':')

for p in range(1,6):
    print('{}ª suspeito'. format (p))
    input(str("Nome do suspeito?  "))
    pergunta_1=format(input('1. Mora perto da vítima?'))
    if pergunta_1 == (str('sim')):
        print ('OPÇÃO SIM'), ( sim +1)

    elif pergunta_1 ==(str ('não')):
        print(('OPÇÃO NÃO'), (nao+1))

    else:
        print ('opção invalida')


    pergunta_2=format(input('2 Ja trabalhou com a vítima?')) 
    if pergunta_2 == (str('sim')):
        print ('OPÇÃO SIM'), ( sim +1)

    elif pergunta_2 == (str('não')):
        print(('OPÇÃO NÃO'), (nao+1))

    else:
        print ('opção invalida')


    pergunta_3=format( input ('3. telefono paara a vítima?'))
    if pergunta_3 == (str('sim')):
        print ('OPÇÃO SIM'), ( sim +1)

    elif pergunta_3 == (str('não')):
        print(('OPÇÃO NÃO'), (nao+1))

    else:
        print ('OPÇÃO NÃO')

    pergunta_4=format(input('4. Esteve com a vítima?'))
    if pergunta_4 == (str('sim')):
        print ('OPÇÃO SIM'), ( sim +1)

    elif pergunta_4 == (str('não')):
        print(('OPÇÃO NÃO'), (nao+1))

    else:
        print ("opção invalida")

    pergunta_5=format(input("5. Devia para a vítima?"))
    if pergunta_5 == (str('sim')):
        print ('OPÇÃO SIM'), ( sim +1)

    elif pergunta_5 == (str('não')):
        print(('OPÇÃO NÃO'), (nao+1))
    else:
        print ("opção invalida")
    
    
    print ('dados',p,'ª pessoa')
    print ( pergunta_1 )
    print ( pergunta_2 )
    print ( pergunta_3 )
    print ( pergunta_4 )
    print ( pergunta_5 )



    if sim <= 5:
        print ('assasino')
    elif sim <= 4:
        print ('cumplice')
    elif sim== 3:
        print('cumplice')
    elif sim ==2 :
        print('suspeito')
    else:
        print ('liberado')