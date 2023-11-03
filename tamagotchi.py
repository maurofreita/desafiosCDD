class Pessoa:

    def __init__(self, n, i, p, c=False, d=False, a=False):
        self.nome = n
        self.idade = i
        self.peso = p
        self.comendo = c
        self.dormindo = d
        self.andando = a

    def andar(self):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.andando = True
            print(f"{self.nome} foi andar. . .")
        elif self.andando == True:
            print(f"{self.nome} ainda está andando")

    def parar_andar(self):
        if self.andando == True:
            self.andando = False
            print(f"{self.nome} terminou de andar.")
        else:
            print(f"{self.nome} não está andando.")

    def comer(self, comida):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.comida = comida
            self.comendo = True
            print(f"{self.nome} foi comer {self.comida}")
        elif self.comendo == True:
            print(f"Termine sua comida antes de comer novamente.")

    def parar_comer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} terminou de comer.")
        else:
            print(f"{self.nome} não está comendo.")

    def dormir(self):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} foi dormir. . .")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} acordou.")
        else:
            print(f"{self.nome} não está dormindo.")