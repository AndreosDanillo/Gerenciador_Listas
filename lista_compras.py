import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i] inserir [a] apagar [v] visualizar [f] finalizar: ')


    if opcao == 'i':
        os.system('cls')
        valor = input('Adicione: ')
        lista.append(valor)
        os.system('cls')
        print('LISTA ATUALIZADA!')
        for i, valor in enumerate(lista, start=1):
            print(f'{i} = {valor}')


    elif opcao == 'a':
            os.system('cls')
            for i, valor in enumerate(lista, start=1):
                print(f'{i} = {valor}')
            apagar = input('O que deseja apagar: ')
            if apagar in lista:
                lista.remove(apagar)
                os.system('cls')
                print('LISTA ATUALIZADA!')
                for i, valor in enumerate(lista, start=1):
                    print(f'{i} = {valor}')
            else:
                os.system('cls')
                print('Não encontramos esse valor na lista!')
                for i, valor in enumerate(lista, start=1):
                    print(f'{i} = {valor}')


    elif opcao == 'v':
         os.system('cls')
         print('LISTA PARCIAL!')
         for i,valor in enumerate(lista, start=1):
            print(f'{i} = {valor}')
         

    elif opcao == 'f':
        os.system('cls')
        if len(lista) == 0:
            print('A lista está vázia')
            sair = input('Deseja realmente sair (s/n): ')
            if sair == 's':
                print('Obrigado por usar!')
                break
        else:
            print('LISTA FINALIZADA!')
            for i, valor in enumerate(lista, start=1):
                    print(f'{i} = {valor}')
            break

            
    else:
         os.system('cls')
         print('Digite algo válido!')