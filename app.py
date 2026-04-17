import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Sort base data
df = df.sort_values("date")

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(style={
    "fontFamily": "Arial",
    "backgroundColor": "#f4f6f8",
    "padding": "20px"
}, children=[

    html.H1(
        "Pink Morsel Sales Dashboard",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),
    ]),

    dcc.Graph(id="sales-graph")
])


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = filtered_df.groupby("date")["sales"].sum().reset_index()
    daily_sales = daily_sales.sort_values("date")

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)