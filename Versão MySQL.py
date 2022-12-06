jogadoresNaFila = []

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='20122004',
    database='pyngpong_bd',
)
cursor = conexao.cursor()

def posJogo(ganhador, perdedor):
    jogadoresNaFila.remove(ganhador)
    jogadoresNaFila.remove(perdedor)
    jogadoresNaFila.append(perdedor)
    jogadoresNaFila.append(ganhador)

def jogadorInexistente():
    seleciona = f'SELECT nome FROM jogador WHERE nome = ("{jogInexistente}")'
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    if len(resultado) != 0:
        pass
    if len(resultado) != 0 and deletar == 1:
        comando = f'DELETE FROM jogador WHERE nome = ("{jogInexistente}")'
        cursor.execute(comando)
        conexao.commit()
        print("\033[1;31mO jogador foi removido.\033[0;0m")
    else:
        if adicionar == 1:
            comando = f'INSERT INTO jogador (nome) VALUES ("{jogInexistente}")'
            cursor.execute(comando)
            conexao.commit() 
        elif deletar == 1:
            print("\033[1;33mO jogador não existe!\033[0;0m")       
            
def pontuacaoPingPong():
            D = 0
            E = 0

            while E < 5 and D < 5:
                ponto = input("Digite quem fez o ponto (\033[1;33md\033[0;0m para direita \033[1;33me\033[0;0m para esquerda): ")
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
                posJogo(ganhador, perdedor)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

            elif E == 5:
                print("\033[1;92mJogador da esquerda", Esquerda, "ganhou\033[0;0m") 
                ganhador = Esquerda
                perdedor = Direita
                posJogo(ganhador, perdedor)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

opcao = 0
while opcao != "batata":
    adicionar = 0
    deletar = 0
    opcao = int(input("\033[1;95mDigite o número com a respectiva opção que deseja trabalhar:\033[0;0m" 
                  "\n 1. Adicionar alguém à fila" 
                  "\n 2. Verificar o próximo da fila" 
                  "\n 3. Começar os pontos da partida" 
                  "\n 4. Inserir ganhador e perdedor" 
                  "\n 5. Tirar alguém da fila"
                  "\n 6. Ver as estatísticas de um jogador"
                  "\n 7. Excluir jogador"
                  "\n 8. Ver jogadores"
                  "\n 9. Modificar regras"
                  "\n 10. Encerrar o código" "\n"))

    if opcao == 1:
        jogadorNovo = input("\033[1;34mDigite quem entrou na fila: \033[0;0m")
        if jogadorNovo in jogadoresNaFila:
            print("\033[1;33mO jogador já está na fila!\033[0;0m")
        else:
            jogadoresNaFila.insert(-1, jogadorNovo)
            print("\033[1;92m",jogadorNovo, "foi adicionado à fila.\033[0;0m")

        jogInexistente = jogadorNovo
        adicionar = 1
        jogadorInexistente()

    if opcao == 2:
        if len(jogadoresNaFila) == 0:
            print("\033[1;31mSem jogadores na fila!\033[0;0m")
        elif len(jogadoresNaFila) >= 1:
            print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")
            print("A ordem para jogar é:", jogadoresNaFila)

    if opcao == 3:
        Direita = input("Quem é o jogador da direita? ")
        if Direita not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Direita)

        jogInexistente = Direita
        adicionar = 1
        jogadorInexistente()

        Esquerda = input("Quem é o jogador da Esquerda? ")
        if Esquerda not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Esquerda)

        jogInexistente = Esquerda
        adicionar = 1
        jogadorInexistente()

        print("\033[1;97mA partida começa\033[0;0m")
        pontuacaoPingPong()

    if opcao == 4:
        ganhador = input("Digite o nome de quem ganhou: ")
        if ganhador not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, ganhador)
        
        jogInexistente = ganhador
        adicionar = 1
        jogadorInexistente()

        perdedor = input("Digite o nome de quem perdeu: ")
        if perdedor not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, perdedor)

        jogInexistente = perdedor
        adicionar = 1
        jogadorInexistente()

        posJogo(ganhador, perdedor)
        print("\033[1;92mFila atualizada!\033[0;0m")
        print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

    if opcao == 5:
        jogadorRemovido = input("\033[1;34mDigite quem deseja tirar da fila: \033[0;0m")
        if jogadorRemovido not in jogadoresNaFila:
            print("\033[1;33mO jogador não está na fila!\033[0;0m")
        else:
            jogadoresNaFila.remove(jogadorRemovido)
            print("\033[1;31mO jogador foi removido da fila.\033[0;0m")

    if opcao == 6:
        pass

    if opcao == 7:
        jogInexistente = input("Digite o nome do jogador que deseja excluir: ")
        deletar = 1
        jogadorInexistente()

    if opcao == 8:
        seleciona = f'SELECT nome FROM jogador'
        cursor.execute(seleciona)
        resultado = cursor.fetchall()
        print(resultado)

    if opcao == 9:
        pass

    if opcao == 10:
        print("\033[1;36mPrograma encerrado, agradecemos por usar nosso trabalho!\033[0;0m")

cursor.close()
conexao.close()