"""Restaurant rating lister."""

filename = "scores.txt"
restaurant_ratings = {}

for line in open(filename):
    line = line.rstrip()
    restaurant = line.split(":")[0]
    rating = line.split(":")[1]
    restaurant_ratings[restaurant] = rating

for restaurant, rating in sorted(restaurant_ratings.items()):
    print(f"{restaurant} is rated at {rating}.")