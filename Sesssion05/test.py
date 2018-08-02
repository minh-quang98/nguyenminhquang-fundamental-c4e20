# quy = ["nam", 77, "Vinh", 21, ["Anime", "Manga"]]
# dictionary
# CRUD
#key : value
person = {
    "name": "Quý",
    "age": 20,
    "university": "hust",
    "ex": 2,
    "favs": ["Anime", "Manga"],
}

key = "age"
if key in person:
    print(person[key])
else:
    print("Not found")

# for key in person.keys():
#     print(key, end="\t")

# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)

# update
# person["ex"] = 20
# person["gender"] = "male"

# # delete
# del person["age"]
# print(person)