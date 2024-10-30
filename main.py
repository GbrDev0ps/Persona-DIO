class Personagem:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        
    def ataque(self):
        
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "Usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "Usou shuriken"
            
        print(f"O {self.tipo} {ataque}")
        
        
persona1 = Personagem("Unknown", 99, "monge")
persona1.ataque()
            