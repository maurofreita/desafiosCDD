pontuacao1 = 0
pontuacao2 = 0

while pontuacao1 != 3 and pontuacao2 != 3:
    print("Digite:"
          "\n[0] para Pedra"
          "\n[1] para Papel"
          "\n[2] para Tesoura")
    jogador1 = int(input("Jogador 1 insira sua escolha: "))
    jogador2 = int(input("Jogador 2 insira sua escolha: "))
    if jogador1 == 0:
        if jogador2 == 0:
            print("\nEmpate.\n")
        elif jogador2 == 1:
            print("\nJogador 2 ganhou a rodada.\n")
            pontuacao2 += 1
        elif jogador2 == 2:
            print("\nJogador 1 ganhou a rodada.\n")
            pontuacao1 += 1
        else:
            print("\nJogada inválida.\n")

    if jogador1 == 1:
        if jogador2 == 0:
            print("\nJogador 1 ganhou a rodada.\n")
            pontuacao1 += 1
        elif jogador2 == 1:
            print("\nEmpate.\n")
        elif jogador2 == 2:
            print("\nJogador 2 ganhou a rodada.\n")
            pontuacao2 += 1
        else:
            print("\nJogada inválida.\n")

    if jogador1 == 2:
        if jogador2 == 0:
            print("\nJogador 2 ganhou a rodada.\n")
            pontuacao2 += 1
        elif jogador2 == 1:
            print("\nJogador 1 ganhou a rodada.\n")
            pontuacao1 += 1
        elif jogador2 == 2:
            print("\nEmpate.\n")
        else:
            print("\nJogada inválida.\n")

    if jogador1 != 0 and jogador1 != 1 and jogador1 != 2:
        print("\nJogada inválida.\n")

if pontuacao1 == 3:
    print("Jogador 1 venceu a partida.")
else:
    print("Jogador 2 venceu a partida.")