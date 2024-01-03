import requests

# Select the pokemon
pokemon_name = input("Enter name: ")
pokemon_url = "https://pokeapi.co/api/v2/pokemon/"+pokemon_name

# Get the .json file
response = requests.get(pokemon_url)

# Verify response
if response.status_code==200:
    pass
else:
    print("Invalid response, please check the input name.")
    exit()

# Pokemon class
class pokemon_class:
    def __init__(self, id, type, height, weight, hp, attack, defense, specialattack, speed):

        self.id = id
        self.type = type
        self.height = height
        self.weight = weight
        self.hp = hp
        self.attack = attack 
        self.defense = defense
        self.specialattack = specialattack
        self.speed = speed

# Parse the .json file
pokemon = pokemon_class(response.json()['id'],
                        response.json()['types'][0]['type']['name'],
                        (response.json()['height'])*10,
                        (response.json()['weight'])/10,
                        response.json()['stats'][0]['base_stat'],
                        response.json()['stats'][1]['base_stat'],
                        response.json()['stats'][2]['base_stat'],
                        response.json()['stats'][3]['base_stat'],
                        response.json()['stats'][4]['base_stat'])

# Print obtained value
print("ID: "+str(pokemon.id))
print("Type: "+pokemon.type)
print("Height: "+str(pokemon.height)+" cm")
print("Weight: "+str(pokemon.weight)+" kg")
print("HP: "+str(pokemon.hp))
print("Attack: "+str(pokemon.attack))
print("Defense: "+str(pokemon.defense))
print("S-A: "+str(pokemon.specialattack))
print("Speed: "+str(pokemon.speed))
