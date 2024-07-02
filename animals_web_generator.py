import json

def load_data(file_path):
    """loads animal data from a json file"""
    with open(file_path, "r") as file:
        return json.load(file)
    

def serialize_animal_data(animals_data):
    """serializes animal data, currently returns it unchanged"""
    return animals_data  # placeholder for future serialization logic


def generate_html(animals_data):
    """generates HTML for animal cards"""
    html = ""
    for animal in animals_data:
        html += '<li class="cards__item">'
        html += f'<h2>{animal.get("name", "Unknown Animal")}</h2>'
        html += '<p class="cards__text">'
        characteristics = animal.get("characteristics", {})
        html += f'<strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br>'
        html += f'<strong>Location:</strong> {animal.get("locations", ["Unknown"])[0]}<br>'
        animal_type = animal.get("type") or characteristics.get("type", "Unknown")
        html += f'<strong>Type:</strong> {animal_type}<br>'
        html += '</p></li>'
    return html


def write_html(html_content):
    """inserts animal HTML into a template"""
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()
    html_output = template.replace('__REPLACE_ANIMALS_INFO__', html_content)
    with open('animals.html', 'w') as output_file:
        output_file.write(html_output)


def main():
    animals_data = load_data('animals_data.json')
    serialized_data = serialize_animal_data(animals_data) #serialization added
    html_content = generate_html(serialized_data)
    write_html(html_content)


if __name__ == "__main__":
    main()
