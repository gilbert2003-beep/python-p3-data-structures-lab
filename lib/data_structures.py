spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] >= 7]
    spiciest_foods = sorted(spiciest_foods, key=lambda x: x["heat_level"], reverse=True)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_info = " | ".join([food["name"], food["cuisine"], f"Heat Level: {food['heat_level']}"])
        food_emoji = "🌶" * food["heat_level"]  # Repeat the chili emoji according to the heat level
        print(f"{food_info} {food_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # or "No spicy food with this cuisine found."

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    average_heat_level = sum(heat_levels) / len(heat_levels)
    average_heat_level = round(average_heat_level, 2)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()  # Create a copy of the original list
    new_food = {
        "name": spicy_food["name"],
        "cuisine": spicy_food["cuisine"],
        "heat_level": spicy_food["heat_level"],
    }
    new_spicy_foods.append(new_food)
    return new_spicy_foods

# Example usage:
print("Names of spicy foods:", get_names(spicy_foods))
print("Spiciest foods:", get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print("Spicy food with cuisine 'Thai':", get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print("Average heat level:", get_average_heat_level(spicy_foods))

new_spicy_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 8,
}
spicy_foods_with_new = create_spicy_food(spicy_foods, new_spicy_food)
print_spicy_foods(spicy_foods_with_new)
