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

def rankingDeJogadores():
    pontosDosJogadores = []

    comando = f'SELECT pontos FROM jogador'
    cursor.execute(comando)
    pontos = cursor.fetchall()

    for i in pontos:
        pontosDosJogadores.append(i[0])

    pontosDosJogadores.sort(reverse = True)

    indexDaLista = 0
    if len(pontosDosJogadores) > 0:
        print("\033[1;94mNome do jogador, pontos e número de partidas: ")
        for i in pontosDosJogadores:
            comando = f'SELECT nome, pontos, partidas FROM jogador WHERE pontos = ("{pontosDosJogadores[indexDaLista]}")'
            cursor.execute(comando)
            nomeJogadorRankeado = cursor.fetchall()
            for i in nomeJogadorRankeado:
                print(i)
            if indexDaLista == 3:
                break
            indexDaLista += 1
    else:
        print("\033[0;33mNão há jogadores cadastrados!\033[0;0m")

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

    print("\033[1;97mO jogador\033[0;34m", ganhador, "\033[0;32mganhou", pontos_ganhos, "\033[1;97mpontos e o jogador\033[0;34m", perdedor, "\033[0;31mperdeu", pontos_perdidos, "\033[1;97mpontos.\033[0;0m")

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
    elif media_vitder < 3 and n_partidas >= 5:
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

    comando = f'SELECT nivel_habilidade FROM jogador WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    habilidadeGanhador = cursor.fetchall()

    comando = f'SELECT nivel_habilidade FROM jogador WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    habilidadePerdedor = cursor.fetchall()

    comando = f'INSERT INTO historico (jog_ganhador, habilidade_ganhador, jog_perdedor, habilidade_perdedor, resultado) VALUES ("{ganhador}","{habilidadeGanhador[0][0]}","{perdedor}","{habilidadePerdedor[0][0]}","{resultado}")'
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
            print("\033[1;31mO jogador foi excluído.\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")  

    elif buscar == 1:
        if len(busca) != 0:
            comando = f'SELECT nome, partidas, vitorias, media_vitder, nivel_habilidade, pontos FROM jogador where nome = ("{jogInexistente}")'
            cursor.execute(comando)
            busca = cursor.fetchall()
            for resultado in busca:
                print("\033[1;94mNome: ", resultado[0])
                print("Número de partidas: ", resultado[1])
                print("Número de vitórias: ", resultado[2])
                print("Média de vitória / derrota: ", resultado[3])
                print("Nível de habildade: ", resultado[4])
                print("Pontos: ", resultado[5], "\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")

    elif buscar == 2:
        if len(busca) != 0:
            comando1 = f'SELECT jog_ganhador, habilidade_ganhador, jog_perdedor, habilidade_perdedor, resultado FROM historico WHERE jog_ganhador = ("{jogInexistente}")'
            cursor.execute(comando1)
            busca1 = cursor.fetchall()
            for resultado in busca1:
                print("\033[1;94m", resultado, "\033[0;0m")
                
            comando2 = f'SELECT jog_ganhador, jog_perdedor, resultado FROM historico WHERE jog_perdedor = ("{jogInexistente}")'
            cursor.execute(comando2)
            busca2 = cursor.fetchall()
            for resultado in busca2:
                print("\033[1;94m", resultado, "\033[0;0m")

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

            # corrige histórico caso haja a ocasião de o jogador ter jogado "contra si mesmo"
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
                    jogadoresNaFila.remove(jogInexistente)
            
            # atualiza estatísticas
            jogador = jogInexistente
            estatisticas(jogador)

            print("\033[1;92mInformaçôes atualizadas!\033[0;0m")
        else:
            print("\033[1;33mO jogador não está registrado!\033[0;0m")
        
def pontuacaoPingPong():
            E = 0
            D = 0
            pontosEsquerda = 0
            pontosDireita = 0

            print("\033[0;33mDigite \033[0;31mee\033[0;0m \033[0;33mpara retirar um ponto da esquerda e \033[0;31mdd\033[0;0m \033[0;33mpara retirar um ponto da direita.\033[0;0m")

            while E < placarMax and D < placarMax:
                ponto = input("Digite quem fez o ponto (\033[1;34me\033[0;0m para esquerda \033[1;34md\033[0;0m para direita): ")
                if ponto == "e":
                    E += 1
                    pontosEsquerda += 1
                elif ponto == "d":
                    D += 1
                    pontosDireita += 1
                elif ponto == "ee":
                    E -= 1
                    pontosEsquerda -= 1
                elif ponto == "dd":
                    D -= 1
                    pontosDireita -= 1
                if E < 0:
                    E = 0
                    pontosEsquerda = 0
                if D < 0:
                    D = 0
                    pontosDireita = 0
                print("\033[0;34m(Esquerda)", Esquerda, "\033[4;34m\033[1;34m", E, "x", D, "\033[0;0m\033[0;34m", Direita, "(Direita)\033[0;0m")

                if E == tirarDe0 and D == 0:
                    E = placarMax
    
                elif D == tirarDe0 and E == 0:
                    D = placarMax

                if vaiA2 == "s":
                    if E == placarMax - 1 and D == placarMax - 1:
                        print("\033[0;32mFoi a 2\033[0;0m")
                        E = 0
                        D = 0

                        while E < 2 and D < 2:
                            ponto = input("Digite quem fez o ponto: ")
                            if ponto == "e":
                                E += 1
                                pontosEsquerda += 1
                            elif ponto == "d":
                                D += 1
                                pontosDireita += 1
                            elif ponto == "ee":
                                E -= 1
                                pontosEsquerda -= 1
                                if E < 0:
                                    E = 0
                                    pontosEsquerda = 0
                            elif ponto == "dd":
                                D -= 1
                                pontosDireita -= 1
                                if D < 0:
                                    D = 0
                                    pontosDireita = 0
                            print("\033[0;34m(Esquerda)", Esquerda, "\033[4;34m\033[1;34m", E, "x", D, "\033[0;0m\033[0;34m", Direita, "(Direita)\033[0;0m")

                            if E == 1 and D == 1:
                                E -= 1
                                D -= 1
                                print("\033[0;32mFoi a 2 de novo\033[0;0m")
                            if E == 2:
                                E = placarMax
                            elif D == 2:
                                D = placarMax

            if E == placarMax:
                print("\033[1;92mJogador da esquerda", Esquerda, "ganhou\033[0;0m") 
                ganhador = Esquerda
                perdedor = Direita
                pontosGanhador = pontosEsquerda
                pontosPerdedor = pontosDireita
                posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
                print("Nome do jogador que vai entrar agora:\033[0;34m",jogadoresNaFila[0],"\033[0;0m")

            elif D == placarMax:
                print("\033[1;92mJogador da direita", Direita, "ganhou\033[0;0m")
                ganhador = Direita
                perdedor = Esquerda
                pontosGanhador = pontosDireita
                pontosPerdedor = pontosEsquerda
                posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
                print("Nome do jogador que vai entrar agora:\033[0;34m",jogadoresNaFila[0],"\033[0;0m")

opcao = 0
while opcao != "0404":
    adicionar = 0
    deletar = 0
    buscar = 0
    atualizar = 0
    opcao = input("\033[1;96mDigite o número com a respectiva opção que deseja trabalhar:\033[0;0m" 
                  "\n \033[1;92m1.\033[0;0m Adicionar alguém à fila" 
                  "\n \033[1;94m2.\033[0;0m Verificar o próximo da fila" 
                  "\n \033[1;92m3.\033[0;0m Começar os pontos da partida" 
                  "\n \033[1;92m4.\033[0;0m Inserir ganhador e perdedor" 
                  "\n \033[1;91m5.\033[0;0m Tirar alguém da fila"
                  "\n \033[1;94m6.\033[0;0m Ver as estatísticas de um jogador"
                  "\n \033[1;91m7.\033[0;0m Excluir jogador"
                  "\n \033[1;94m8.\033[0;0m Ver jogadores"
                  "\n \033[1;95m9.\033[0;0m Modificar regras"
                  "\n \033[1;94m10.\033[0;0m Ver histórico"
                  "\n \033[1;95m11.\033[0;0m Editar jogador"
                  "\n \033[1;92m12.\033[0;0m Começar torneio"
                  "\n \033[1;91m13.\033[0;0m Encerrar o código" "\n")

    if opcao == "1":
        jogadorNovo = input("\033[0;32mDigite quem entrou na fila: \033[0;0m")
        if jogadorNovo in jogadoresNaFila:
            print("\033[0;33mO jogador já está na fila!\033[0;0m")
        else:
            jogadoresNaFila.insert(-1, jogadorNovo)
            print("\033[1;97m",jogadorNovo, "\033[1;92mfoi adicionado à fila.\033[0;0m")

        jogInexistente = jogadorNovo
        adicionar = 1
        jogadorInexistente()

    elif opcao == "2":
        if len(jogadoresNaFila) == 0:
            print("\033[0;33mSem jogadores na fila!\033[0;0m")
        elif len(jogadoresNaFila) >= 1:
            print("\033[4;34mO próximo da fila é:\033[1;94m",jogadoresNaFila[0],"\033[0;0m")
            print("\033[0;34mA ordem para jogar é:", jogadoresNaFila)

    elif opcao == "3":
        Esquerda = input("\033[0;32mQuem é o jogador da Esquerda? \033[0;0m")
        if Esquerda not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Esquerda)

        jogInexistente = Esquerda
        adicionar = 1
        jogadorInexistente()

        exc = 0
        while exc != 1:
            Direita = input("\033[0;32mQuem é o jogador da Direita? \033[0;0m")

            if Esquerda == Direita:
                print("\033[0;33mUm jogador não pode jogar contra si mesmo!\033[0;0m")
            else:
                exc = 1
        
        if Direita not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, Direita)

        jogInexistente = Direita
        adicionar = 1
        jogadorInexistente()

        print("\033[1;92mA partida começa\033[0;0m")
        pontuacaoPingPong()

    elif opcao == "4":
        ganhador = input("\033[0;32mDigite o \033[1;34mnome\033[0;32m de quem ganhou: \033[0;0m")
        if ganhador not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, ganhador)

        exc = 0
        while exc != 1:
            pontosGanhador = input("\033[0;32mDigite quantos \033[1;34mpontos\033[0;32m fez o ganhador: \033[0;0m")
            if not pontosGanhador.isdigit():
                print("\033[1;33mDigite um número!\033[0;0m")
            elif float(pontosGanhador) < 3:
                print("\033[1;33mO jogador não pode ganhar com menos de 3 pontos!\033[0;0m")
            else:
                exc = 1
                jogInexistente = ganhador
                adicionar = 1
                jogadorInexistente()

        exc = 0
        while exc != 1:
            perdedor = input("\033[0;32mDigite o \033[1;34mnome\033[0;32m de quem perdeu: \033[0;0m")
            if perdedor == ganhador:
                print("\033[1;33mUm jogador não pode jogar contra si mesmo!\033[0;0m")
            else:
                exc = 1

        if perdedor not in jogadoresNaFila:
            jogadoresNaFila.insert(-1, perdedor)
                
        exc = 0
        while exc != 1:
            pontosPerdedor = input("\033[0;32mDigite quantos \033[1;34mpontos\033[0;32m fez o perdedor: \033[0;0m")
            if not pontosPerdedor.isdigit():
                print("\033[1;33mDigite um número!\033[0;0m")
            elif float(pontosPerdedor) > float(pontosGanhador):
                print("\033[1;33mO perdedor não pode ter feito mais pontos que o ganhador!\033[0;0m")
            elif float(pontosPerdedor) == float(pontosGanhador):
                print("\033[1;33mA partida não pode acabar em empate!\033[0;0m")
            else:
                exc = 1
                jogInexistente = perdedor
                adicionar = 1
                jogadorInexistente()

        posJogo(ganhador, perdedor, pontosGanhador, pontosPerdedor)
        print("\033[1;92mFila atualizada!\033[0;0m")
        print("O próximo da fila é:\033[1;33m",jogadoresNaFila[0],"\033[0;0m")

    elif opcao == "5":
        jogadorRemovido = input("\033[0;33mDigite o nome de quem deseja \033[1;91mtirar\033[0;33m da fila: \033[0;0m")
        if jogadorRemovido not in jogadoresNaFila:
            print("\033[1;33mO jogador não está na fila!\033[0;0m")
        else:
            jogadoresNaFila.remove(jogadorRemovido)
            print("\033[1;91mO jogador foi removido da fila.\033[0;0m")

    elif opcao == "6":
        jogInexistente = input("\033[0;34mDigite o nome do jogador que deseja ver as estatísticas: \033[0;0m")
        buscar = 1
        jogadorInexistente()

    elif opcao == "7":
        jogInexistente = input("Digite o nome do jogador que deseja \033[1;33mexcluir\033[0;0m: ")
        deletar = 1
        jogadorInexistente()
        if jogInexistente in jogadoresNaFila:
            jogadoresNaFila.remove(jogInexistente)

    elif opcao == "8":
        escolha = input("Digite \033[1;34m1\033[0;0m para ver todos os jogadores e \033[1;34m2\033[0;0m para o ranking das 3 melhores pontuações: ")
        if escolha == "1":
            comando = f'SELECT nome FROM jogador'
            cursor.execute(comando)
            busca = cursor.fetchall()
            for resultado in busca:
                print("\033[1;94m", resultado[0], "\033[0;0m")
            if len(busca) == 0:
                print("\033[1;33mSem jogadores cadastrados!\033[0;0m")
        elif escolha == "2":
            rankingDeJogadores()
        else:
            print("\033[1;33mSelecione uma opção válida!\033[0;0m")

    elif opcao == "9":
        exc = 0
        while exc != 1:
            placarMax = input("Selecione a quantidade de \033[1;34mpontos\033[0;0m necessários para \033[1;34mvencer\033[0;0m a partida: ")
            if not placarMax.isdigit():
                print("\033[1;33mDigite um número!\033[0;0m")
            elif float(placarMax) < 3:
                print("\033[1;33mNo mínimo 3 pontos para vitória!\033[0;0m")
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
            elif float(tirarDe0) < 3:
                print("\033[1;33mNo mínimo 3 pontos para tirar de 0!\033[0;0m")
            else:
                exc = 1
                tirarDe0 = float(tirarDe0)

        print("\033[1;92mRegras atualizadas!\033[0;0m")

    elif opcao == "10":
        escolha = input("Digite \033[1;34m1\033[0;0m para histórico completo e \033[1;34m2\033[0;0m para o histórico de um jogador específico: ")
        if escolha == "1":
            comando = f'SELECT jog_ganhador, habilidade_ganhador, jog_perdedor, habilidade_perdedor, resultado FROM historico'
            cursor.execute(comando)
            busca = cursor.fetchall()
            for resultado in busca:
                print("\033[1;94m", resultado, "\033[0;0m")
            if len(busca) == 0:
                print("\033[1;33mSem partidas registradas!\033[0;0m")
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
        print("\033[0;33mFunção incompleta...\033[0;0m")

    elif opcao == "13":
        print("\033[1;36mPrograma encerrado, agradecemos por usar nosso trabalho!\033[0;0m")

    elif opcao == "deletar partidas":
        comando = 'DELETE from historico'
        cursor.execute(comando)
        conexao.commit() 
        print("\033[1;31mHistórico completamente apagado.\033[0;0m")

    elif opcao == "deletar jogadores":
        comando = 'DELETE from jogador'
        cursor.execute(comando)
        conexao.commit() 
        jogadoresNaFila = []
        print("\033[1;31mJogadores apagados.\033[0;0m")

    else:
        print("\033[1;33mSelecione uma opção válida!\033[0;0m")

cursor.close()
conexao.close()