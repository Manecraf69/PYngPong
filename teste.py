import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='20122004',
    database='pyngpong_bd',
)
cursor = conexao.cursor()

Teste = 11

if Teste == 1:

    ganhador = "pedro"
    perdedor = "claudio"
    resultado = "3x0"

    comando1 = f'INSERT INTO historico (jog_ganhador, jog_perdedor, resultado) VALUES ("{ganhador}","{perdedor}","{resultado}")'
    cursor.execute(comando1)
    conexao.commit() 

elif Teste == 2:

    ganhador = "Marcio"
    perdedor = "Paulo"

    ganhador = "Paulo"
    perdedor = "Marcio"

    comando = f'SELECT jog_ganhador FROM historico WHERE jog_ganhador = ("{ganhador}")'
    cursor.execute(comando)
    buscaGanhador1 = cursor.fetchall()

    comando = f'SELECT jog_perdedor FROM historico WHERE jog_perdedor = ("{ganhador}")'
    cursor.execute(comando)
    buscaGanhador2 = cursor.fetchall()

    n_partidas = len(buscaGanhador1) + len(buscaGanhador2)

    comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    conexao.commit() 

    comando = f'SELECT jog_perdedor FROM historico WHERE jog_perdedor = ("{perdedor}")'
    cursor.execute(comando)
    buscaPerdedor1 = cursor.fetchall()

    comando = f'SELECT jog_ganhador FROM historico WHERE jog_ganhador = ("{perdedor}")'
    cursor.execute(comando)
    buscaPerdedor2 = cursor.fetchall()

    n_partidas = len(buscaPerdedor1) + len(buscaPerdedor2)

    comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    conexao.commit() 

elif Teste == 3:

    ganhador = "Marcio"
    perdedor = "Paulo"

    # ganhador = "Paulo"
    # perdedor = "Marcio"

    comando = f'SELECT jog_ganhador, jog_perdedor FROM historico WHERE jog_ganhador = ("{ganhador}")'
    cursor.execute(comando)
    buscaGanhador = cursor.fetchall()

    n_partidas = len(buscaGanhador)

    comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    conexao.commit() 

    comando = f'SELECT jog_perdedor, jog_ganhador FROM historico WHERE jog_perdedor = ("{perdedor}")'
    cursor.execute(comando)
    buscaPerdedor = cursor.fetchall()

    n_partidas = len(buscaPerdedor)

    comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    conexao.commit() 

    print(buscaGanhador, buscaPerdedor)

elif Teste == 4:

    well = [67, 9.89, 5]
    rodrigo = [74, 8.23, 5]
    marcio = [102, 4.09, 4]
    bololo = [30, 0.21, 1]
    paulo = [26, 2.01, 2]

    teste1 = [0, 0.00, 0] # ganha
    teste2 = [0, 0.00, 0]

    teste1 = [1, 1.00, 2] # ganha dnv
    teste2 = [1, 0.00, 0]

    # if media_vitder < 1:
    #     pontos + 0
    # elif media_vitder > 1 and media_vitder < 3:
    #     pontos + 1
    # elif media_vitder > 3 and media_vitder < 5:
    #     pontos + 2
    # elif media_vitder > 5 and media_vitder < 3:
    #     pontos + 3
    # elif media_vitder > 7:
    #     pontos + 4

    # if media_vitder < 1:
    #     pontos - 4
    # elif media_vitder > 1 and media_vitder < 3:
    #     pontos - 3
    # elif media_vitder > 3 and media_vitder < 5:
    #     pontos - 2
    # elif media_vitder > 5 and media_vitder < 3:
    #     pontos - 1
    # elif media_vitder > 7:
    #     pontos - 0

    a = 0

elif Teste == 5:

    comando = f'SELECT partidas FROM jogador WHERE nome = "Marcio"'
    cursor.execute(comando)
    busca = cursor.fetchall()

    variavel = busca[0][0]

    variavel *= 5

    print(variavel)

    Teste6 =6

    ganhador = "Marcio"
    perdedor = "Paulo"

    habilidade_ganhador = 4
    habilidade_perdedor = 2

    if habilidade_perdedor == 5:
        pontos_ganhos = 4
    elif habilidade_perdedor == 4:
        pontos_ganhos = 3
    elif habilidade_perdedor == 3:
        pontos_ganhos = 2
    elif habilidade_perdedor == 2:
        pontos_ganhos = 1
    elif habilidade_perdedor == 1:
        pontos_ganhos = 0

    comando = f'SELECT pontos FROM jogador WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    busca = cursor.fetchall()

    variavel = busca[0][0]
    variavel += pontos_ganhos

    comando = f'UPDATE jogador SET pontos = ("{variavel}") WHERE nome = ("{ganhador}")'
    cursor.execute(comando)
    conexao.commit() 

    if habilidade_ganhador == 5:
        pontos_perdidos = 0
    elif habilidade_ganhador == 4:
        pontos_perdidos = 1
    elif habilidade_ganhador == 3:
        pontos_perdidos = 2
    elif habilidade_ganhador == 2:
        pontos_perdidos = 3
    elif habilidade_ganhador == 1:
        pontos_perdidos = 4

    comando = f'SELECT pontos FROM jogador WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    busca = cursor.fetchall()

    variavel = busca[0][0]
    variavel -= pontos_perdidos

    comando = f'UPDATE jogador SET pontos = ("{variavel}") WHERE nome = ("{perdedor}")'
    cursor.execute(comando)
    conexao.commit() 

elif Teste == 6:

    var1 = 5
    var2 = 6

    if var1 == var2 - 1:
        print("ae sim")

elif Teste == 7:

    comando = f'UPDATE jogador SET partidas = 15 WHERE nome = "Marcio999"'
    cursor.execute(comando)
    conexao.commit()

    comando = f'SELECT pontos, nome FROM jogador WHERE nome = "Marcio"'
    cursor.execute(comando)
    busca1 = cursor.fetchall()
                
    pontosJogadorAntigo = busca1[0][0]
    nomeJogadorAntigo = busca1[-1][-1]
    print(pontosJogadorAntigo, nomeJogadorAntigo)

elif Teste == 8:
    lista1 = []
    lista2 = []

    jogInexistente = "Marcio"
    comando = f'SELECT id_partida FROM historico where jog_ganhador = ("{jogInexistente}")'
    cursor.execute(comando)
    busca1 = cursor.fetchall()

    for resultado in busca1:
        lista1.append(resultado)

    comando = f'SELECT id_partida FROM historico where jog_perdedor = ("{jogInexistente}")'
    cursor.execute(comando)
    busca2 = cursor.fetchall()

    for resultado in busca2:
        lista2.append(resultado)

    iguais = [elemento for elemento in lista1 if elemento in lista2]
    batatas = 0
    for i in iguais:
        print(i)
        jooj = iguais[0]
        jooj1 = str(iguais[batatas])
        batatas += 1
        jooj1 = jooj1.replace(",)", "")
        jooj1 = jooj1.replace("(", "")

        comando = f'DELETE FROM historico WHERE id_partida = ("{jooj1}")'
        cursor.execute(comando)
        conexao.commit()

elif Teste == 9:
    lista1 = []
    lista2 = []
    suamae = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    jogInexistente = "Marcio"
    comando = f'SELECT id_partida FROM historico where jog_ganhador = ("{jogInexistente}")'
    cursor.execute(comando)
    busca1 = cursor.fetchall()

    for resultado in busca1:
        lista1.append(resultado)

    comando = f'SELECT id_partida FROM historico where jog_perdedor = ("{jogInexistente}")'
    cursor.execute(comando)
    busca2 = cursor.fetchall()

    for resultado in busca2:
        lista2.append(resultado)

    iguais = [elemento for elemento in lista1 if elemento in lista2]
    for i in iguais:
        print(iguais)
        jooj = iguais[0]

elif Teste == 10:
    opcao = input("\033[1;96mDigite o número com a respectiva opção que deseja trabalhar:\033[0;0m" 
                  "\n \033[0;97m1. \033[4;32mAdicionar alguém à fila\033[0;0m" 
                  "\n \033[0;97m2. \033[4;34mVerificar o próximo da fila\033[0;0m" 
                  "\n \033[0;97m3. \033[4;32mComeçar os pontos da partida\033[0;0m" 
                  "\n \033[0;97m4. \033[4;32mInserir ganhador e perdedor\033[0;0m" 
                  "\n \033[0;97m5. \033[4;31mTirar alguém da fila\033[0;0m"
                  "\n \033[0;97m6. \033[4;34mVer as estatísticas de um jogador\033[0;0m"
                  "\n \033[0;97m7. \033[4;31mExcluir jogador\033[0;0m"
                  "\n \033[0;97m8. \033[4;34mVer jogadores\033[0;0m"
                  "\n \033[0;97m9. \033[4;35mModificar regras\033[0;0m"
                  "\n \033[0;97m10. \033[4;34mVer histórico\033[0;0m"
                  "\n \033[0;97m11. \033[4;35mEditar jogador\033[0;0m"
                  "\n \033[0;97m12. \033[4;31mEncerrar o código\033[0;0m" "\n")

elif Teste == 11:
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
                  "\n \033[1;91m12.\033[0;0m Encerrar o código" "\n")

elif Teste == 12:
    jogador = "Ricardo"

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

    print(n_partidas, "partidas,", n_vitorias, "vitorias,", n_derrotas, "derrotas,", media_vitder, "media.")

elif Teste == 13:
    pontosDosJogadores = []

    comando = f'SELECT pontos FROM jogador'
    cursor.execute(comando)
    pontos = cursor.fetchall()

    for i in pontos:
        # print(i[0])
        pontosDosJogadores.append(i[0])

    pontosDosJogadores.sort(reverse = True)
    # print(pontosDosJogadores)

    indexDaLista = 0
    if len(pontosDosJogadores) > 0:
        print("Nome do jogador, pontos e número de partidas: ")
        for i in pontosDosJogadores:
            # print(pontosDosJogadores[indexDaLista])
            comando = f'SELECT nome, pontos, partidas FROM jogador WHERE pontos = ("{pontosDosJogadores[indexDaLista]}")'
            cursor.execute(comando)
            nomeJogadorRankeado = cursor.fetchall()
            for i in nomeJogadorRankeado:
                print(i)
            if indexDaLista == 3:
                break
            indexDaLista += 1
    else:
        print("Não há jogadores cadastrados!")
        
cursor.close()
conexao.close()