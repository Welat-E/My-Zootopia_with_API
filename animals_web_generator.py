import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    print()
    if "name" in animal:
        print("Name:", animal["name"])
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print("Diet:", animal["characteristics"]["diet"])
    if "locations" in animal and animal["locations"]:
        print("Location:", animal["locations"][0])

    # Suche nach "type" im Haupteintrag, falls nicht vorhanden, dann in "characteristics"
    if "type" in animal:
        print("Type:", animal["type"])
    elif "characteristics" in animal and "type" in animal["characteristics"]:
        print("Type:", animal["characteristics"]["type"])
