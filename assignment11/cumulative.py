# Task 2: A Line Plot with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Establish the relative path to the database file
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "..", "db", "lesson.db")

print(f"🔗 Connecting to database via relative path: {db_path}")
import os
import sqlite3

# 1. Finds the directory where this script sits (assignment11/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Looks up one level (..), then into the root db/ folder
db_path = os.path.abspath(os.path.join(BASE_DIR, "..", "db", "lesson.db"))

# 3. Connect to the real database file directly
conn = sqlite3.connect(db_path)

# Define the SQL statement to aggregate total price per order
query = """
SELECT 
    o.order_id, 
    SUM(p.price * l.quantity) AS total_price 
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id ASC;
"""

# Load the data into a DataFrame and close the database connection
df = pd.read_sql_query(query, conn)
conn.close()

# 2. Calculate cumulative sum using .apply()
def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

# 4. Generate the Line Plot using Pandas plotting functionality
df.plot(
    x="order_id", 
    y="cumulative", 
    kind="line", 
    color="crimson", 
    marker="o",
    linewidth=2,
    legend=False,
    title="Cumulative Company Revenue Over Time"
)

# Customize descriptive axis labels and layout spacing
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# 4. Display the graphical window
plt.show()
