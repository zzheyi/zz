import unittest
from unittest.mock import patch
from recipes_search.meal_planning import MealPlannerAPI

class TestMealPlanning(unittest.TestCase):

    @patch('recipes_search.meal_planning.requests.get')
    def test_generate_meal_plan_successful(self, mock_get):
        # Arrange: Set up the mock response data
        mock_response_data = {
            'meals': [{'id': 123, 'title': 'Test Meal', 'readyInMinutes': 30, 'servings': 2}],
            'nutrients': {'calories': 2000, 'protein': 100, 'fat': 50, 'carbohydrates': 300}
        }
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = mock_response_data

        # Act: Call the function
        api_key = 'fake_api_key'
        meal_planner = MealPlannerAPI(api_key)
        meal_planner.username = 'test_user'
        meal_planner.hash = 'test_hash'
        response = meal_planner.generate_meal_plan('day', 2000)

        # Assert: Check if the response matches the expected outcome
        self.assertEqual(response, mock_response_data)

    @patch('recipes_search.meal_planning.requests.get')
    def test_generate_meal_plan_failure(self, mock_get):
        # Arrange: Mock a failed API call
        mock_get.return_value.ok = False
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = Exception('API Error')

        # Act and Assert: Ensure an exception is raised for a failed API call
        api_key = 'fake_api_key'
        meal_planner = MealPlannerAPI(api_key)
        meal_planner.username = 'test_user'
        meal_planner.hash = 'test_hash'

        with self.assertRaises(Exception) as context:
            meal_planner.generate_meal_plan('day', 2000)
        
        self.assertTrue('API Error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

