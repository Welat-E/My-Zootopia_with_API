import requests

API_KEY = "h25Mlufhop/YEdyh5TV0ag==mmGDx4l1vMG0ohtp"
API_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(f'{API_URL}{animal_name}', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return [{"name": animal_name, "error": "This animal doesn't exist."}]
    else:
        return [{"name": animal_name, "error": f"Failed to retrieve data: {response.status_code}"}]
