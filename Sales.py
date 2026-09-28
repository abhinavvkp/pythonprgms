import pandas as pd

# Load the sales dataset
df = pd.read_csv("sakes.csv")

# Display the dataset
print("Sales Dataset:")
print(df)

# Find total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Find average sales
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# Find maximum sales
maximum_sales = df["Sales"].max()
print("Maximum Sales:", maximum_sales)

# Find minimum sales
minimum_sales = df["Sales"].min()
print("Minimum Sales:", minimum_sales)

# Display customers with sales greater than a specific amount
amount = 30000
print("\nCustomers with Sales greater than", amount, ":")
result = df[df["Sales"] > amount]
print(result)

# Sort sales data in descending order
print ("\nSales Data Sorted by Sales:")
sorted_df = df.sort_values(by="Sales", ascending=False)
print(sorted_df)
