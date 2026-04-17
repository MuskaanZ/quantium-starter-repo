import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_sales.csv")

# Ensure correct types
df["date"] = pd.to_datetime(df["date"])

# Aggregate sales by date
daily_sales = df.groupby("date")["sales"].sum().reset_index()
daily_sales = daily_sales.sort_values("date")

# Create figure
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)