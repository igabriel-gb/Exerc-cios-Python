while True:
    try:
        from datetime import date
        data=date.today().year


        pg1 = float(
            input('Informe seu ano de nascimento: '))
        idade = data - pg1
        while pg1 < 0:
            print(f'Erro, ano de nascimento invalido. Informe seu ano de nacsimento:  ')
            idade = data - pg1
        print(idade,'anos')

    except ValueError:
            loop = input("digite apenas numeros que continuar? sim ou não  ")[0]
            if loop == 's':
                continue
            else:
                print("Fim")
                break    