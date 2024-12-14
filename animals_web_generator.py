import json

def load_animal_data(filename):
    """Loads animal data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def generate_animal_cards(data):
    """Generates HTML card snippets for each animal."""
    cards_html = ""
    for animal in data:
        try:
            cards_html += f"""
            <li class="cards__item">
                <div class="card__title">{animal['name']}</div>
                <p class="card__text">
                    <strong>Type:</strong> {animal['characteristics'].get('type', 'Unknown')}<br>
                    <strong>Diet:</strong> {animal['characteristics']['diet']}<br>
                    <strong>Locations:</strong> {", ".join(animal['locations'])}
                </p>
            </li>
            """
        except KeyError as e:
            print(f"Error: Missing key {e} in animal data {animal}")
    return cards_html

def write_html(cards_html, output_file='animals.html', template_file='animals_template.html'):
    """Writes the final HTML file using the template and generated cards."""
    try:
        with open(template_file, 'r') as template:
            template_content = template.read()

        # Replace the placeholder with animal cards
        final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', cards_html)

        # Write the final HTML to the output file
        with open(output_file, 'w') as output:
            output.write(final_html)
        print(f"HTML file generated successfully: {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    # Load animal data from JSON
    data = load_animal_data('animals_data.json')

    # Generate animal cards
    animal_cards = generate_animal_cards(data)

    # Write the HTML file
    write_html(animal_cards)

if __name__ == "__main__":
    main()
