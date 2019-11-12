maquina = 'O'
humano = 'X'
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def inserirPosicao(linha, coluna, jogador):
    if verificaValidade(linha, coluna):
        matriz[linha][coluna] = jogador
        return True

    return False


def verificaValidade(linha, coluna):
    if [linha, coluna] in verificaEspacoVazio(matriz):
        return True

    return False


def verificaEspacoVazio(matriz):
    celulasVazias = []
    for linha, linhaDaMatriz in enumerate(matriz):
        for coluna, celula in enumerate(linhaDaMatriz):
            if celula == ' ':
                celulasVazias.append([linha, coluna])

    return celulasVazias


def tabuleiro(matriz):
    print('         |   |')
    print('       {} | {} | {}'.format(matriz[0][0], matriz[0][1], matriz[0][2]))
    print('         |   |')
    print('      -----------')
    print('         |   |')
    print('       {} | {} | {}'.format(matriz[1][0], matriz[1][1], matriz[1][2]))
    print('         |   |')
    print('      -----------')
    print('         |   |')
    print('       {} | {} | {}'.format(matriz[2][0], matriz[2][1], matriz[2][2]))
    print('         |   |')


def turnoHumano():
    profundidade = len(verificaEspacoVazio(matriz))
    if profundidade == 0 or gameOver(matriz):
        return
    move = 0
    movimentos = {1: [0, 0], 2: [0, 1], 3: [0, 2],4: [1, 0], 5: [1, 1], 6: [1, 2],7: [2, 0], 8: [2, 1], 9: [2, 2],}
    print('\n=-=-=-=Sua vez=-=-=-=\n')
    while move not in movimentos:
        try:
            move = int(input('Escolha um número de 1 a 9: '))
            coord = movimentos[move]
            podeMover = inserirPosicao(coord[0], coord[1], humano)
            if not podeMover:
                print('Posiçao ocupada!')
                move = 0
        except (ValueError, KeyError):
            print('Digite um número entre 1 e 9!')


def turnoMaquina():
    profundidade = len(verificaEspacoVazio(matriz))
    if profundidade == 0 or gameOver(matriz):
        return
    move = 0
    movimentos = {1: [0, 0], 2: [0, 1], 3: [0, 2],4: [1, 0], 5: [1, 1], 6: [1, 2],7: [2, 0], 8: [2, 1], 9: [2, 2],}
    print('\n=-=-=-=Vez do PC=-=-=-=\n')
    while move not in movimentos:
        try:
            move = int(input('Escolha um número de 1 a 9: '))
            coord = movimentos[move]
            podeMover = inserirPosicao(coord[0], coord[1], maquina)
            if not podeMover:
                print('Posiçao ocupada!')
                move = 0
        except (ValueError, KeyError):
            print('Digite um número entre 1 e 9!')


def vencedor(matriz, jogador):
    return ((matriz[0][0] == jogador and matriz[0][1] == jogador and matriz[0][2] == jogador) or
            (matriz[1][0] == jogador and matriz[1][1] == jogador and matriz[1][2] == jogador) or
            (matriz[2][0] == jogador and matriz[2][1] == jogador and matriz[2][2] == jogador) or
            (matriz[0][0] == jogador and matriz[1][0] == jogador and matriz[2][0] == jogador) or
            (matriz[0][1] == jogador and matriz[1][1] == jogador and matriz[2][1] == jogador) or
            (matriz[0][2] == jogador and matriz[1][2] == jogador and matriz[2][2] == jogador) or
            (matriz[0][0] == jogador and matriz[1][1] == jogador and matriz[2][2] == jogador) or
            (matriz[2][0] == jogador and matriz[1][1] == jogador and matriz[0][2] == jogador))


def gameOver(matriz):
    return vencedor(matriz, humano) or vencedor(matriz, maquina)


def main():
    while len(verificaEspacoVazio(matriz)) > 0 and not gameOver(matriz):
        tabuleiro(matriz)
        turnoHumano()
        turnoMaquina()
    if vencedor(matriz, humano):
        print('\n=-=-=Voce ganhou=-=-=')
        tabuleiro(matriz)
    elif vencedor(matriz, maquina):
        print('\n=-=-=Voce perdeu=-=-=')
        tabuleiro(matriz)
    else:
        print('\n=-=-=-=Deu velha=-=-=-=')
        tabuleiro(matriz)

main()