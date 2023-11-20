import requests
url_api = "https://pokeapi.co/api/v2/pokemon/"
url_api_gene = "https://pokeapi.co/api/v2/generation/"

def datosgeneracion(pokemon_data_url = ""):
    response = requests.get(pokemon_data_url)
    data = response.json()
    pokemon_data = {
        'pokemon_species': ""
    }
    pokemon_data['pokemon_species'] = data['pokemon_species']

    return pokemon_data


def generaciones():
    for i in range(1,10,1):
        j = str(i)
        pokemon_data_url = url_api_gene + j
    return(pokemon_data_url)

#Busqueda de datos 
Numero_pokemones_por_genera = list()
for i in range(1,10,1):
    j = str(i)
    pokemon_data_url = (url_api_gene + j)
    data = datosgeneracion(pokemon_data_url)
    Numero_pokemones_por_genera.append(len(data['pokemon_species']))
print (Numero_pokemones_por_genera)

