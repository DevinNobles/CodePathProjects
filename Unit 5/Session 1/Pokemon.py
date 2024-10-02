pokelist = []


class Pokemon:

    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
        pokelist.append(self)
    
    def __repr__(self):
        return self.name

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    def catch(self):
        self.is_caught = True
        print(f"You caught a {self.name}!")
    
    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I Choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
    
    def addType(self, ntype):
        self.types.append(ntype)
    
        
def get_by_type(my_pokemon, pokemon_type):
    # Initialize an empty list to hold the Pokémon that match the type
    filtered_pokemon = []
    
    # Iterate over each Pokémon in the provided list
    for pokemon in my_pokemon:
        # Check if the specified type is in the Pokémon's types
        if pokemon_type in pokemon.types:
            filtered_pokemon.append(pokemon)  # Add matching Pokémon to the result list
    
    print(filtered_pokemon)  # Return the list of filtered Pokémon

def get_evolutionary_line(starter_pokemon, evolveList=None):
    if evolveList is None:
        evolveList = []  # Initialize the list only once at the top level

    evolveList.append(starter_pokemon)  # Add the current Pokémon to the list

    if starter_pokemon.evolution is not None:
        get_evolutionary_line(starter_pokemon.evolution, evolveList)
    
    return evolveList


Pikachu = Pokemon("Pikachu", ["Electric"])
Squirtle = Pokemon("Squirtle", ["Water"])
Jigglypuff = Pokemon("Jigglypuff", ["Normal"])
Diglett = Pokemon("Diglett", ["Ground"])
Meowth = Pokemon("Meowth", ["Normal"])
Pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
Blastoise = Pokemon("Blastoise", ["Water"])

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)
"""
Squirtle.catch()
Pikachu.choose()
Squirtle.choose()
Jigglypuff.addType("Fairy")
print(pokelist)

get_by_type(pokelist, "Normal")
"""
lst = get_evolutionary_line(charmander)
print(lst)
