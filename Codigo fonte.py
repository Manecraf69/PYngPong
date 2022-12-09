jogadoresNaFila = ["Marcio"]
# jogadoresNaFila = ["Marcio", "Paulo", "Ricardo", "Leo", "Kalinoski","Emili","Monteiro","Gomes"]
# jogadoresNaFila = []

def posJogo():
    jogadoresNaFila.remove(ganhador)
    jogadoresNaFila.remove(perdedor)
    jogadoresNaFila.append(perdedor)
    jogadoresNaFila.append(ganhador)

def pontuacaoPingPong():
            D = 0
            E = 0

            while E < 5 and D < 5:
                ponto = input("Digite quem fez o ponto: ")
                if ponto == "d":
                    D += 1
                elif ponto == "e":
                    E += 1
                print(Direita,"(Direita)",D, "x", E, Esquerda, "(Esquerda)")

                if D == 3 and E == 0:
                    D = 5

                elif E == 3 and D == 0:
                    E = 5
    
                if E == 4 and D == 4:
                    print("Foi a 2")
                    E = 0
                    D = 0

                    while E < 2 and D < 2:
                        ponto = input("Digite quem fez o ponto: ")
                        if ponto == "d":
                            D += 1
                        elif ponto == "e":
                            E += 1
                        print(Direita,"(Direita)",D, "x", E, Esquerda, "(Esquerda)")
        
                        if E == 1 and D == 1:
                            E -= 1
                            D -= 1
                            print("Foi a 2 de novo")
                        if E == 2:
                            E = 5
                        elif D == 2:
                            D = 5

            if D == 5:
                print("\033[1;92mJogador da direita", Direita, "ganhou\033[0;0m")
                ganhador = Direita
                perdedor = Esquerda
                jogadoresNaFila.remove(ganhador)
                jogadoresNaFila.remove(perdedor)
                jogadoresNaFila.append(perdedor)
                jogadoresNaFila.append(ganhador)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

            elif E == 5:
                print("\033[1;92mJogador da esquerda", Esquerda, "ganhou\033[0;0m") 
                ganhador = Esquerda
                perdedor = Direita
                jogadoresNaFila.remove(ganhador)
                jogadoresNaFila.remove(perdedor)
                jogadoresNaFila.append(perdedor)
                jogadoresNaFila.append(ganhador)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

opcao = 0
while opcao != "6":
    opcao = input("\033[1;95mDigite o número com a respectiva opção que deseja trabalhar:\033[0;0m" 
                  "\n 1. Adicionar alguém à fila" 
                  "\n 2. Verificar o próximo da fila" 
                  "\n 3. Começar os pontos da partida" 
                  "\n 4. Inserir ganhador e perdedor" 
                  "\n 5. Tirar alguém da fila"
                  "\n 6. Encerrar o código" "\n")

    if opcao == "1":
        jogadorNovo = input("\033[1;34mDigite quem entrou na fila: \033[0;0m")
        if jogadorNovo in jogadoresNaFila:
            print("\033[1;33mO jogador já está na fila!\033[0;0m")
        else:
            jogadoresNaFila.insert(-1, jogadorNovo)
            print("\033[1;92m",jogadorNovo, "foi adicionado à fila.\033[0;0m")

    elif opcao == "2":
        if len(jogadoresNaFila) == 0:
            print("\033[1;31mSem jogadores na fila!\033[0;0m")
        elif len(jogadoresNaFila) >= 1:
            print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")
            print("A ordem para jogar é:", jogadoresNaFila)

    elif opcao == "3":
        Direita = input("Quem é o jogador da direita? ")
        if Direita not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Direita)
        Esquerda = input("Quem é o jogador da Esquerda? ")
        if Esquerda not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Esquerda)

        print("\033[1;97mA partida começa\033[0;0m")
        pontuacaoPingPong()

    elif opcao == "4":
        ganhador = input("Digite o nome de quem ganhou: ")
        if ganhador not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, ganhador)
        perdedor = input("Digite o nome de quem perdeu: ")
        if perdedor not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, perdedor)

        posJogo()
        print("\033[1;92mFila atualizada!\033[0;0m")
        print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

    elif opcao == "5":
        jogadoresNaFila.remove(input("Digite o nome de quem saiu da fila: "))
        print("\033[1;31mO jogador foi removido da fila.\033[0;0m")

    elif opcao == "6":
        print("\033[1;36mPrograma encerrado, agradecemos por usar nosso trabalho!\033[0;0m")
        break

    else:
        print("\033[1;33mSelecione uma opção válida!\033[0;0m")