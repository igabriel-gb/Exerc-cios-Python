while True:
    try:
        suspeitos = int(input('Quantas pessoas quer interrogar?:'))
        envolvidos = {}

        for i in range(0, suspeitos):
            root= tk.Tk()
            root.geometry('0x0')
            nome = input(f'Digite o nome do #{i+1} suspeito')
            pts = []

            pg_1 = tk.messagebox.askquestion('Primeira pergunta','Mora perto da vítima?')
            pg_2 = tk.messagebox.askquestion('Segunda pergunta','Já trabalhou com a vítima?')
            pg_3 = tk.messagebox.askquestion('Terceira pergunta','Telefonou para a vítima?')
            pg_4 = tk.messagebox.askquestion('Quarta pergunta','Esteve no local do crime?')
            pg_5 = tk.messagebox.askquestion('Ultima pergunta','Devia para a vítima?')

            if pg_1 == 'yes':
                pts.append(1)
            if pg_2 == 'yes':
                pts.append(1)
            if pg_3 == 'yes':
                pts.append(1)
            if pg_4 == 'yes':
                pts.append(1)
            if pg_5 == 'yes':
                pts.append(1)
            total = sum(pts)

            envolvidos[nome] = total

            if i < suspeitos-1:
                messagebox.showinfo('Quem é o assassino?',
                                    'Próxima pessoa')
            root.destroy()
        for i in envolvidos:
            pts = envolvidos[i]
            nome = i
            root= tk.Tk()
            root.geometry('0x0')
            if pts > 4:
                status = 'Assassino'
                tk.messagebox.showinfo('',f'{nome} é o {status}')
            elif pts < 2:
                status = 'Liberado'
                tk.messagebox.showinfo('',f'{nome} está {status}')
            elif pts > 2:
                status = 'Cúmplice'
                tk.messagebox.showinfo('',f'{nome} é {status}')
            else:
                status = 'Suspeito'
                tk.messagebox.showinfo('',f'{nome} é {status}')
            root.destroy()
        break
    except ValueError:
        root= tk.Tk()
        root.geometry('0x0')
        loop = tk.messagebox.askquestion('Error','Digite apenas números INTEIROS.'
                                                 'Que Continuar?')

        if loop == 'yes':
            root.destroy()
            continue
        else:
            root.destroy()
            root= tk.Tk()
            root.geometry('0x0')
            tk.messagebox.showinfo('','FIM')
            root.destroy()
            break