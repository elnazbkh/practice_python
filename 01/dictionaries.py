
#movie = ["sunlight", "woody allen", 2009,"yes", "no"]

movie ={"title":"sunlight", "director": "woody allen", "year": 2009, "answer": "yes"}
print(movie["title"])

#print(movie.clear())

print(movie.values())

print(movie.__len__())
print(movie.get("name"))

movie.update({"a": 1235, "b":585})

print(movie)
print(movie.get("writer", "unknown"))
print(movie.keys())
print(list(movie.keys()))