import requests

def get_recipe_price_breakdown(api_key, recipe_id):
    """
    Get the price breakdown of a recipe by its ID.

    :param api_key: The API key for Spoonacular API.
    :param recipe_id: The ID of the recipe for which to get the price breakdown.
    :return: A formatted string containing the price breakdown.
    """
    response = requests.get(f"https://api.spoonacular.com/recipes/{recipe_id}/priceBreakdownWidget.json",
                            params={'apiKey': api_key})

    if response.ok:
        price_data = response.json()
        return format_price_breakdown(price_data)
    else:
        response.raise_for_status()

def format_price_breakdown(price_data):
    """
    Format the price breakdown data for better readability.

    :param price_data: The JSON data containing the price breakdown.
    :return: A formatted string of the price breakdown.
    """
    formatted_price_breakdown = "Price Breakdown:\n"
    for ingredient in price_data['ingredients']:
        name = ingredient['name']
        price = ingredient['price']
        amount_metric = ingredient['amount']['metric']
        amount_us = ingredient['amount']['us']
        formatted_price_breakdown += f"- {name} ({amount_metric['value']} {amount_metric['unit']} / {amount_us['value']} {amount_us['unit']}): ${price:.2f}\n"

    total_cost = price_data['totalCost']
    cost_per_serving = price_data['totalCostPerServing']
    formatted_price_breakdown += f"\nTotal Cost: ${total_cost:.2f}\nCost Per Serving: ${cost_per_serving:.2f}"

    return formatted_price_breakdown

# Example usage
api_key = 'b76bf0d048624914b6be0b8c3c3455f1'  # Replace with your actual API key
recipe_id = 638245  # Replace with a valid recipe ID
print(get_recipe_price_breakdown(api_key, recipe_id))