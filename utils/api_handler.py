import requests

def fetch_all_products():
    try:
        response = requests.get("https://dummyjson.com/products?limit=100", timeout=10)
        response.raise_for_status()
        return response.json().get("products", [])
    except Exception:
        return []
