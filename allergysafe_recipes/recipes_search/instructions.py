import requests

def get_recipe_instructions(api_key, recipe_id):
    """
    Get detailed instructions for a recipe by its ID.

    :param api_key: The API key for Spoonacular API.
    :param recipe_id: The unique ID of the recipe.
    :return: Formatted string containing step-by-step instructions.
    """
    response = requests.get(f"https://api.spoonacular.com/recipes/{recipe_id}/information",
                            params={'apiKey': api_key, 'includeNutrition': False})
    
    if response.ok:
        recipe_data = response.json()
        instructions = recipe_data.get('instructions', 'No instructions available.')
        return format_instructions(instructions)
    else:
        response.raise_for_status()

def format_instructions(instructions):
    """
    Format the instructions to make them more readable.

    :param instructions: A string containing the cooking instructions.
    :return: A formatted string of the instructions.
    """
    if not instructions:
        return "No instructions provided."
    
    formatted_instructions = "Instructions:\n"
    steps = instructions.split('.')
    for idx, step in enumerate(steps, 1):
        formatted_instructions += f"{idx}. {step.strip()}.\n" if step.strip() else ""
    
    return formatted_instructions