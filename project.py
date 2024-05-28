import requests

def main():
    find_by_ingredients = "https://api.spoonacular.com/recipes/findByIngredients"
    api_key = 'your_api_here'
    ingredients = get_ingredients()
    response = get_recipes(api_key, find_by_ingredients, ingredients)
    recipes = response.json() if response.status_code == 200 else []
    choice = get_choice() - 1
    title = get_title(recipes, choice)
    get_info(api_key, title, recipes, choice)

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

def get_title(recipes, choice):
    if 0 <= choice < len(recipes):
        id = recipes[choice]['id']
        return id
    else:
        print(f"Error: Invalid recipe choice")
        return None

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

if __name__ == "__main__":
    main()
