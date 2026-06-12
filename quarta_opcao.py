class Hero:
    def __init__(self, heroName, age, tipe):
        self.heroName = heroName
        self.age = age
        self.tipe = tipe

    def combat(self):
        fight = {
            "Arcanista": "Raio Gélido",
            "Arqueiro": "Tiro Múltiplo",
            "Monge": "Palma Explosiva",
            "Necromante": "Mago Esqueleto",
            "Paladino": "Escudo Reluzente"
        }

        combat = fight[self.tipe]

        print(f"O {self.tipe} atacou usando {combat}")


hero_1 = Hero("Rathma", 35, "Necromante")
hero_2 = Hero("Esu", 32, "Arcanista" )

hero_1.combat()
hero_2.combat()
