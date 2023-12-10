import requests

class MealPlannerAPI:
    BASE_URL = 'https://api.spoonacular.com'

    def __init__(self, api_key):
        self.api_key = api_key
        self.username = None
        self.hash = None

    def connect_user(self, user_info):
        """
        Connect an app's user to a Spoonacular user.

        :param user_info: A dictionary containing user's information (username, firstName, lastName, email).
        :return: A JSON response containing the Spoonacular username, password, and hash.
        """
        endpoint = "/users/connect"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            self.BASE_URL + endpoint,
            json=user_info,
            headers=headers,
            params={'apiKey': self.api_key}
        )

        if response.ok:
            user_data = response.json()
            self.username = user_data.get('username')
            self.hash = user_data.get('hash')
            return user_data
        else:
            response.raise_for_status()

    def generate_meal_plan(self, time_frame, target_calories, diet='', exclude=''):
        """
        Generate a meal plan with specified parameters.

        :param time_frame: Time frame for the meal plan ('day' or 'week').
        :param target_calories: Caloric target for one day.
        :param diet: Specific diet to adhere to (optional).
        :param exclude: Ingredients to exclude (optional).
        :return: A JSON response containing the meal plan.
        """
        if not self.username or not self.hash:
            raise ValueError("User not connected. Please connect a user first.")

        endpoint = f"/mealplanner/generate"
        params = {
            'apiKey': self.api_key,
            'timeFrame': time_frame,
            'targetCalories': target_calories,
            'diet': diet,
            'exclude': exclude,
            'username': self.username,
            'hash': self.hash
        }

        response = requests.get(self.BASE_URL + endpoint, params=params)

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

def display_meal_plan(meal_plan):
    """
    Display the meal plan in a user-friendly format.

    :param meal_plan: The meal plan data.
    """
    print("Your Meal Plan for the Day:")
    print("============================")
    for meal in meal_plan['meals']:
        print(f"Title: {meal['title']}")
        print(f" - Ready in: {meal['readyInMinutes']} minutes")
        print(f" - Servings: {meal['servings']}")
        print(f" - Recipe URL: {meal['sourceUrl']}\n")

    print("Nutritional Summary for the Day:")
    print("================================")
    nutrients = meal_plan['nutrients']
    print(f"Calories: {nutrients['calories']:.2f}")
    print(f"Protein: {nutrients['protein']:.2f} g")
    print(f"Fat: {nutrients['fat']:.2f} g")
    print(f"Carbohydrates: {nutrients['carbohydrates']:.2f} g")