for p in range(1,6):
    print('{}ª ENTREVISTADO'. format (p))

    sim = 0
    nao = 0
    
    input (str('nome: '))
    print ('responda com SIM ou NÃO')
    while True:
        pergunta_1 = str(input(f'1. Mora perto da vítima?\n'))[0].lower()
        if pergunta_1 in "sn":
            break
        else:
            print("opção invalida, tente novamente")
    if pergunta_1 == 's':
        sim += 1
        print('SIM')
    elif pergunta_1 == 'n':
        nao += 1
        print('NÃO')


    while True:
        pergunta_2 = str(input(f'2. Já trabalhou com a vítima?\n'))[0].lower()
        if pergunta_2 in "sn":
            break
        else:
            print("opção invalida, tente novamente")
    if pergunta_2 == 's':
        sim += 1
        print('SIM')
    elif pergunta_2 == 'n':
        nao += 1
        print('NÃO')

    while True:
        pergunta_3 = str(input(f'3. Telefonou para a vítima?\n'))[0].lower()
        if pergunta_3 in "sn":
            break
        else:
            print("opção invalida, tente novamente")
    if pergunta_3 == 's':
        sim += 1
        print('SIM')
    elif pergunta_3 == 'n':
        nao += 1
        print('NÃO')

    while True:
        pergunta_4 = str(input(f'4. Esteve com a vítima?\n'))[0].lower()
        if pergunta_4 in "sn":
            break
        else:
            print("opção invalida, tente novamente")
    if pergunta_4 == 's':
        sim += 1
        print('SIM')
    elif pergunta_4 == 'n':
        nao += 1
        print('NÃO')


    while True:
        pergunta_5 = str(input(f'5. Devia para a vítima?\n'))[0].lower()
        if pergunta_5 in "sn":
            break
        else:
            print("opção invalida, tente novamente")
    if pergunta_5 == 's':
        sim += 1
        print('SIM')
    elif pergunta_5 == 'n':
        nao += 1
        print('NÃO')

    print ('Dados do {}ª entrevistado'. format (p))


    print(f"o entrevistado deu {sim} respostas SIM")
    print(f"o entrevistado deu {nao} respostas NÃO")

    if sim == 5: print('De acordo com os dados coletados o entrevistado e considerado ASSASSINO')
    elif sim == 4 : print('Com base nas informações o entrevistado será considerado CÚMPLICE do crime')
    elif sim == 3: print('Com base nas informações o entrevistado será considerado CÚMPLICE do crime')
    elif sim == 2: print('O entrevistado será considerado SUSPEITO até o fim das investigações')
    else: 
        print('Não tivemos evidencias do entrevistado com a vitima, no intato o mesmo será LIBERADO')
 