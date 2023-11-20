import requests
import mate
import matplotlib.pyplot as plt

url_api = "https://pokeapi.co/api/v2/pokemon/"
url_api_gene = "https://pokeapi.co/api/v2/generation/"
url_api_tipo = "https://pokeapi.co/api/v2/type/"


def busquedanombre():
    pokemon_name = input("Dime el nombre del pokemon: ")
    pokemon_data_url = url_api + pokemon_name
    return(pokemon_data_url)


def busquedanumero():
    pokemon_number = input("Dime el numero del pokemon: ")
    pokemon_data_url = url_api + pokemon_number
    return(pokemon_data_url)


def getdata(pokemon_data_url = ""):
    response = requests.get(pokemon_data_url)
    data = response.json()


    pokemon_data = {
        "name": "",
        "height": "",
        "abilities": "",
        "types": "",
        "weight": ""
    }

    pokemon_data["name"] = data["name"]
    pokemon_data["height"] = data["height"]
    pokemon_data["abilities"] = len(data["abilities"])
    pokemon_data["types"] = data["types"]
    pokemon_data["weight"] = data["weight"]

    return pokemon_data

def escribirarchivo(datos):

    fo.write(str(datos)+"\n")

    
#Definiciones del Amaury
def datosgeneracion(pokemon_data_url = ""):
    response = requests.get(pokemon_data_url)
    data = response.json()
    pokemon_data = {
        'pokemon_species': ""
    }
    pokemon_data['pokemon_species'] = data['pokemon_species']

    return pokemon_data

def distribuciontipos(pokemon_data_url = ""):
    response = requests.get(pokemon_data_url)
    data = response.json()
    pokemon_data_2 = {
        'pokemon': ""
    }
    pokemon_data_2['pokemon'] = data['pokemon']

    return pokemon_data_2


def generaciones():
    for i in range(1,10,1):
        j = str(i)
        pokemon_data_url = url_api_gene + j
    return(pokemon_data_url)

#Metodos del Adonai

def graficageneracion(y = list()):
    Gens = ["Gen 1","Gen 2","Gen 3","Gen 4","Gen 5","Gen 6","Gen 7","Gen 8","Gen 9"]
    plt.pie(y,labels = Gens)





print("Bienvenido a la Api de Pokemon.")
fo = open("Busquedas.txt","a")

def proceso():
    while True:
        try:
            busq=int(input("Si desea buscar pokemon por nombre presione 1.\nSi desea buscar por numero, presione 2.\nPara saber cuantos Pokemon hay por generación, presione 3.\nPara ver la distribución de tipos, presione 4.\nSi desea salir, pulse cualquier otro numero."))
        except ValueError as e1:
            print("\nDebes capturar un numero y que sea entero.\n")
            busq=int(input("Si desea buscar pokemon por nombre presione 1.\nSi desea buscar por numero, presione 2.\nPara saber cuantos Pokemon hay por generación, presione 3.\nPara ver la distribución de tipos, presione 4.\nSi desea salir, pulse cualquier otro numero."))
        finally:
            if busq == 1:
                data = getdata(busquedanombre())

                pokemon_type = [types["type"]["name"]for types in data["types"]]
                print(data)
                print(", ".join(pokemon_type))
                fo.write("Resultado de busqueda por nombre\n")
                escribirarchivo(data)

            elif busq == 2:
                data = getdata(busquedanumero())
                pokemon_type = [types["type"]["name"]for types in data["types"]]
                print(data)
                print(", ".join(pokemon_type))
                fo.write("Resultado de busqueda por numero\n")
                escribirarchivo(data)                
            
            elif busq == 3:
                Numero_pokemones_por_genera = list()
                for i in range(1,10,1):
                    j = str(i)
                    pokemon_data_url = (url_api_gene + j)
                    data = datosgeneracion(pokemon_data_url)
                    Numero_pokemones_por_genera.append(len(data['pokemon_species']))
                print (Numero_pokemones_por_genera)
                #graficageneracion(Numero_pokemones_por_genera)
                fo.write("Busqueda de pokemon por generación\n")
                escribirarchivo(Numero_pokemones_por_genera)
                mate.promedio(Numero_pokemones_por_genera)
            
            elif busq == 4:
                for s in range(1,10,1):
                    r = str(s)
                    pokemon_data_url = (url_api_gene + r)
                    data = datosgeneracion(pokemon_data_url)
                    tipos_generacion = list()
                    for i in range (1,19,1):
                        j = str(i)
                        pokemon_data_url_2 = (url_api_tipo + j)
                        data_2 = distribuciontipos(pokemon_data_url_2)
                        cont_typo = int(0)
                        cont_1 = int(0)
                        cont_2 = int(0)
                        info_1 = data['pokemon_species']
                        info_2 = data_2['pokemon']
                        for elen in info_2:
                            cont_2 = int(0)
                            filtro_1 = info_2[cont_1]
                            filtro_2 = filtro_1['pokemon']
                            filtro_3 = filtro_2['name']
                            for elen in info_1:
                                filtro_4 = info_1[cont_2]
                                filtro_5 = filtro_4['name']
                                if filtro_3 == filtro_5:
                                    cont_typo +=1
                                    cont_2 +=1
                                else:
                                    cont_2 +=1
                            cont_1 +=1
                        tipos_generacion.append(cont_typo)
                    print("Distribucion de la", s, "generacion", tipos_generacion)
                    mate.promedio(Numero_pokemones_por_genera)




            else:
                print("Hasta luego.")
                fo.close()
                break




