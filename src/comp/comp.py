# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i.name for i in humans if i.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [i.name for i in humans if i.name[len(i.name) - 1] == "e"]
# for e in humans:
#     index = len(e.name) - 1
#     if e.name[index] == "e":
#         b.append(e.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letter_range = ["C", "D", "E", "F", "G"]
c = [i.name for i in humans for r in letter_range if i.name[0] == r]
# for n in humans:
#     letter_range = ["C", "D", "E", "F", "G"]
#     for r in letter_range:
#         if n.name[0] == r:
#             c.append(n.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age + 10 for i in humans]
# for a in humans:
#     d.append(a.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{i.name}-{i.age}" for i in humans]
# for j in humans:
#     result = "{}-".format(j.name)
#     result += "{}".format(j.age)
#     e.append(result)
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(a.name, a.age) for a in humans if a.age >= 27 and a.age <= 32]
# for a in humans:
#     if a.age >= 27 and a.age <= 32:
#         f.append((a.name, a.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(h.name.upper(), h.age + 5) for h in humans]
# for h in humans:
#     g.append(Human(h.name.upper(), h.age + 5))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(s.age) for s in humans]
# for s in humans:
#     square = math.sqrt(s.age)
#     h.append(square)
print(h)
