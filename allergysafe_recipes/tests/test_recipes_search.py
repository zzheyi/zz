#!/usr/bin/env python

"""Tests for `recipes_search` package."""


import unittest

# tests/test_recipes_search.py

import unittest
from unittest.mock import patch
from recipes_search.recipes_search import search_recipes

class TestRecipesSearch(unittest.TestCase):

    @patch('recipes_search.recipes_search.requests.get')
    def test_search_recipes(self, mock_get):
        # Mock the response from the requests.get call within search_recipes
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {
            "results": [
                {"title": "Chocolate Cake", "id": 12345, "image": "chocolate-cake.jpg"},
                {"title": "Carrot Cake", "id": 54321, "image": "carrot-cake.jpg"}
            ],
            "totalResults": 2
        }

        # Call the search_recipes function with a test query and API key
        api_key = 'test_api_key'
        query = 'cake'
        result = search_recipes(api_key, query)

        # Assertions to check if the results are as expected
        self.assertIn("Chocolate Cake", result)
        self.assertIn("Carrot Cake", result)
        self.assertIn("12345", result)
        self.assertIn("54321", result)

if __name__ == '__main__':
    unittest.main()

