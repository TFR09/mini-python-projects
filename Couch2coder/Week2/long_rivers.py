# River data
rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

# Print all river names
for river in rivers:
    print(river["name"])

# Print total length of rivers
total = 0
for river in rivers:
    total += river["length"]
print(f"The rivers above span a total length of {total} miles")

# Print all rivers starting with M
print("The rivers starting with M are:")
for river in rivers:
    if river["name"][0] == "M":
        print(river["name"])

# Print all river length in miles
for river in rivers:
    length = round(river["length"] * 1.6)
    print(f"The length of the {river['name']} river is {length} km")