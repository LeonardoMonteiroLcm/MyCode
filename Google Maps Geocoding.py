import json
import requests # pip install requests

# Sua chave da API do Google Maps
API_KEY = "AIzaSyCsKSZ9FZ5KBCWMvJJkzuGrUyZx3xyHL7w"
GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# Carrega os endereços do arquivo JSON de entrada
with open("list_of_real_usa_addresses.json", "r", encoding="utf-8") as f:
    addresses = json.load(f)

# Lista para armazenar os endereços com latitude e longitude
geocoded_addresses = []

for entry in addresses:
    full_address = f"{entry['address']}, {entry['city']}, {entry['state']}, {entry['zip']}, USA"
    params = {"address": full_address, "key": API_KEY}
    response = requests.get(GEOCODING_URL, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        entry["latitude"] = location["lat"]
        entry["longitude"] = location["lng"]
    else:
        entry["latitude"] = None
        entry["longitude"] = None
    
    geocoded_addresses.append(entry)

# Salva os dados no arquivo JSON de saída
with open("list_of_real_usa_addresses_latlong.json", "w", encoding="utf-8") as f:
    json.dump(geocoded_addresses, f, indent=4, ensure_ascii=False)

print("Processo concluído! Dados salvos em list_of_real_usa_addresses_latlong.json.")