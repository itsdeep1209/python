greats = {
    1: "James Gosling",
    2: "Dennis Ritchie",
    3: "Lars Bak",
    4: "Bjarne Stroustrup"
    
}

greats[5] = "Brendan Eich"
print(greats[3])
print(greats.get(4))
print(greats)
greats.update({1: "Guido van Rosum"})
print(greats)
greats.pop(5)
print(greats)
greats.popitem()
print(greats)