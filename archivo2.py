from pip._vendor import requests

class Pokemon:
    def __init__(self):
        self.__nombre=""
        self.__habilidades=""
        self.__url=[]
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_atributos(self,habilidades):
        self.__habilidades=habilidades

    def get_atributos(self):
        return self.__nombre, self.__habilidades,self.__url
    def get_nombre(self):
        return self.__nombre
    def get_habilidades(self):
        return self.__habilidades
    def get_url(self):
        return self.__url
    def info(self):
      data_pokemon=extract_json(f'https://pokeapi.co/api/v2/pokemon/{self.__nombre}')
      self.__habilidades = extract_habilidades(data_pokemon)
      url_imagen= data_pokemon['sprites']['other']
      self.__url=url_imagen['official-artwork']['front_default']

      print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')  
      print(f'Name: {self.__nombre}')
      print(f'Abilities {self.__nombre}: ',', '.join(self.__habilidades))
      print(f'Image URL: ',self.__url)
      print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')  
      
def extract_json(url):
    json1=requests.get(url,stream=True)
    json1=json1.json()
    return json1   
def extract_habilidades(datos):
  return [elem['ability']['name'] for elem in datos['abilities']]

class Pokemon2:
  def generation(self):
    pokemon=Pokemon()
    generation=int(input("Type generation (1 to 8) :"))
    data=extract_json(f"https://pokeapi.co/api/v2/generation/{generation}")
    pokemons_in_generation=[item['name'] for item in data['pokemon_species']]
    for poke in pokemons_in_generation:
        pokemon.set_nombre(poke)
        pokemon.info()

  def shape(self):
    pokemon=Pokemon()
    
    response = requests.get("https://pokeapi.co/api/v2/pokemon-shape/")
    data = response.json()
    shape = [item['name'] for item in data ['results']]  
    print("You can select from:\n", shape)
    
    shape=input("Type shape :").lower()
    url: str = "https://pokeapi.co/api/v2/pokemon-shape/" + shape
    
    data=extract_json(url)
     
    pokemons_in_shape=[item['name'] for item in data['pokemon_species']]
    for poke in pokemons_in_shape:
        pokemon.set_nombre(poke)
        pokemon.info()
      
  def ability(self):
    pokemon=Pokemon()
    
    response = requests.get("https://pokeapi.co/api/v2/ability/")
    data = response.json()
    ability = [item['name'] for item in data ['results']]  
    print("You can select from:\n", ability)
    
    ability=input("Type ability :").lower()
    url: str = "https://pokeapi.co/api/v2/ability/" + ability
    
    data=extract_json(url)
     
    pokemons_in_ability = [item['pokemon']['name'] for item in data['pokemon']]
    for poke in pokemons_in_ability:
        pokemon.set_nombre(poke)
        pokemon.info()

  def habitat(self):
    pokemon=Pokemon()
    
    response = requests.get("https://pokeapi.co/api/v2/pokemon-habitat/")
    data = response.json()
    habitat = [item['name'] for item in data ['results']]  
    print("You can select from:\n", habitat)
    
    habitat=input("Type shape :").lower()
    url: str = "https://pokeapi.co/api/v2/pokemon-habitat/" + habitat
    
    data=extract_json(url)
     
    pokemons_in_habitat=[item['name'] for item in data['pokemon_species']]
    for poke in pokemons_in_habitat:
        pokemon.set_nombre(poke)
        pokemon.info()

  def type(self):
    pokemon=Pokemon()
    
    response = requests.get("https://pokeapi.co/api/v2/type/")
    data = response.json()
    type = [item['name'] for item in data ['results']]  
    print("You can select from:\n", type)
    
    type=input("Type shape :").lower()
    url: str = "https://pokeapi.co/api/v2/type/" + type
    
    data=extract_json(url)
     
    pokemons_in_type=[item['pokemon']['name'] for item in data['pokemon']]
    for poke in pokemons_in_type:
        pokemon.set_nombre(poke)
        pokemon.info()
      

def inicio():
  
  run = Pokemon2()
  
  choice = input(
    "Select how you want to sort the pokemon (generation, shape, ability, habitat, type): "
  )
  if choice == "generation":
    run.generation()
  elif choice == "shape":
    run.shape()
  elif choice == "ability":
    run.ability()
  elif choice == "habitat":
    run.habitat()
  elif choice == "type":
    run.type()
  else: print ("Incorrect command")
inicio()
