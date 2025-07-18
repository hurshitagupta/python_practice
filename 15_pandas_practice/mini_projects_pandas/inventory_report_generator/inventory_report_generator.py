#Project: Inventory Report Generator

import pandas as pd

#sample data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Phone", "Speaker", "Laptop", "Tablet", "Monitor", "Speaker"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Audio", "Electronics", "Electronics", "Electronics", "Audio"],
    "Price": [75000, 30000, 20000, 12000, 28000, 7000, 80000, 22000, 13000, 7500],
    "Quantity": [2, 3, 1, 4, 2, 5, 1, 3, 2, 4]
}

#converting into dataframe
df = pd.DataFrame(data)
print(f"{'*'*10} Raw Data{'*'*10}")
print(f"{df}\n")


#1. cleaning and organising

#a. sorting the df by product name a-z
df = df.sort_values("Product")
# print(df)

#b. Reset the index after sorting.
df = df.reset_index()

#resetting index adds a new column as index, so we will delete it
df = df.drop(columns="index")

# c. Uppercase all product names for consistency.
df["Product"] = df["Product"].str.upper()
print(f"{'*'*10} Data After Cleaning And Organising {'*'*10}")
print(f"{df}\n")


#2. Inventory Summary

#adding a new column called Total Revenue
df["Total Revenue"] = df["Price"] * df["Quantity"]
# print(df)

#preparing the inventory summary based per product
inventory_summary = df.groupby("Product").agg({
    "Quantity" : "sum",
    "Price" : "mean",
    "Total Revenue": "sum"
})
print(f"{'*'*10} Inventory Summary {'*'*10}")
print(f"{inventory_summary}\n")


#3. Category Level Insights

category_level_insight = df.groupby("Category").agg({
    "Quantity" : "sum",
    "Total Revenue" : "sum"
})

print(f"{'*'*10} Category Level Insights {'*'*10}")
print(f"{category_level_insight}\n")

#4.  top 3 products by total revenue

print(f"{'*'*10} Top 3 Products by Total Revenue {'*'*10}")
product_revenue = df.groupby("Product").agg({
    "Total Revenue" : "sum"
}).sort_values(("Total Revenue"),ascending=False).iloc[:3]

print(f"{product_revenue}\n")

#5. Low performing products

total_product_qty = df.groupby("Product").agg({
    "Quantity" : "sum"
})

print(f"{'*'*10} Low performing products {'*'*10}")
print(f"{total_product_qty[total_product_qty['Quantity']<4]}\n")

#6. Renaming "Audio" Category with "Sound Gear"

print(f"{'*'*10} Data {'*'*10}")

df["Category"] = df["Category"].str.replace("Audio","Sound Gear")
print(f"{df}\n")

#7. Average revenue per category in a sorted format.

avg_revenue = df.groupby("Category")["Total Revenue"].mean().sort_values()

print(f"{'*'*10} Average Revenue {'*'*10}")
print(f"{avg_revenue}\n")
