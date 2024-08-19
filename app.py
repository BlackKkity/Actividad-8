import requests

def get_data_from_swapi(endpoint):
    url = f"https://swapi.dev/api/{endpoint}/"
    response = requests.get(url)
    return response.json()

def get_planets_with_arid_climate():
    planets = get_data_from_swapi("planets")
    arid_planets = [planet for planet in planets['results'] if 'arid' in planet['climate'].lower()]
    return len(arid_planets)

def get_wookie_count():
    characters = get_data_from_swapi("people")
    wookie_count = sum(1 for char in characters['results'] if char['name'] == 'Chewbacca')
    return wookie_count

def get_smallest_starship_name_in_first_movie():
    films = get_data_from_swapi("films")
    first_film = films['results'][0]
    starships = [requests.get(starship_url).json() for starship_url in first_film['starships']]
    smallest_starship = min(starships, key=lambda x: x['length'])
    return smallest_starship['name']

def main():
    arid_climate_count = get_planets_with_arid_climate()
    wookie_count = get_wookie_count()
    smallest_starship_name = get_smallest_starship_name_in_first_movie()

    result = (
        f"A) Número de películas con planetas cuyo clima es árido: {arid_climate_count}\n"
        f"B) Número de Wookies en toda la saga: {wookie_count}\n"
        f"C) Nombre de la aeronave más pequeña en la primera película: {smallest_starship_name}\n"
    )

    with open("swapi_results.txt", "w") as file:
        file.write(result)

if __name__ == "__main__":
    main()
