people = [
    {"name": "Kofi", "age": 25},
    {"name": "Adwoa", "age": 30},
    {"name": "Kwame", "age": 22},
    {"name": "Ewura", "age": 28},
]

people.sort(key= lambda person: person["age"])
print(people)