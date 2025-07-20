fruit_colors = {
    "apple" : "red",
    "banana" : "yellow",
    "grape" : "purple"
}
print(fruit_colors)

ages ={"Alice" : 25, "Bob" : 30, "Charlie" : 22}
print(ages["Bob"])

country_capitals = {
    "France" : "Paris",
    "Japan" : "Tokyo"
}
country_capitals ["Germany"] = "Berlin"
country_capitals ["Japan"] = "Kyoto"
print(country_capitals)

inventory = {
    "apple" : 10,
    "banana" : 5,
    "orange" : 8
    }
del inventory ["banana"]
print(inventory)

book = {
    "title" : "1984",
    "author" : "George Orwell",
    "year" : 1949
}
keys = book.keys()
values = book.values()
items = book.items()
print(keys)
print(values)
print(items)

grades = {
    "Math" : 90,
    "Science" : 85,
    "History" : 78

}
print("Science" in grades)
print(78 in grades.values())
