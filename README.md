# My Zootopia API Project

My Zootopia API Project is a web application that utilizes an API to provide information about various animals from the Zootopia universe. This project includes features for displaying animal data and generating dynamic web pages.

## Features

- **View Animals**: Display a list of animals with details from the Zootopia API.
- **Dynamic Web Pages**: Generate HTML pages dynamically based on animal data.
- **Data Fetching**: Use a Python script to fetch and process animal data.

## Installation

### Prerequisites

- Python 3.x

### Setting Up the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Welat-E/My-Zootopia_with_API.git
   cd My-Zootopia_with_API
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Web Application**: Run the `animals_web_generator.py` script to generate and serve the web pages.
- **Animal Data**: The application utilizes `animals_data.json` for displaying animal information.

## File Structure

- `animals.html`: Template for displaying animal data.
- `animals_data.json`: JSON file containing data about animals.
- `animals_template.html`: HTML template for generating animal pages.
- `animals_web_generator.py`: Python script for generating web pages.
- `data_fetcher.py`: Script for fetching animal data from the API.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
