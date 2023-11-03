class ContaBancaria:

    def __init__(self, num_c, nome_c, tipo_c):
        self.numconta = num_c
        self.saldo = 0
        self.statusconta = False
        self.nomeconta = nome_c
        self.tipoconta = tipo_c
        self.limite = 0

    def depositar(self, deposito):
        if self.statusconta == True:
            if self.saldo < 0:
                self.saldo += deposito
                self.limite += (deposito - self.saldo)
                print(f"Depósito efetuado com sucesso.\n"
                      f"Você possui R${self.saldo} e R${self.limite} de limite.")
            else:
                self.saldo += deposito
                print(f"Depósito efetuado com sucesso.\n"
                      f"Você possui R${self.saldo} e R${self.limite} de limite.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def sacar(self, saque):
        if self.statusconta == True:
            if self.saldo + self.limite - saque >= 0:
                self.saldo -= saque
                if self.saldo < 0:
                    self.limite += self.saldo
                    print(f"Saque efetuado com sucesso.\n"
                          f"Você possui R${self.saldo} e R${self.limite} de limite.")
                else:
                    print(f"Saque efetuado com sucesso.\n"
                          f"Você possui R${self.saldo} e R${self.limite} de limite.")
            else:
                print(f"Saldo insuficiente.\n"
                      f"Você possui R${self.saldo} e R${self.limite} de limite.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def versaldo(self):
        if self.statusconta == True:
            print(f"Olá {self.nomeconta}, você possui R${self.saldo} em conta."
                  f"\nE possui um limite de R${self.limite}.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def ativarconta(self):
        if self.statusconta == True:
            print(f"{self.nomeconta} sua conta já está ativa.")
        else:
            print("Conta ativada com sucesso!")
            self.statusconta = True

    def desativarconta(self):
        if self.statusconta == True:
            if self.saldo == 0:
                print("Conta desativada com sucesso!")
            else:
                print("Para desativar a conta primeiro zere o seu saldo.")
        else:
            print("Sua conta já está inativa")

    def ativarlimite(self, limite):
        if self.statusconta == True:
            self.limite += limite
        else:
            print("Por favor ative sua conta antes de usar.")

    def desativalimite(self):
        if self.statusconta == True:
            self.limite = 0
        else:
            print("Por favor ative sua conta antes de usar.")


class Animal:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer. . .")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando. . .")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} foi latindo . . .")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunhir(self):
        print(f"O {self.nome} foi grunhindo . . .")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"O {self.nome} foi mugindo . . .")
