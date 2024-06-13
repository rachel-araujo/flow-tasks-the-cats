import requests
from prefect import flow, task

# Obter imagem aleatória de gato
@task(retries=3, retry_delay_seconds=10)
def fetch_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_url = response.json()[0]['url']
        return image_url
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Failed to fetch cat image: {error}")

# Obter fato aleatório sobre gatos
@task(retries=3, retry_delay_seconds=10)
def fetch_random_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        fact = response.json()['fact']
        return fact
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Failed to fetch cat fact: {error}")

# Imprimir resultados
@task
def display_results(image_url, fact):
    print(f"Here is a cat image URL: {image_url}")
    print(f"Did you know? {fact}")

# Definir fluxo principal
@flow(name="Cat Information Flow")
def main_flow():
    image_url = fetch_random_cat_image()
    cat_fact = fetch_random_cat_fact()
    display_results(image_url, cat_fact)

# Executar fluxo
if __name__ == "__main__":
    main_flow()