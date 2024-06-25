import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten aus der JSON-Datei lesen
animals_data = load_data('animals_data.json') 

# HTML-Code für die Tierkarten generieren (mit angepasster Einrückung)
html_output = ""
for animal in animals_data:
    html_output += '        <li class="cards__item">\n'  # 8 Leerzeichen Einrückung
    if "name" in animal:
        html_output += f'            <h2>{animal["name"]}</h2>\n'  # 12 Leerzeichen Einrückung
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        html_output += f'            <p>Diet: {animal["characteristics"]["diet"]}</p>\n'
    if "locations" in animal and animal["locations"]:
        html_output += f'            <p>Location: {animal["locations"][0]}</p>\n'
    if "type" in animal:
        html_output += f'            <p>Type: {animal["type"]}</p>\n'
    elif "characteristics" in animal and "type" in animal["characteristics"]:
        html_output += f'            <p>Type: {animal["characteristics"]["type"]}</p>\n'
    html_output += '        </li>\n'  # 8 Leerzeichen Einrückung

# animals_template.html einlesen und Platzhalter ersetzen
with open('animals_template.html', 'r') as f:
    html_template = f.read()
html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', html_output)

# Neuen HTML-Code in die Datei animals.html schreiben
with open('animals.html', 'w') as f:
    f.write(html_output)
