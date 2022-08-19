from fileinput import filename

def restaurant_rate_lister(filename):
    """Restaurant rating lister."""
    #open/take in file (scores.txt)

    # from fileinput import filenamep

    with open(filename) as restaurant_ratings:
    #read ratings

    #create dictionary from ratings
        restaurant_reviews = {}
        for line in restaurant_ratings.readlines():
            line = line.replace("\n", "")
            result = line.split(":") #["Florean Fortescue's Ice Cream Parlour", "4"]
            restaurant = result[0]
            rating = result[1]
            # dictionary = {}
            # dictionary[key] = value
            # {key: value}
            restaurant_reviews[restaurant] = [rating]
           
        print(restaurant_reviews)

        return restaurant_reviews

print(restaurant_rate_lister("scores.txt"))


#sort dictionary alphabetically