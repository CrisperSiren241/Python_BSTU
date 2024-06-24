import requests

def get_breed_info(breed_name):
    url = "https://api.thedogapi.com/v1/breeds/search"
    query_params = {"q": breed_name}

    response = requests.get(url, params=query_params)
    
    if response.status_code == 200:
        breed_data = response.json()
        if breed_data: 
            return breed_data[0] 
        else:
            return None
    else:
        print("Error:", response.status_code)
        return None

def display_breed_info(breed_info):
    if breed_info:
        print("\nBreed Name:", breed_info.get("name"))
        print("Breed Group:", breed_info.get("breed_group"))
        print("Life Span:", breed_info.get("life_span"))
        print("Temperament:", breed_info.get("temperament"))
    else:
        print("Breed not found.")



breed_info = get_breed_info("Affenpinscher")
display_breed_info(breed_info)