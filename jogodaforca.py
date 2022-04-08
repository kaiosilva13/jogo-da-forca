from random import randint
from remove_accents import remove_non_ascii_normalized as remover_acentos

continuar = int()
opcao = int()
palpite = str()
pergunta = str()
while not continuar == '1':
    print('.' * 80)
    print('Bem vindo ao jogo da forca!\n(obs: quando for palpitar quaisquer letra utilize letras sem acentuação)')
    print('.' * 80)
    opcao = int()
    while opcao not in [1, 2, 3]:
        opcao = int(input('Escolha uma opção de tema :\n1 - Frutas\n2 - Países\n3 - Cores\nEsolha uma opção:'))
        if opcao not in [1, 2, 3]:
            print('Digite uma opção válida')
    if opcao == 1:
        palavra = ('maçã', 'melancia', 'limão', 'uva', 'pera', 'morango', 'banana', 'kiwi', 'jabuticaba',
                   'açai', 'manga', 'abacaxi', 'amora', 'abacate', 'caju', 'carambola', 'figo', 'framboesa',
                   'romã', 'tangerina', 'laranja', 'buriti', 'cacau', 'damasco', 'graviola', 'groselha',
                   'jambo', 'mamão', 'marmelo', 'pêssego', 'seriguela', 'tâmara', 'tamarindo', 'umbu')

    elif opcao == 2:
        palavra = ('brasil', 'argentina', 'angola', 'japão', 'alemanha', 'peru', 'china', 'equador', 'bélgica',
                   'canadá', 'frança' 'espanha', 'croácia', 'islândia', 'méxico', 'austrália', 'russia',
                   'turquia', 'dinamarca', 'cuba', 'honduras', 'jamaica', 'panamá', 'chile', 'bolívia',
                   'colômbia', 'uruguai', 'venezuela', 'ucrânia', 'itália', 'polônia', 'holanda', 'grécia'
                   , 'suécia', 'suiça', 'eslovênia', 'chipre', 'nigéria', 'gana', 'senegal', 'argélia',
                   'sudão', 'irã', 'israel', 'afeganistão', 'iraque', 'síria', 'líbano', 'zimbábue',
                   'áustria')
    elif opcao == 3:
        palavra = ('azul', 'rosa', 'vermelho', 'marrom', 'cinza', 'roxo', 'verde', 'amarelo', 'preto', 'branco',
                   'lilás', 'ciano', 'nude', 'laranja', 'bege', 'bronze', 'creme', 'dourado', 'esmeralda',
                   'magenta', 'prata', 'turquesa', 'violeta', 'marfim')
    elif opcao == 0:
        break
    num_sorteado = randint(0, len(palavra) - 1)
    palavra_sorteada = palavra[num_sorteado]
    palavra_sem_acento = remover_acentos(palavra_sorteada)
    chances = 6
    acerto_direto = ''
    letras_usuário = []
    acertos = 0
    print(f'A palavra sorteada tem {len(palavra_sorteada)} letras')
    print("""
                0
               /|\\
               / \\
               """)
    while not chances == 0:
        print('.' * 80)
        palpite = str(input('Qual letra você acha que tem na palavra?')).lower().strip()
        while palpite not in 'abcdefghijklmnopqrstuvwxyz':
            palpite = str(input('Qual letra você acha que tem na palavra?')).lower().strip()
            if palpite not in 'abcdefghijklmnopqrstuvwxyz':
                print('Digite letras sem acentuações!')
        if palpite in letras_usuário:
            print('A letra já foi digitada')
        if palpite in palavra_sem_acento:
            for c in palavra_sem_acento:
                if c == palpite:
                    print(f'{c}', end='')
                    acertos += 1
                elif c in letras_usuário:
                    print(f'{c}', end='')
                else:
                    print('_', end='')
            print()
            if acertos == len(palavra_sorteada):
                print(f'Genial! a palavra sorteada foi {palavra_sorteada.capitalize()} e você acertou')
                print('.' * 80)
                continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')
                while continuar not in '01':
                    continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')
                break
            else:
                print(f'Você ainda tem {chances} chances')
                letras_usuário.append(palpite)
        else:
            for c in palavra_sem_acento:
                if c == palpite:
                    print(f'{c}', end='')
                elif c in letras_usuário:
                    print(f'{c}', end='')
                else:
                    print('_', end='')
            print()
            print('Não há essa letra na palavra! Tente novamente')
            letras_usuário.append(palpite)
            chances -= 1
            if chances == 5:
                print("""
                 0
                /|\\
                / 
                """)
                print(f'Você ainda tem {chances} chances')
            elif chances == 4:
                print("""
                 0
                /|\\
                        
                       """)
                print(f'Você ainda tem {chances} chances')
            elif chances == 3:
                print("""
                  0
                 /|

                                 """)
                print(f'Você ainda tem {chances} chances')
            elif chances == 2:
                print("""
                0
                |

                                            """)
                print(f'Você ainda tem {chances} chances')
            elif chances == 1:
                print("""
                0
                           

                                                       """)
                print(f'Você ainda tem {chances} chances')

        if palpite in palavra_sem_acento:
            print()
            pergunta = str(input('Já sabe qual a palavra? [s/n] '))[0].lower().strip()
            while pergunta not in 'sn':
                pergunta = str(input('Já sabe qual a palavra? [s/n] '))[0].lower().strip()
                if pergunta not in 'sn':
                    print('Responda com s para Sim e n para Não')
            if not pergunta == 's':
                continue
            elif pergunta == 's':
                acerto_direto = str(input('Qual seu palpite? ')).lower().strip()
                if acerto_direto == palavra_sorteada or acerto_direto == palavra_sem_acento:
                    print(f'Genial! a palavra sorteada foi {palavra_sorteada.capitalize()} e você acertou')
                    print('.' * 80)
                    continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')
                    if continuar == '0':
                        break
                    while continuar not in '01':
                        continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')
                    break
                else:
                    print('Errouuu! Continue a  jogar')
    if chances == 0:
        print(f'Perdeu! A palavra sorteada era {palavra_sorteada.capitalize()}')
        print('.' * 80)
        continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')
        while continuar not in '01':
            continuar = input('Deseja continuar jogando? Digite 0 para Sim e 1 para Não: ')