import pandas as pd
import matplotlib.pyplot as plt


cars = pd.read_csv("vw.csv")


# PIE CHART 
# Data for the pie chart
fuel = cars["fuelType"].unique()
fuel = sorted(fuel, key=lambda f: f[2])
fuel_distribution = cars.groupby("fuelType")["fuelType"].count()
fuel_distribution = fuel_distribution.reindex(fuel)

# Pie chart figure of Distribution between fuel types
plt.figure(figsize=(4, 4))
plt.pie(fuel_distribution, labels=fuel, autopct="%.2f%%", startangle=140, pctdistance=1.3)
plt.title("Distribution of Car Fuel Types")
plt.axis('equal')


# BAR CHART
# data for bar graph
models = cars["model"].unique()
avg_mileage_per_model = cars.groupby("model")["mileage"].mean()
avg_mileage_per_model = avg_mileage_per_model.reindex(models)

# Bar Chart figure showing average miles per model
plt.figure(figsize=(10,5))
plt.bar(models, avg_mileage_per_model, width=0.5)
plt.title("Average Miles per Volkswagen Model", pad=30)
plt.xticks(rotation=90, fontsize=8)
plt.xlabel("Models")
plt.ylabel("Miles")
plt.subplots_adjust(bottom=0.255, right=0.95, left=0.1)
plt.show()