class hero {
    constructor(heroName, age, tipe) {
        this.heroName = heroName
        this.age = age
        this.tipe = tipe
    }

    combat() {
        let fight = ""

        switch (this.tipe) {
            case "Arcanista":
                fight = "Raio Gélido"
                break;

            case "Arqueiro":
                fight = "Tiro Múltiplo"
                break

            case "Monge":
                fight = "Palma Explosiva"
                break

            case "Necromante":
                fight = "Mago Esqueleto"
                break

            case "Paladino":
                fight = "Escudo Reluzente";
                break
        }

        console.log(`O ${this.tipe} atacou usando ${fight}`)
    }
}

let hero1 = new hero("Gavião Arqueiro", 20, "Arqueiro")
let hero2 = new hero("Sauron", 18, "Necromante")

hero1.combat()
hero2.combat()
