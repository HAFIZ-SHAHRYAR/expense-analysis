import pandas as pd

# Read the data
data = pd.read_csv("expenses.csv")

# Display the dataset
print(data)

# Calculate total expenses
total = data["Amount"].sum()

# Calculate average expense
average = data["Amount"].mean()

# Find spending by category
category_total = data.groupby("Category")["Amount"].sum()

print("\nTotal expenses:", total)
print("Average expense:", average)

print("\nExpenses by category:")
print(category_total)

import matplotlib.pyplot as plt

# BAR CHART
plt.figure(figsize=(8, 5))

category_total.plot(kind="bar")

plt.title("Monthly Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("expenses_bar_chart.png")
plt.show()


# PIE CHART
plt.figure(figsize=(7, 7))

category_total.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Expense Distribution by Category")
plt.ylabel("")
plt.tight_layout()

plt.savefig("expenses_pie_chart.png")
plt.show()
