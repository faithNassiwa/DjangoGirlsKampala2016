print("Quiz 2")
# Marathon App using loops Quiz 2:

# Declaration and intialization
distance_to_cover = 102  # in miles
distance_covered_by_first_walker = 0  # in miles per hour
distance_covered_by_second_walker = 0  # in miles per hour
walking = True

while walking:  # Start loop
    distance_covered_by_first_walker += 2  # Increment till when rate_of_first_walker + rate_of_second_walker = 102
    distance_covered_by_second_walker += 1  # Increment till when rate_of_first_walker + rate_of_second_walker = 102

# The two walkers will meet at a point where the sum of the distances they have covered equate to the distance to cover
    if distance_covered_by_first_walker + distance_covered_by_second_walker == 102:
        print("They meet at {} miles from the start point of the first walker".format(distance_covered_by_first_walker))
        print("And at {} miles from the start point of the second walker ".format(distance_covered_by_second_walker))
