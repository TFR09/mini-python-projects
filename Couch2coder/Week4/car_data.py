import csv

cars = []

with open("vw.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        cars.append(row)

most_expensive = cars[0]
for car in cars:
    price = int(car["price"])
    highest = int(most_expensive["price"])
    if price > highest:
        most_expensive = car

print(f"The most expensive car is VW {most_expensive}")      

total_price = 0
golfs = 0
for car in cars:
    if car["model"] == "Golf":
        total_price += int(car["price"])
        golfs += 1

average_price = round(total_price / golfs)
print(f"The average price of the VW Golf Model is ${average_price}")

total_mileage = 0
polos = 0
for car in cars:
    if car["model"] == "Polo" and car["year"] == "2020":
        total_mileage += int(car["mileage"])
        polos += 1

average_mileage = round(total_mileage / polos)
print(f"The average mileage of all VW Polos registered in 2020 is {average_mileage} miles")