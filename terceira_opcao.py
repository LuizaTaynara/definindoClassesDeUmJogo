class Hero:
    def __init__(self, heroName, age, tipe):
        self.heroName = heroName
        self.age = age
        self.tipe = tipe

    def combat(self):
        fight = ""

        if self.tipe == "Arcanista":
            fight = "Raio Gélido"
        elif self.tipe == "Arqueiro":
            fight = "Tiro Múltiplo"
        elif self.tipe == "Monge":
            fight = "Palma Explosiva"
        elif self.tipe == "Necromante":
            fight = "Mago Esqueleto"
        elif self.tipe == "Paladino":
            fight = "Escudo Reluzente"

        print(f"O {self.tipe} atacou usando {fight}")


hero_1 = Hero("Aang", 13, "Monge")
hero_2 = Hero("Katara", 14, "Arcanista" )

hero_1.combat()
hero_2.combat()
