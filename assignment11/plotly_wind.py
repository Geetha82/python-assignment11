# Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import pandas as pd
import os

# 1. Load the Plotly built-in wind dataset as a Pandas DataFrame
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

# 2. Print the first and last 10 lines of the DataFrame to the terminal
print("===== FIRST 10 ROWS =====")
print(df.head(10))
print("\n===== LAST 10 ROWS =====")
print(df.tail(10))

# 3. Clean the Data: Convert 'strength' column to a float
# strip non-numeric card markers if present and convert the type explicitly
df['strength'] = df['strength'].astype(str).str.replace(r'[^\d\.]', '', regex=True).astype(float)

# 4. Create an Interactive Scatter Plot
fig = px.scatter(
    df, 
    x="frequency", 
    y="strength", 
    color="direction",
    title="Wind Analysis: Strength vs. Frequency by Direction",
    labels={"frequency": "Frequency", "strength": "Strength", "direction": "Direction"}
)

# 5. Determine the file output path inside assignment11/
base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "wind.html")

# 6. Save the interactive plot as a standalone HTML file
fig.write_html(html_path)
print(f"\nInteractive plot generated and successfully saved to: {html_path}")
