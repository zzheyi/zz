import requests

def get_recipe_nutrition(api_key, recipe_id):
    """
    Fetch nutritional information for a specific recipe by ID.

    :param api_key: The API key for Spoonacular API.
    :param recipe_id: The ID of the recipe to retrieve nutrition information for.
    :return: Formatted string containing the nutritional information of the recipe.
    """
    BASE_URL = 'https://api.spoonacular.com'
    endpoint = f"{BASE_URL}/recipes/{recipe_id}/nutritionWidget.json"
    params = {'apiKey': api_key}

    try:
        response = requests.get(endpoint, params=params)
        if response.ok:
            nutrition_info = response.json()
            return format_nutritional_info(nutrition_info)
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Error occurred: {req_err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def format_nutritional_info(nutrition_info):
    """
    Format the nutritional information for display.

    :param nutrition_info: JSON response containing the nutritional information.
    :return: Formatted string of nutritional information.
    """
    formatted_info = ""
    if 'calories' in nutrition_info:
        formatted_info += f"Calories: {nutrition_info['calories']}\n"
    if 'carbs' in nutrition_info:
        formatted_info += f"Carbohydrates: {nutrition_info['carbs']}\n"
    if 'fat' in nutrition_info:
        formatted_info += f"Fat: {nutrition_info['fat']}\n"
    if 'protein' in nutrition_info:
        formatted_info += f"Protein: {nutrition_info['protein']}\n"

    formatted_info += "\nDetailed Nutrients:\n"
    if 'nutrients' in nutrition_info:
        for nutrient in nutrition_info['nutrients']:
            name = nutrient['name']
            amount = nutrient['amount']
            unit = nutrient['unit']
            percent_of_daily_needs = nutrient['percentOfDailyNeeds']
            formatted_info += f"{name}: {amount}{unit} ({percent_of_daily_needs}% of daily needs)\n"

    return formatted_info