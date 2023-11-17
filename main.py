import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
)

cursor = banco.cursor()

while True:

    menu = input("O que você deseja fazer? 1 Adicionar \n | 2 Ler \n |3 Atualizar \n 4 Deletar: ")
    if menu == '1':
        tabelas = input("Em qual tabela você deseja realizar a ação: ")
        if tabelas == "Aluno":
            nome = input("Digite o nome do aluno: ")
            endereco = input("Digite o telefone para contato: ")
            telefone = input("Informe o endereço: ")
            adicionar = f' insert into alunos (nome_aluno,endereço,telefone) VALUES ("{nome}","{endereco}","{telefone}")'
            cursor.execute(adicionar)
            banco.commit()
        elif tabelas == "Modalidades":
            nome = input("Digite o nome da modalidade: ")
            turno = input("Digite o turno: ")
            duracao = input("Informe o tempo de duração: ")
            adicionar = f' insert into modalidade (nome,turno,duracao) VALUES ("{nome}","{turno}","{duracao}")'
            cursor.execute(adicionar)
            banco.commit()

        elif tabelas == "Personal":
            nome = input("Digite o nome do personal: ")
            cref = input("Digite o cref: ")
            adicionar = f' insert into personal (nome,cref) VALUES ("{nome}","{cref}")'
            cursor.execute(adicionar)
            banco.commit()

        else:
            print("opção invalida")


    elif menu == "2":
        tabelas = input("Em qual tabela você deseja realizar a ação: ")

        if tabelas == "aluno":
            leitura = f'select * from alunos'
            cursor.execute(leitura)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)

        elif tabelas == "Modalidade":
            leitura = f'select * from modalidade'
            cursor.execute(leitura)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)

        elif tabelas == "Personal":
            leitura = f'select * from personal'
            cursor.execute(leitura)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)

        else:
            print("Opção inválida")








    elif menu == "4":
        tabelas = input("Em qual tabela você deseja realizar a ação: ")
        if tabelas == "Aluno":
            menu2 = input("Digite a coluna que você quer trabalhar: ")
            if menu2 == no
        elif tabelas == "Modalidades":

        elif tabelas == "Personal":
