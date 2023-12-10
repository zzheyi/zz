import requests

BASE_URL = 'https://api.spoonacular.com'

def format_search_results(search_results):
    formatted_results = "Search Results:\n"
    for recipe in search_results['results']:
        formatted_results += f"Title: {recipe['title']}\n" \
                             f"ID: {recipe['id']}\n" \
                             f"Image: {recipe['image']}\n\n"
    return formatted_results

def search_recipes(api_key, query, exclude_ingredients="", **kwargs):
    params = {
        'apiKey': api_key,
        'query': query,
        'excludeIngredients': exclude_ingredients,
        **kwargs
    }

    try:
        response = requests.get(f"{BASE_URL}/recipes/complexSearch", params=params)
        if response.ok:
            search_results = response.json()
            return format_search_results(search_results)
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
