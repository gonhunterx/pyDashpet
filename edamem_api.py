import requests


def check_food(food_name, app_id, app_key):
    base_url = "https://api.edamam.com/api/food-database/v2/parser"

    params = {
        "ingr": food_name,
        "app_id": app_id,
        "app_key": app_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("parsed"):
            return True  # Food is recognized
        else:
            return False  # Food is not recognized
    else:
        return None  # API request error
