import requests


# function to fetch animal data
def fetch_data(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        'X-Api-Key': 'PkENBQCJu7xhonKfJq1flg==lYMSRIROvX6QU1Gv'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:  # check if data is not empty
            return data
        else:
            print(f"No data found for '{animal_name}'")
            return []
    else:
        print(f"Error: Received {response.status_code} from the API")
        return []


# main function to interact with the user
def main():
    animal_name = input("Enter the name of an animal: ")
    animals = fetch_data(animal_name)

    if animals:
        print(f"Data for {animal_name}:")
        for animal in animals:
            print(f"Name: {animal.get('name', 'N/A')}")
            characteristics = animal.get('characteristics', {})
            print(f"Type: {characteristics.get('type', 'Unknown')}")
            print(f"Diet: {characteristics.get('diet', 'Unknown')}")
            print(f"Locations: {', '.join(animal.get('locations', ['Unknown']))}")
            print()
    else:
        print(f"No information found for '{animal_name}'.")


if __name__ == "__main__":
    main()