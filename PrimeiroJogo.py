import random

class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"{self.nome} ({self.classe}) - Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}"

def batalhar(heroi, monstro):
    print("Batalha começou!")
    while heroi.esta_vivo() and monstro.esta_vivo():
        print("----")
        print(heroi)
        print(monstro)
        print("----")
        heroi.atacar(monstro)
        if monstro.esta_vivo():
            monstro.atacar(heroi)
    if heroi.esta_vivo():
        print("Você venceu!")
    else:
        print("Você foi derrotado...")

def main():
    print("Bem-vindo ao jogo de RPG!")
    nome = input("Digite o nome do seu personagem: ")
    classe = input("Escolha a classe do seu personagem (Guerreiro/Mago/Arqueiro): ")
    vida = 100
    ataque = random.randint(10, 20)
    defesa = random.randint(5, 15)

    heroi = Personagem(nome, classe, vida, ataque, defesa)
    monstro = Personagem("Goblin", "Monstro", 50, 15, 5)

    print("Um terrível goblin apareceu! Prepare-se para a batalha!")
    batalhar(heroi, monstro)

if __name__ == "__main__":
    main()