#criar o banco de dados
from sys import exit

import sqlite3

conn = sqlite3.connect('pj2018')
curs = conn.cursor()

#tblcmd = "create table sortudos (a char(30), b char(30), c char(2), d char(9), e char(30), f char(2), g char(9), h char(1))"
#curs.execute(tblcmd)

def InserirDados():
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    a = input("Entre com o CÓDIGO: \n->")
    b = input("Entre com o NOME DO AMIGO DA SORTE: \n->")
    c = input("Entre com o DDD DO AMIGO DA SORTE: \n->")
    d = input("Entre com o TELEFONE DO AMIGO DA SORTE: \n->")
    e = input("Entre com o NOME DO PARTICIPANTE: \n->")
    f = input("Entre com o DDD DO PARTICIPANTE: \n->")
    g = input("Entre com o TELEFONE DO PARTICIPANTE: \n->")
    h = input("Entre com a OPÇÃO ESCOLHIDA PELO PARTICIPANETE: \n->")
    query = "insert into sortudos (a, b, c, d, e, f, g, h) values ('%s','%s','%s', '%s', '%s','%s','%s','%s');" % (a,b,c,d,e,f,g,h)
    curs.execute(query)
    conn.commit()


def PesquisaSorteado():
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    resposta = input("Digite o número de telefone do Participante: \n->")
    curs.execute("""
    select * from sortudos where g = '%s';""" % (resposta))
    x = 0
    for row in curs.fetchall():
        x = x + 1
        print("\nCódigo: ", row[0])
        print("\nAmigo da sorte: ", row[1])
        print("\nTelefone do amigo da sorte: ", row[2], row[3])
        print("\nNome do sorteado: ", row[4])
        print("\nTelefone do sorteado: ", row[5], row[6], " -> Opção escolhida: ", row[7])
    print("\nNome do sorteado: ", row[4])
    print("O total de registro é: ", x)

def Pesquisa_Amigo_da_Sorte():
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    resposta = input("Digite o número de telefone do Amigo da Sorte: \n->")
    curs.execute("""
    select * from sortudos where d = '%s';""" % (resposta))
    x = 0
    for row in curs.fetchall():
        x = x + 1
        print("\nCódigo: ", row[0])
        print("\nAmigo da sorte: ", row[1])
        print("\nTelefone do amigo da sorte: ", row[2], row[3])
        print("\nNome do sorteado: ", row[4])
        print("\nTelefone do sorteado: ", row[5], row[6], " -> Opção escolhida: ", row[7])  
    print("\nAmigo da sorte: ", row[1])
    print("O total de registro é: ", x)


def ContaRegistros():
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    curs.execute("select * from sortudos;")
    x = 0
    for row in curs.fetchall():
        x = x + 1
    print("O total de registro é: ", x)



def Ver_Nomes_Telefones():
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    curs.execute("select * from sortudos;")
    x = 0
    for row in curs.fetchall():
        x = x + 1
        print("\nNome do sorteado: ", row[4])
        print("\nTelefone do sorteado: ", row[5], row[6], " -> Opção escolhida: ", row[7])
    print("O total de registro é: ", x)



def Sorteio():
    import random
    import sqlite3
    conn = sqlite3.connect('pj2018')
    curs = conn.cursor()
    curs.execute("select g from sortudos;")
    lista = []
    for row in curs.fetchall():
        lista.append(row)
    sorteio = random.choice(lista)
    print(lista,'\n')
    print("E o número sorteado foi: ", sorteio)
    curs.execute("""
    select * from sortudos where g = '%s';""" % (sorteio))
    x = 0
    for row in curs.fetchall():
        x = x + 1
        print("\nCódigo: ", row[0])
        print("\nAmigo da sorte: ", row[1])
        print("\nTelefone do amigo da sorte: ", row[2], row[3])
        print("\nNome do sorteado: ", row[4])
        print("\nTelefone do sorteado: ", row[5], row[6], " -> Opção escolhida: ", row[7])
    print("\nNome do sorteado: ", row[4])
    print("O total de registro é: ", x)
    







    


def Inicio():
    resposta = input("""\nDigite:\n\n '1' para pesquisar por Amigo da Sorte... \n\n '2' para pesquisar por Participante... \n\n '3' para Cadastrar Novos... \n\n '4' para Contar Registros ...\n\n '5' Ver Nomes e Telefones dos Participantes...\n\n '6' para Sortear ...\n\n '7' para Sair... \n\n->""")
    if resposta == str(1):
        Pesquisa_Amigo_da_Sorte()
    elif resposta == str(2):
        PesquisaSorteado()
    elif resposta == str(3):
        InserirDados()
    elif resposta == str(4):
        ContaRegistros()
    elif resposta == str(5):
        Ver_Nomes_Telefones()
    elif resposta == str(6):
        Sorteio()
    else:
        exit()

try:
    while True:
        Inicio()
except:
    print("Falha no programa.")
    print("Reiniciando...")
