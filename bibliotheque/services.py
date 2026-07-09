import requests

def recuperer_infos_isbn(isbn):
    url = "https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "format": "json",
        "jscmd": "data"
    }
    response = requests.get(url, params=params)
    data = response.json()

    cle = f"ISBN:{isbn}"
    if cle not in data:
        return None

    livre_data = data[cle]

    return {
        "titre": livre_data.get("title", ""),
        "auteur": livre_data.get("authors", [{}])[0].get("name", "Auteur inconnu"),
        "couverture_url": livre_data.get("cover", {}).get("medium", ""),
    }