"""Restaurant rating lister."""

from random import *
filename = "scores.txt"
restaurant_ratings = {}

for line in open(filename):
    line = line.rstrip()
    restaurant = line.split(":")[0]
    rating = line.split(":")[1]
    restaurant_ratings[restaurant] = rating


def add_rating(restaurant_ratings = restaurant_ratings):
    """Asks for a restaurant and rating, then adds that to the dictionary."""

    restaurant_name = input("What restaurant do you want to rate? ")

    while True:
        restaurant_rating = input(f"How would you rate {restaurant_name}? ")
        try:
            restaurant_rating = int(restaurant_rating)
        except:
            print("Please pick an integer between 1 and 5.")
            continue
        if restaurant_rating < 1 or restaurant_rating > 5:
            print("Please pick an integer between 1 and 5.")
            continue
        else: break

    restaurant_ratings[restaurant_name] = restaurant_rating


def display_ratings(restaurant_ratings = restaurant_ratings):
    """Prints alphabetized list of ratings."""

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f"{restaurant} is rated at {rating}.")


def random_restaurant(restaurant_ratings = restaurant_ratings):
    """Prints a random restaurant and its rating and asks user to update it."""

    idx = randint(1, len(restaurant_ratings.keys()))
    restaurant_idx = {}

    count = 1
    for restaurant in restaurant_ratings:
        restaurant_idx[count] = restaurant
        count += 1

    restaurant = restaurant_idx[idx]
    rating = restaurant_ratings[restaurant]
    print(f"{restaurant} is rated at {rating}.")

    while True:
        restaurant_rating = input(f"How would you rate {restaurant}? ")
        try:
            restaurant_rating = int(restaurant_rating)
        except:
            print("Please pick an integer between 1 and 5.")
            continue
        if restaurant_rating < 1 or restaurant_rating > 5:
            print("Please pick an integer between 1 and 5.")
            continue
        else: break

    restaurant_ratings[restaurant] = restaurant_rating


while True:
    task = input("Would you like to 'rate', 'view ratings', 'get random' or 'quit'? ")
    if task == 'quit':
        break
    elif task == 'view ratings':
        display_ratings()
    elif task == 'rate':
        add_rating()
    elif task == 'get random':
        random_restaurant()