def agr_ratings(ratings):
    if not ratings:
        print("No ratings provided.")
        return []

    good_ratings_squared = [rating ** 2 for rating in ratings if rating >= 5]
    
    return good_ratings_squared

ratings = [8, 4, 7, 2, 10, 5, 6]  
result = agr_ratings(ratings)
print("Good ratings squared:", result)
