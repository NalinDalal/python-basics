friends = ["Kevin", "Karen", "Jim"]
print(friends[0])
print(friends[-1])
friends[1] = "Mike"

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = ["Nalin", "Kripa", "Yogesh"]
friends1.extend(
    friends2
)  # extend() adds all elements of another list to the end of the current list
# note: type should be same for both

# append() adds a single element to the end of the list (like push in other languages)
friends1.append("Creed")

# insert(index, value) inserts an element at a specific position
# Here, "Kelly" will be inserted at index 1 (second position)
friends1.insert(1, "Kelly")

# remove(value) removes the first occurrence of the specified value
friends1.remove("Jim")

print(friends1)

# find index of something
print(friends1.index("Kevin"))

# find count of something: how many times it occurs
print(friends1.count("Kevin"))
