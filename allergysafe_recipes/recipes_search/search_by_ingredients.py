import requests

def search_recipes_by_ingredients(api_key, ingredients, number=10, limitLicense=True, ranking=1, ignorePantry=True):
    """
    Search for recipes based on the ingredients provided.

    :param api_key: The API key for Spoonacular API.
    :param ingredients: A comma-separated string of ingredients that the recipes should contain.
    :param number: The maximum number of recipes to return (default is 10).
    :param limitLicense: Whether the recipes should have an open license for display (default is True).
    :param ranking: Whether to maximize used ingredients (1) or minimize missing ingredients (2).
    :param ignorePantry: Whether to ignore typical pantry items, such as water, salt, flour, etc. (default is True).
    :return: A list of recipes that use the given ingredients.
    """
    params = {
        'apiKey': api_key,
        'ingredients': ingredients,
        'number': number,
        'limitLicense': limitLicense,
        'ranking': ranking,
        'ignorePantry': ignorePantry
    }
    response = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=params)
    
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()