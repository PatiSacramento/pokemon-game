class Pokemon:
    # construtor:
    def __init__(self, tipo, especie, level=1, nome=None): 
        self.tipo = tipo
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} (level {})".format(self.nome, self.level)


    def atacar(self, pokemon):
        print("{} atacou {}!".format(self, pokemon))




meu_pokemon = Pokemon("fogo", "charmander", nome="carlos", level=50)
pokemon_amigo = Pokemon("eletrico", "pikachu")

print(meu_pokemon)