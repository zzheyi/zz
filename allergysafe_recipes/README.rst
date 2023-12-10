===================
allergysafe_recipes
===================


.. image:: https://img.shields.io/pypi/v/recipes_search.svg
        :target: https://pypi.python.org/pypi/recipes_search

.. image:: https://img.shields.io/travis/zzheyi/recipes_search.svg
        :target: https://travis-ci.com/zzheyi/recipes_search

.. image:: https://readthedocs.org/projects/recipes-search/badge/?version=latest
        :target: https://recipes-search.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

Introduction
--------

The Allergy-Safe Recipe Explorer is a Python package designed to facilitate easy access to recipes and nutritional information, specifically catering to individuals with food allergies. This package will utilize the Spoonacular API to provide users with recipes that are safe for their specific dietary needs, offering advanced filtering, nutritional breakdowns, cost estimations, and more.



Features
--------

- Search for allergen-friendly recipes with customizable ingredient filters.
- Create meal plans that cater to specific dietary needs and preferences.
- Obtain detailed nutritional profiles for recipes to support health-conscious meal planning.
- Access price breakdowns for recipes, aiding in economical meal preparation.
- Retrieve step-by-step instructions for cooking, making it easy to follow along.
- Conduct ingredient-based recipe searches to find the perfect meal with what's on hand.

Installation
--------

Install `allergysafe_recipes` using pip:

.. code-block:: bash

    pip install allergysafe_recipes

Usage
-----

Each module within `allergysafe_recipes` serves a different functionality. To get start, you will need to register for an account at "https://spoonacular.com/food-api" to get your API key. Then here's how to use each function of the package:

Recipes Search
--------------

Search for recipes by query. Optionally exclude certain ingredients.

.. code-block:: python

    from allergysafe_recipes.recipes_search import search_recipes
    api_key = 'your_api_key'  # Replace with your Spoonacular API key
    query = 'gluten-free pizza'
    results = search_recipes(api_key, query)
    print(results)

Meal Planning
-------------

Generate a meal plan for a day or a week with specified caloric intake and dietary preferences.

.. code-block:: python

    from allergysafe_recipes.meal_planning import MealPlannerAPI
    planner = MealPlannerAPI(api_key)
    user_info = {
        "username": "user1",
        "firstName": "John",
        "lastName": "Doe",
        "email": "123456@example.com"
    }
    planner.connect_user(user_info)
    meal_plan = planner.generate_meal_plan('day', 2000, 'gluten free')
    print(meal_plan)

Nutrition
---------

Get nutritional information for a specific recipe by ID.

.. code-block:: python

    from allergysafe_recipes.nutrition import get_recipe_nutrition
    nutrition = get_recipe_nutrition(api_key, recipe_id=654959)
    print(nutrition)

Pricing
-------

Retrieve a breakdown of the cost of ingredients for a recipe.

.. code-block:: python

    from allergysafe_recipes.pricing import get_recipe_price_breakdown
    price_breakdown = get_recipe_price_breakdown(api_key, recipe_id=1003464)
    print(price_breakdown)

Instructions
------------

Get step-by-step cooking instructions for a given recipe.

.. code-block:: python

    from allergysafe_recipes.instructions import get_recipe_instructions
    instructions = get_recipe_instructions(api_key, recipe_id=715538)
    print(instructions)

Search by Ingredients
---------------------

Find recipes that utilize as many of the given ingredients as possible.

.. code-block:: python

    from allergysafe_recipes.search_by_ingredients import find_recipes_by_ingredients
    ingredients = 'apples, flour, sugar'
    recipes = find_recipes_by_ingredients(api_key, ingredients)
    print(recipes)

Running Tests
-------

To run tests, navigate to the `tests` directory and run the test files:

.. code-block:: bash

    python -m unittest discover tests

Ensure that you have set your Spoonacular API key in the test scripts or as an environment variable.

Contributing
-------

Contributions are welcome. Please follow the contributing guidelines detailed in `CONTRIBUTING.rst`.

License
-------

This project is licensed under the MIT License. See `LICENSE` for more details.

Contact
-------

If you have any questions or feedback, contact the package maintainer at zz3155@columbia.edu.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
