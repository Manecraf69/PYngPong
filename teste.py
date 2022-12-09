import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='20122004',
    database='pyngpong_bd',
)
cursor = conexao.cursor()

Teste1 = 1

# ganhador = "pedro"
# perdedor = "claudio"
# resultado = "3x0"

# comando1 = f'INSERT INTO historico (jog_ganhador, jog_perdedor, resultado) VALUES ("{ganhador}","{perdedor}","{resultado}")'
# cursor.execute(comando1)
# conexao.commit() 

Teste2 = 2

# ganhador = "Marcio"
# perdedor = "Paulo"

# ganhador = "Paulo"
# perdedor = "Marcio"

# comando = f'SELECT jog_ganhador FROM historico WHERE jog_ganhador = ("{ganhador}")'
# cursor.execute(comando)
# buscaGanhador1 = cursor.fetchall()

# comando = f'SELECT jog_perdedor FROM historico WHERE jog_perdedor = ("{ganhador}")'
# cursor.execute(comando)
# buscaGanhador2 = cursor.fetchall()

# n_partidas = len(buscaGanhador1) + len(buscaGanhador2)

# comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{ganhador}")'
# cursor.execute(comando)
# conexao.commit() 

# comando = f'SELECT jog_perdedor FROM historico WHERE jog_perdedor = ("{perdedor}")'
# cursor.execute(comando)
# buscaPerdedor1 = cursor.fetchall()

# comando = f'SELECT jog_ganhador FROM historico WHERE jog_ganhador = ("{perdedor}")'
# cursor.execute(comando)
# buscaPerdedor2 = cursor.fetchall()

# n_partidas = len(buscaPerdedor1) + len(buscaPerdedor2)

# comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{perdedor}")'
# cursor.execute(comando)
# conexao.commit() 

Teste3 = 3

# ganhador = "Marcio"
# perdedor = "Paulo"

# # ganhador = "Paulo"
# # perdedor = "Marcio"

# comando = f'SELECT jog_ganhador, jog_perdedor FROM historico WHERE jog_ganhador = ("{ganhador}")'
# cursor.execute(comando)
# buscaGanhador = cursor.fetchall()

# n_partidas = len(buscaGanhador)

# comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{ganhador}")'
# cursor.execute(comando)
# conexao.commit() 

# comando = f'SELECT jog_perdedor, jog_ganhador FROM historico WHERE jog_perdedor = ("{perdedor}")'
# cursor.execute(comando)
# buscaPerdedor = cursor.fetchall()

# n_partidas = len(buscaPerdedor)

# comando = f'UPDATE jogador SET total_partida = ("{n_partidas}") WHERE nome = ("{perdedor}")'
# cursor.execute(comando)
# conexao.commit() 

# print(buscaGanhador, buscaPerdedor)

Teste4 = 4

# well = [67, 9.89, 5]
# rodrigo = [74, 8.23, 5]
# marcio = [102, 4.09, 4]
# bololo = [30, 0.21, 1]
# paulo = [26, 2.01, 2]

# teste1 = [0, 0.00, 0] # ganha
# teste2 = [0, 0.00, 0]

# teste1 = [1, 1.00, 2] # ganha dnv
# teste2 = [1, 0.00, 0]

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

Teste5 = 5

# comando = f'SELECT partidas FROM jogador WHERE nome = "Marcio"'
# cursor.execute(comando)
# busca = cursor.fetchall()

# variavel = busca[0][0]

# variavel *= 5

# print(variavel)

# Teste6 =6

# ganhador = "Marcio"
# perdedor = "Paulo"

# habilidade_ganhador = 4
# habilidade_perdedor = 2

# if habilidade_perdedor == 5:
#     pontos_ganhos = 4
# elif habilidade_perdedor == 4:
#     pontos_ganhos = 3
# elif habilidade_perdedor == 3:
#     pontos_ganhos = 2
# elif habilidade_perdedor == 2:
#     pontos_ganhos = 1
# elif habilidade_perdedor == 1:
#     pontos_ganhos = 0

# comando = f'SELECT pontos FROM jogador WHERE nome = ("{ganhador}")'
# cursor.execute(comando)
# busca = cursor.fetchall()

# variavel = busca[0][0]
# variavel += pontos_ganhos

# comando = f'UPDATE jogador SET pontos = ("{variavel}") WHERE nome = ("{ganhador}")'
# cursor.execute(comando)
# conexao.commit() 

# if habilidade_ganhador == 5:
#     pontos_perdidos = 0
# elif habilidade_ganhador == 4:
#     pontos_perdidos = 1
# elif habilidade_ganhador == 3:
#     pontos_perdidos = 2
# elif habilidade_ganhador == 2:
#     pontos_perdidos = 3
# elif habilidade_ganhador == 1:
#     pontos_perdidos = 4

# comando = f'SELECT pontos FROM jogador WHERE nome = ("{perdedor}")'
# cursor.execute(comando)
# busca = cursor.fetchall()

# variavel = busca[0][0]
# variavel -= pontos_perdidos

# comando = f'UPDATE jogador SET pontos = ("{variavel}") WHERE nome = ("{perdedor}")'
# cursor.execute(comando)
# conexao.commit() 

Teste6 = 6

# var1 = 5
# var2 = 6

# if var1 == var2 - 1:
#     print("ae sim")

Teste7 = 7

# comando = f'UPDATE jogador SET partidas = 15 WHERE nome = "Marcio999"'
# cursor.execute(comando)
# conexao.commit()

# comando = f'SELECT pontos, nome FROM jogador WHERE nome = "Marcio"'
# cursor.execute(comando)
# busca1 = cursor.fetchall()
            
# pontosJogadorAntigo = busca1[0][0]
# nomeJogadorAntigo = busca1[-1][-1]
# print(pontosJogadorAntigo, nomeJogadorAntigo)

cursor.close()
conexao.close()