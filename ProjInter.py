
import os
os.system('cls')

                # REPERTÓRIO DE INFORMAÇÕES
curso = 'Análise e Desenvolvimento de Sistemas - UNICSUL São Miguel Paulista'
Inf_Proj = 'Este programa faz parte do Projeto Interdisciplinar das matérias de:\nProgramação de Computadores e Organização e Arquitetura de Computadores\nProfessores resposáveis: Nelson Missaglia e Marco Antônio Sanches'
Comp = 'Integrantes do grupo:\n Gustavo Gabriel\n Gustavo Teixeira\n Maria Eduarda Sena\n Barbara Silva\n Vanderley Oliveira\n Kayque Lima'
Version = 'Versão: 0.2'

                # MENU
 
while True:
   
    print('--------'*12)
    print('Seja bem-vindo(a) ao Conversor de Base Decimal'.center(80))
    print('Aqui converteremos um número de base Decimal em Binário, Hexadecimal ou Octadecimal')
    print('--------'*12)

                # OPÇÕES
    print("Por favor, escolha uma opção:")
    print("1 - Decimal >> Binário")
    print("2 - Decimal >> Hexadecimal")
    print("3 - Decimal >> Octadecimal")
    print("4 - Informações")
    print("5 - Sair")

    escolha = input("Digite sua escolha: ")

    print('--------'*12)

    match(escolha):
        
                # BINÁRIO    
        case('1'):
            print("Opção 1 selecionada.")
            decimal = int(input('Digite um número decimal: '))
            original = decimal
            bina = ""

            while decimal > 0:
                r = decimal % 2
                bina = str(r) + bina
                decimal = decimal//2

            print(f'O número {original} em Binário é: ({bina})²')
            print('--------'*12)
            input('Aperte "Enter" para voltar ao menu...')
            os.system('cls')

                # HEXADECIMAL
        case('2'):
            print("Opção 2 selecionada.")
            decimal = int(input('Digite um número decimal: '))
            original = decimal
            hexa = ''

            while decimal > 0:
                resto = decimal % 16
                if resto < 10:
                    hexa = str(resto) + hexa
                else:
                    hexa = chr(resto+55) + hexa
                decimal = decimal // 16
            print(f'O número {original} em Hexadecimal é: ({hexa})¹⁶')
            print('--------'*12)
            input('Aperte "Enter" para voltar ao menu...')
            os.system('cls')

                # OCTADECIMAL   
        case('3'):
            print("Opção 3 selecionada.")
            decimal = int(input('Digite um número decimal: '))
            original = decimal
            octa = ''

            while decimal >0:
                resto = decimal%8
                octa = str(resto) + octa
                decimal = decimal//8
            
            print(f'O número {original} em Octadecimal é: ({octa})⁸')
            print('--------'*12)
            input('Aperte "Enter" para voltar ao menu...')
            os.system('cls')
            
                # INFORMAÇÕES
    
        case('4'):
            os.system('cls')
            print('Informações disponíveis:'.center(40))
            print('1 - Informaçoes Maiores do Projeto')
            print('2 - Curso do Projeto')
            print('3 - Componentes do Projeto')
            print('4 - Versão atual')
            print('5 - Sair')
            escolha_inf = input('Qual informação deseja?: ')

            match(escolha_inf):
                case('1'):
                    print('--------'*12)
                    print(Inf_Proj)
                    print('--------'*12)
                case('2'):
                    print('--------'*12)
                    print(curso)
                    print('--------'*12)
                case('3'):
                    print('--------'*12)
                    print(Comp)
                    print('--------'*12)
                case('4'):
                    print('--------'*12)
                    print(Version)
                    print('--------'*12)
                case('5'):
                    print()
                case _:
                    print('Escolha inválida!')
                
            input('Aperte "Enter" para voltar ao menu de opções...')
            os.system("cls")
            
                # SAIR
        case('5'):
            print("Saindo do menu...")
            break
            
        case _:
            input('Escolha inválida. Aperte "Enter" para tentar novamente.')
            os.system('cls')
            
