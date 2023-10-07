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

    my_list = [food["name"] for food in spicy_foods]
    return my_list


print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):

    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods


print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emoji = "🌶"
        heat_emojis = heat_emoji * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None


print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    # for food in spicy_foods:
    #     name = food["name"]
    #     cuisine = food["cuisine"]
    #     heat_level = food["heat_level"]
    #     heat_emoji = "🌶"
    #     heat_emojis = heat_emoji * heat_level

    #     if heat_level > 5:
    #         print(f"{name} ({cuisine}) | {heat_emojis}")

    # for food in spicy_foods:
    #     heat_level = food["heat_level"]

    #     if heat_level > 5:
    #         return print_spicy_foods(spicy_foods)
    #     else:
    #         return None

    spiciest_food = [
        food for food in spicy_foods if food.get("heat_level") > 5]
    print_spicy_foods(spiciest_food)


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):

    n = len(spicy_foods)
    print(n)

    heat = [food.get("heat_level") for food in spicy_foods]
    print(heat)
    x = sum(heat)
    print(x)
    print(x/n)
    return x / n


print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.extend([spicy_food])
    return spicy_foods


spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

new_spicy_food = create_spicy_food(spicy_foods, spicy_food)
print(new_spicy_food[3])
