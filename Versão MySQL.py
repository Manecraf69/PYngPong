jogadoresNaFila = []

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='20122004',
    database='pyngpong_bd',
)
cursor = conexao.cursor()

# regras padrão
placarMax = 5
vaiA2 = "s"
tirarDe0 = 3

def historicoRepetido(jogInexistente):
    partidasGanhas = []
    partidasPerdidas = []

    jogInexistente = "Marcio"
    comando = f'SELECT id_partida FROM historico where jog_ganhador = ("{jogInexistente}")'
    cursor.execute(comando)
    busca1 = cursor.fetchall()

    for resultado in busca1:
        partidasGanhas.append(resultado)

    comando = f'SELECT id_partida FROM historico where jog_perdedor = ("{jogInexistente}")'
    cursor.execute(comando)
    busca2 = cursor.fetchall()

    for resultado in busca2:
        partidasPerdidas.append(resultado)

    mesmasPartidas = [elemento for elemento in partidasGanhas if elemento in partidasPerdidas]
    indexDaLista = 0
    for i in mesmasPartidas:
        partidaJogadorDuplicado = str(mesmasPartidas[indexDaLista])
        indexDaLista += 1
        partidaJogadorDuplicado = partidaJogadorDuplicado.replace(",)", "")
        partidaJogadorDuplicado = partidaJogadorDuplicado.replace("(", "")

        comando = f'DELETE FROM historico WHERE id_partida = ("{partidaJogadorDuplicado}")'
        cursor.execute(comando)
        conexao.commit()

def pontos(ganhador, perdedor):
    comando = f'SELECT nivel_habilidade FROM jogador WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    habilidade_ganhador = cursor.fetchall()

    comando = f'SELECT nivel_habilidade FROM jogador WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    habilidade_perdedor = cursor.fetchall()

    if habilidade_perdedor[0][0] == 5:
        pontos_ganhos = 10
    elif habilidade_perdedor[0][0] == 4:
        pontos_ganhos = 8
    elif habilidade_perdedor[0][0] == 3:
        pontos_ganhos = 6
    elif habilidade_perdedor[0][0] == 2:
        pontos_ganhos = 4
    elif habilidade_perdedor[0][0] == 1:
        pontos_ganhos = 2

    comando = f'SELECT pontos FROM jogador WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    busca = cursor.fetchall()

    variavelGanhador = busca[0][0]
    variavelGanhador += pontos_ganhos

    comando = f'UPDATE jogador SET pontos = ("{variavelGanhador}") WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    conexao.commit() 

    if habilidade_ganhador[0][0] == 5:
        pontos_perdidos = 0
    elif habilidade_ganhador[0][0] == 4:
        pontos_perdidos = 1
    elif habilidade_ganhador[0][0] == 3:
        pontos_perdidos = 2
    elif habilidade_ganhador[0][0] == 2:
        pontos_perdidos = 3
    elif habilidade_ganhador[0][0] == 1:
        pontos_perdidos = 4

    comando = f'SELECT pontos FROM jogador WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    busca = cursor.fetchall()

    variavelPerdedor = busca[0][0]
    variavelPerdedor -= pontos_perdidos

    comando = f'UPDATE jogador SET pontos = ("{variavelPerdedor}") WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    conexao.commit() 

def estatisticas(jogador):
    comando = f'SELECT jog_ganhador FROM historico WHERE jog_ganhador = ("{jogador}")'
    cursor.execute(comando)
    buscaVitorias = cursor.fetchall()

    comando = f'SELECT jog_perdedor FROM historico WHERE jog_perdedor = ("{jogador}")'
    cursor.execute(comando)
    buscaDerrotas = cursor.fetchall()

    n_partidas = len(buscaVitorias) + len(buscaDerrotas)
    n_vitorias = len(buscaVitorias)
    n_derrotas = len(buscaDerrotas)
    if n_derrotas == 0:
        n_derrotas = 1
    media_vitder = n_vitorias / n_derrotas

    # número total de partidas
    comando = f'UPDATE jogador SET partidas = ("{n_partidas}") WHERE nome = ("{jogador}")'
    cursor.execute(comando)
    conexao.commit() 

    # número de vitórias
    comando = f'UPDATE jogador SET vitorias = ("{n_vitorias}") WHERE nome = ("{jogador}")'
    cursor.execute(comando)
    conexao.commit() 

    # média de vitórias / derrotas
    comando = f'UPDATE jogador SET media_vitder = ("{media_vitder}") WHERE nome = ("{jogador}")'
    cursor.execute(comando)
    conexao.commit() 

    # nível habilidade

    if media_vitder <= 1:
        habilidade = 1
    elif media_vitder < 3:
        habilidade = 2
    elif media_vitder < 5:
        habilidade = 3
    elif media_vitder < 7:
        habilidade = 4
    elif media_vitder > 7 and n_partidas >= 40:
        habilidade = 5
    elif media_vitder > 7:
        habilidade = 4
    else:
        habilidade = 1

    comando = f'UPDATE jogador SET nivel_habilidade = ("{habilidade}") WHERE nome = ("{jogador}")'
    cursor.execute(comando)
    conexao.commit() 

def posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor):
    jogadoresNaFila.remove(ganhador)
    jogadoresNaFila.remove(perdedor)
    jogadoresNaFila.append(perdedor)
    jogadoresNaFila.append(ganhador)

    resultado = f"{pontosGanhador} x {pontosPerdedor}"

    comando = f'INSERT INTO historico (jog_ganhador, jog_perdedor, resultado) VALUES ("{ganhador}","{perdedor}","{resultado}")'
    cursor.execute(comando)
    conexao.commit() 

    pontos(ganhador, perdedor)

    jogador = ganhador
    estatisticas(jogador)

    jogador = perdedor
    estatisticas(jogador)

def jogadorInexistente():
    comando = f'SELECT nome FROM jogador WHERE nome = ("{jogInexistente}")'
    cursor.execute(comando)
    busca = cursor.fetchall()
    if adicionar == 1:
        if len(busca) != 0:
            pass
        else:
            comando = f'INSERT INTO jogador (nome) VALUES ("{jogInexistente}")'
            cursor.execute(comando)
            conexao.commit() 

    elif deletar == 1:
        if len(busca) != 0:
            comando = f'DELETE FROM jogador WHERE nome = ("{jogInexistente}")'
            cursor.execute(comando)
            conexao.commit()
            print("\033[1;31mO jogador foi removido.\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")  

    elif buscar == 1:
        if len(busca) != 0:
            comando = f'SELECT nome, partidas, vitorias, media_vitder, nivel_habilidade, pontos FROM jogador where nome = ("{jogInexistente}")'
            cursor.execute(comando)
            busca = cursor.fetchall()
            for resultado in busca:
                print("\033[1;92mNome: ", resultado[0])
                print("Número de partidas: ", resultado[1])
                print("Número de vitórias: ", resultado[2])
                print("Média de vitória / derrota: ", resultado[3])
                print("Nível de habildade: ", resultado[4])
                print("Pontos: ", resultado[5], "\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")

    elif buscar == 2:
        if len(busca) != 0:
            comando1 = f'SELECT jog_ganhador, jog_perdedor, resultado FROM historico WHERE jog_ganhador = ("{jogInexistente}")'
            cursor.execute(comando1)
            busca1 = cursor.fetchall()
            for resultado in busca1:
                print("\033[1;92m", resultado, "\033[0;0m")
                
            comando2 = f'SELECT jog_ganhador, jog_perdedor, resultado FROM historico WHERE jog_perdedor = ("{jogInexistente}")'
            cursor.execute(comando2)
            busca2 = cursor.fetchall()
            for resultado in busca2:
                print("\033[1;92m", resultado, "\033[0;0m")

            if len(busca1) == 0 and len(busca2) == 0:
                print("\033[1;33m O jogador ainda não participou de nenhuma partida!\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")

    elif atualizar == 1:
        if len(busca) != 0:
            nomeNovo = input("Digite o \033[1;33mnovo nome\033[0;0m para dar ao jogador (se o nome já existir serão \033[1;33munificados as estatísticas e histórico\033[0;0m): ")
            # atualiza histórico
            comando = f'UPDATE historico SET jog_ganhador = ("{nomeNovo}") WHERE jog_ganhador = ("{jogInexistente}")'
            cursor.execute(comando)
            conexao.commit()
            comando = f'UPDATE historico SET jog_perdedor = ("{nomeNovo}") WHERE jog_perdedor = ("{jogInexistente}")'
            cursor.execute(comando)
            conexao.commit()

            # corrige histórico caso haja a ocasiao de o jogador ter jogado "contra si mesmo"
            historicoRepetido(jogInexistente)
            
            # busca os pontos e soma no jogador correto
            comando = f'SELECT pontos, nome FROM jogador WHERE nome = ("{jogInexistente}")'
            cursor.execute(comando)
            busca1 = cursor.fetchall()
            
            pontosJogadorAntigo = busca1[0][0]

            comando = f'SELECT pontos, nome FROM jogador WHERE nome = ("{nomeNovo}")'
            cursor.execute(comando)
            busca2 = cursor.fetchall()

            # apenas a troca do nome
            if len(busca2) != 1:
                comando = f'UPDATE jogador SET nome = ("{nomeNovo}") WHERE nome = ("{jogInexistente}")'
                cursor.execute(comando)
                conexao.commit()

                if jogInexistente in jogadoresNaFila:
                    pos = jogadoresNaFila.index(jogInexistente)
                    jogadoresNaFila[pos] = nomeNovo
                
            # unificação de dois usuários em um só, juntando estatísticas
            if len(busca2) == 1:
                pontosJogadorNovo = busca2[0][0]
            
                novosPontos = pontosJogadorAntigo + pontosJogadorNovo

                comando = f'UPDATE jogador SET pontos = ("{novosPontos}") WHERE nome = ("{nomeNovo}")'
                cursor.execute(comando)
                conexao.commit()

                comando = f'DELETE FROM jogador WHERE nome = ("{jogInexistente}")'
                cursor.execute(comando)
                conexao.commit()

                if jogInexistente in jogadoresNaFila:
                    pos = jogadoresNaFila.index(jogInexistente)
                    jogadoresNaFila.remove(jogInexistente)
            
            # atualiza estatísticas
            jogador = jogInexistente
            estatisticas(jogador)

            print("\033[1;92mInformaçôes atualizadas!\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")
        
def pontuacaoPingPong():
            D = 0
            E = 0
            pontosDireita = 0
            pontosEsquerda = 0

            print("Digite \033[1;34mdd\033[0;0m para retirar um ponto da direita e \033[1;34mee\033[0;0m para retirar um ponto da esquerda.")

            while E < placarMax and D < placarMax:
                ponto = input("Digite quem fez o ponto (\033[1;34md\033[0;0m para direita \033[1;34me\033[0;0m para esquerda): ")
                if ponto == "d":
                    D += 1
                    pontosDireita += 1
                elif ponto == "e":
                    E += 1
                    pontosEsquerda += 1
                elif ponto == "dd":
                    D -= 1
                    pontosDireita -= 1
                elif ponto == "ee":
                    E -= 1
                    pontosEsquerda -= 1
                if D < 0:
                    D = 0
                    pontosDireita = 0
                if E < 0:
                    E = 0
                    pontosEsquerda = 0
                print(Direita,"(Direita)\033[1;34m",D, "x", E, "\033[0;0m", Esquerda, "(Esquerda)")

                if D == tirarDe0 and E == 0:
                    D = placarMax

                elif E == tirarDe0 and D == 0:
                    E = placarMax
    
                if vaiA2 == "s":
                    if E == placarMax - 1 and D == placarMax - 1:
                        print("Foi a 2")
                        E = 0
                        D = 0

                        while E < 2 and D < 2:
                            ponto = input("Digite quem fez o ponto: ")
                            if ponto == "d":
                                D += 1
                                pontosDireita += 1
                            elif ponto == "e":
                                E += 1
                                pontosEsquerda += 1
                            elif ponto == "dd":
                                D -= 1
                                pontosDireita -= 1
                            elif ponto == "ee":
                                E -= 1
                                pontosEsquerda -= 1
                            if D < 0:
                                D = 0
                                pontosDireita = 0
                            if E < 0:
                                E = 0
                                pontosEsquerda = 0
                            print(Direita,"(Direita)\033[1;34m",D, "x", E, "\033[0;0m", Esquerda, "(Esquerda)")
            
                            if E == 1 and D == 1:
                                E -= 1
                                D -= 1
                                print("Foi a 2 de novo")
                            if E == 2:
                                E = placarMax
                            elif D == 2:
                                D = placarMax

            if D == placarMax:
                print("\033[1;92mJogador da direita", Direita, "ganhou\033[0;0m")
                ganhador = Direita
                perdedor = Esquerda
                pontosGanhador = pontosDireita
                pontosPerdedor = pontosEsquerda
                posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

            elif E == placarMax:
                print("\033[1;92mJogador da esquerda", Esquerda, "ganhou\033[0;0m") 
                ganhador = Esquerda
                perdedor = Direita
                pontosGanhador = pontosEsquerda
                pontosPerdedor = pontosDireita
                posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
                print("Nome do jogador que vai entrar agora:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

opcao = 0
while opcao != "0404":
    adicionar = 0
    deletar = 0
    buscar = 0
    atualizar = 0
    opcao = input("\033[1;95mDigite o número com a respectiva opção que deseja trabalhar:\033[0;0m" 
                  "\n 1. Adicionar alguém à fila" 
                  "\n 2. Verificar o próximo da fila" 
                  "\n 3. Começar os pontos da partida" 
                  "\n 4. Inserir ganhador e perdedor" 
                  "\n 5. Tirar alguém da fila"
                  "\n 6. Ver as estatísticas de um jogador"
                  "\n 7. Excluir jogador"
                  "\n 8. Ver jogadores"
                  "\n 9. Modificar regras"
                  "\n 10. Ver histórico"
                  "\n 11. Editar jogador"
                  "\n 12. Encerrar o código" "\n")

    if opcao == "1":
        jogadorNovo = input("\033[1;34mDigite quem entrou na fila: \033[0;0m")
        if jogadorNovo in jogadoresNaFila:
            print("\033[1;33mO jogador já está na fila!\033[0;0m")
        else:
            jogadoresNaFila.insert(-1, jogadorNovo)
            print("\033[1;92m",jogadorNovo, "foi adicionado à fila.\033[0;0m")

        jogInexistente = jogadorNovo
        adicionar = 1
        jogadorInexistente()

    elif opcao == "2":
        if len(jogadoresNaFila) == 0:
            print("\033[1;33mSem jogadores na fila!\033[0;0m")
        elif len(jogadoresNaFila) >= 1:
            print("O próximo da fila é:\033[1;92m",jogadoresNaFila[0],"\033[0;0m")
            print("A ordem para jogar é:", jogadoresNaFila)

    elif opcao == "3":
        Direita = input("Quem é o jogador da direita? ")
        if Direita not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Direita)

        jogInexistente = Direita
        adicionar = 1
        jogadorInexistente()

        exc = 0
        while exc != 1:
            Esquerda = input("Quem é o jogador da Esquerda? ")

            if Direita == Esquerda:
                print("\033[1;33mUm jogador não pode jogar contra si mesmo!\033[0;0m")
            else:
                exc = 1
        
        if Esquerda not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Esquerda)

        jogInexistente = Esquerda
        adicionar = 1
        jogadorInexistente()

        print("\033[1;97mA partida começa\033[0;0m")
        pontuacaoPingPong()

    elif opcao == "4":
        ganhador = input("Digite o \033[1;34mnome\033[0;0m de quem ganhou: ")
        if ganhador not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, ganhador)

        exc = 0
        while exc != 1:
            pontosGanhador = input("Digite quantos \033[1;34mpontos\033[0;0m fez o ganhador: ")
            if not pontosGanhador.isdigit():
                print("\033[1;33mDigite um número!\033[0;0m")
            else:
                exc = 1
                jogInexistente = ganhador
                adicionar = 1
                jogadorInexistente()

        exc = 0
        while exc != 1:
            perdedor = input("Digite o \033[1;34mnome\033[0;0m de quem perdeu: ")
            if perdedor == ganhador:
                print("\033[1;33mUm jogador não pode jogar contra si mesmo!\033[0;0m")
            else:
                exc = 1

        if perdedor not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, perdedor)
                
        exc = 0
        while exc != 1:
            pontosPerdedor = input("Digite quantos \033[1;34mpontos\033[0;0m fez o perdedor: ")
            if not pontosPerdedor.isdigit():
                print("\033[1;33mDigite um número!\033[0;0m")
            else:
                exc = 1
                jogInexistente = perdedor
                adicionar = 1
                jogadorInexistente()

        posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
        print("\033[1;92mFila atualizada!\033[0;0m")
        print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

    elif opcao == "5":
        jogadorRemovido = input("Digite quem deseja \033[1;33mtirar\033[0;0m da fila: ")
        if jogadorRemovido not in jogadoresNaFila:
            print("\033[1;33mO jogador não está na fila!\033[0;0m")
        else:
            jogadoresNaFila.remove(jogadorRemovido)
            print("\033[1;31mO jogador foi removido da fila.\033[0;0m")

    elif opcao == "6":
        jogInexistente = input("Digite o nome do jogador que deseja ver as estatísticas: ")
        buscar = 1
        jogadorInexistente()

    elif opcao == "7":
        jogInexistente = input("Digite o nome do jogador que deseja \033[1;33mexcluir\033[0;0m: ")
        deletar = 1
        jogadorInexistente()
        if jogInexistente in jogadoresNaFila:
            jogadoresNaFila.remove(jogInexistente)

    elif opcao == "8":
        comando = f'SELECT nome FROM jogador'
        cursor.execute(comando)
        busca = cursor.fetchall()
        for resultado in busca:
            print("\033[1;92m", resultado[0], "\033[0;0m")
        if len(busca) == 0:
            print("\033[1;33mSem jogadores cadastrados!\033[0;0m")

    elif opcao == "9":
        exc = 0
        while exc != 1:
            placarMax = input("Selecione a quantidade de \033[1;34mpontos\033[0;0m necessários para \033[1;34mvencer\033[0;0m a partida: ")
            if not placarMax.isdigit():
                    print("\033[1;33mDigite um número!\033[0;0m")
            else:
                exc = 1
                placarMax = float(placarMax)

        exc = 0
        while exc != 1:
            vaiA2 = input("Digite \033[1;34ms\033[0;0m para ter sistema de vai a dois e \033[1;34mn\033[0;0m para não ter: ")
            if vaiA2 != "s" and vaiA2 != "n":
                print("Digite \033[1;34ms\033[0;0m ou \033[1;34mn\033[0;0m!")
            else:
                exc = 1

        exc = 0
        while exc != 1:
            tirarDe0 = input("Digite com quantos \033[1;34mpontos a zero\033[0;0m a partida acaba: ")
            if not tirarDe0.isdigit():
                    print("\033[1;33mDigite um número!\033[0;0m")
            else:
                exc = 1
                tirarDe0 = float(tirarDe0)

    elif opcao == "10":
        escolha = input("Digite \033[1;34m1\033[0;0m para histórico completo e \033[1;34m2\033[0;0m para o histórico de um jogador específico: ")
        if escolha == "1":
            comando = f'SELECT jog_ganhador, jog_perdedor, resultado FROM historico'
            cursor.execute(comando)
            busca = cursor.fetchall()
            for resultado in busca:
                print("\033[1;92m", resultado, "\033[0;0m")
            if len(busca) == 0:
                print("\033[1;33mSem jogadores cadastrados!\033[0;0m")
        elif escolha == "2":
            jogInexistente = input("Digite o \033[1;34mnome\033[0;0m do jogador que deseja ver todo o histórico: ")
            buscar = 2
            jogadorInexistente()
        else:
            print("\033[1;33mSelecione uma opção válida!\033[0;0m")

    elif opcao == "11":
        jogInexistente = input("Digite o \033[1;33mnome\033[0;0m do jogador que deseja \033[1;33malterar\033[0;0m: ")
        atualizar = 1
        jogadorInexistente()

    elif opcao == "12":
        print("\033[1;36mPrograma encerrado, agradecemos por usar nosso trabalho!\033[0;0m")

    else:
        print("\033[1;33mSelecione uma opção válida!\033[0;0m")

cursor.close()
conexao.close()