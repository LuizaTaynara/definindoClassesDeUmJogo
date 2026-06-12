class buildingHero{
    constructor(nameHero, age, tipe, attack){
        this.nameHero = nameHero
        this.age = age
        this.tipe = tipe
        this.attack = attack
    }
    fight(){
        console.log(`O ${this.tipe} atacou usando ${this.attack}`)
    }
}

let hero = new buildingHero("Eleven", 23, "Arcanista", "Raio Gélido")

hero.fight()
