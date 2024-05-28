## Explaining the Project

## CS50:

### This was my final project for **CS50’s Introduction to Programming with Python course.**

# **Foodify**

### This program works with **spoonacular api** to give the user recipes based on the ingredients they wish to include in the recipe.

## Youtube Demonstration:

### You can find the demo for this program at this [link](https://youtu.be/n2Cva07zaxc).

## Step_01

### When you first run the program, it prompts the user for ingredients that the user would like the recipe to include.

```python
def get_ingredients():
    ingredients = []
    print()
    while True:
        user_input = input("Add Ingredient (or type 'done'): ")
        if user_input.lower().strip() == 'done':
            print()
            break
        ingredients.append(user_input)
    return ingredients
```

## Step_02

### When the user inputs "done", the program breaks out of the get_ingredients loop and the second step starts which allows the program to connect to the spoonacular api and return a list of five recipes with their names and ingredients that the user needs, along with the ones they entered.

```python
def get_recipes(api_key, find_by_ingredients, ingredients):
    url = find_by_ingredients
    params = {
        'apiKey': api_key,
        'ingredients': ','.join(ingredients),
        'instructionsRequired': "true",
        'number': 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        recipes = response.json()
        for recipe in recipes:
            print(f"Title: {recipe['title']}")
            print(f"Used Ingredients: {', '.join([ingredient['name'] for ingredient in recipe['usedIngredients']])}")
            print(f"Missed Ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
            print()
    else:
        print(f"Error: {response.status_code}")

    return response
```

### The **spoonacular API** allows us to search for world famous recipes based on ingredients and returns the best results.

## Step_03:

### This function allows the user to choose between a list of five recipes and get instructions on how to cook any one of their choosing.

```python
def get_choice():
    while True:
        try:
            n = int(input("Choose a Recipe (1 - 5): "))
            print()

            if 1 <= n <= 5:
                return n

            else:
                print("Invalid Choice")

        except ValueError:
            print("Invalid Value. Please Enter a value between 1 and 5")
```

## Step_04:

### This function's sole purpose it to return the id of the recipe that the user has chosen.

```python
def get_title(recipes, choice):
    if 0 <= choice < len(recipes):
        id = recipes[choice]['id']
        return id
    else:
        print(f"Error: Invalid recipe choice")
        return None
```

## Step_05:

### The get_recipe_information function allows us to import the instructions for all the recipes that are being returned to the user.

```python
def get_recipe_information(api_key, recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        'apiKey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching recipe information: {response.status_code}")
        return None
```

## Step_06:

### This functions uses the title and id returned by the functions before itself to once again use spoonacular api to get instructions for the desired recipe. It connects to the api using another function get_recipe_information which connects to the api and returns the json file containing all the desired information.

```python
def get_info(api_key, title, recipes, choice):
    if title is None:
        print("No valid recipe selected.")
        return

    recipe_info = get_recipe_information(api_key, title)

    print(f"Title: {recipes[choice]['title']}")
    print()

    if recipe_info:
        instructions =  recipe_info.get('instructions', 'No instructions available')
        instructions = instructions.replace("<ol>", "").replace("<li>", "").replace("</li>", "").replace("</ol>", "")
        print(f"Instructions: {instructions}")
    print()
```

## Libraries Used:

### This program works solely on one library, namely, [requests](https://pypi.org/project/requests/)
