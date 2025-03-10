# # Placeholder for reusable components

# import plotly.express as px

# def create_filters(vessel_types, nearest_ports, vessel_names, dates):
#     """
#     This function will create all the filters: dropdowns for vessel type, nearest port, vessel name,
#     and radio button for date.
#     """
#     return html.Div([
#         dcc.Dropdown(
#             id="vessel-type-filter",
#             options=[{"label": vt, "value": vt} for vt in vessel_types],
#             placeholder="Select Vessel Type",
#         ),
#         dcc.Dropdown(
#             id="nearest-port-filter",
#             options=[{"label": np, "value": np} for np in nearest_ports],
#             placeholder="Select Nearest Port",
#         ),
#         dcc.Dropdown(
#             id="vessel-name-filter",
#             options=[{"label": vn, "value": vn} for vn in vessel_names],
#             placeholder="Select Vessel Name",
#         ),
#         dcc.RadioItems(
#             id="date-filter",
#             options=[{"label": dt, "value": dt} for dt in dates],
#             labelStyle={"display": "inline-block"},
#         ),
#     ], style={'display': 'flex', 'gap': '10px'})

# def create_map(filtered_df):
#     """
#     This function generates a map with the filtered DataFrame.
#     It also adds summary information (total unique vessels) to the map title and as an annotation.
#     """
#     # Calculate the total number of unique vessels based on MMSI
#     unique_count = filtered_df["MMSI"].nunique()
    
#     # Create the map figure using Plotly Express
#     fig = px.scatter_mapbox(
#         filtered_df,
#         lat="LAT",
#         lon="LON",
#         color="Vessel Type Name",
#         hover_data=["MMSI", "VesselName", "SOG"],
#         mapbox_style="open-street-map",
#         zoom=5,
#         size_max=10
#     )
    
#     # Add an annotation with the unique vessel count (optional)
#     fig.add_annotation(
#         text=f"Total Unique Vessels: {unique_count}",
#         xref="paper", yref="paper",
#         x=0.05, y=0.95,  # Position near the top-left of the map
#         showarrow=False,
#         font=dict(size=14, color="black")
#     )
    
#     return fig


# Placeholder for reusable components

import plotly.express as px
from dash import html, dcc, dash_table
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

def create_filters(vessel_types, nearest_ports, vessel_names, dates):
    """
    This function will create all the filters: dropdowns for vessel type, nearest port, vessel name,
    and radio button for date.
    """
    return html.Div([
        dcc.Dropdown(
            id="vessel-type-filter",
            options=[{"label": vt, "value": vt} for vt in vessel_types],
            placeholder="Select Vessel Type",
        ),
        dcc.Dropdown(
            id="nearest-port-filter",
            options=[{"label": np, "value": np} for np in nearest_ports],
            placeholder="Select Nearest Port",
        ),
        dcc.Dropdown(
            id="vessel-name-filter",
            options=[{"label": vn, "value": vn} for vn in vessel_names],
            placeholder="Select Vessel Name",
        ),
        dcc.RadioItems(
            id="date-filter",
            options=[{"label": dt, "value": dt} for dt in dates],
            labelStyle={"display": "inline-block"},
        ),
    ], style={'display': 'flex', 'gap': '10px'})

def create_map(filtered_df):
    """
    This function generates a map with the filtered DataFrame.
    It also adds summary information (total unique vessels) to the map title and as an annotation.
    """
    # Calculate the total number of unique vessels based on MMSI
    unique_count = filtered_df["MMSI"].nunique()
    
    # Create the map figure using Plotly Express
    fig = px.scatter_mapbox(
        filtered_df,
        lat="LAT",
        lon="LON",
        color="Vessel Type Name",
        hover_data=["MMSI", "VesselName", "SOG"],
        mapbox_style="open-street-map",
        zoom=5,
        size_max=10
    )
    
    # Add an annotation with the unique vessel count (optional)
    fig.add_annotation(
        text=f"Total Unique Vessels: {unique_count}",
        xref="paper", yref="paper",
        x=0.05, y=0.95,  # Position near the top-left of the map
        showarrow=False,
        font=dict(size=14, color="black")
    )

    # Move the legend to the bottom center
    fig.update_layout(
        legend=dict(
            orientation="h",  # Make legend horizontal
            yanchor="bottom",  # Align legend at the bottom
            y=-0.05,  # Move legend slightly below the map
            xanchor="center",  # Center-align legend
            x=0.5  # Place legend in the middle
        ),
        margin=dict(r=0, t=0, l=0, b=20)  # Remove extra margins around the map
    )
    
    return fig

def create_port_table(port_result_df):
    """Create a Bootstrap Card containing the Port Table."""
    return dbc.Card(
        dbc.CardBody([ 
            html.H5("Number of Arrivals & Departures per Port", style={"fontFamily": "Arial, sans-serif"}),
            dash_table.DataTable(
                id="port-table",
                columns=[{"name": col, "id": col} for col in port_result_df.columns],
                data=port_result_df.to_dict("records"),
                page_size=4,
                style_table={"overflowX": "auto", "margin": "auto", "border": "none", "fontFamily": "Arial, sans-serif"},
                style_header={"fontWeight": "bold", "border": "none", "fontFamily": "Arial, sans-serif"},
                style_cell={"textAlign": "center", "border": "none", "fontFamily": "Arial, sans-serif"},
                style_data={"border": "none"}
            )
        ])
    )

# Function to create Bootstrap-styled summary cards
def create_summary_card(title, value, color):
    return dbc.Card(
        dbc.CardBody([ 
            html.H5(title, className="card-title"),
            html.H3(id=value, children="...", className="card-text", style={"fontWeight": "bold"})
        ]),
        style={"textAlign": "center", "margin": "10px", "backgroundColor": color, "color": "white"}
    )

# Function to create trend graph with dynamic height
def create_trend_graph(df):
    df_trend = df.groupby('Hour').size().reset_index(name='Unique Vessels')

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_trend['Hour'],
        y=df_trend['Unique Vessels'],
        mode='lines+markers',
        name='Unique Vessels Over Time',
        line=dict(color='blue')
    ))

    # Dynamically adjust height
    min_height = 150  
    max_height = 300  
    graph_height = min(max(len(df_trend) * 10, min_height), max_height)

    fig.update_layout(
        title='Trend of Unique Vessels Over Time',
        xaxis_title='Hour of the Day',
        yaxis_title='Number of Vessels',
        template='plotly_white',
        margin=dict(l=20, r=20, t=30, b=20),
        height=graph_height
    )

    return dcc.Graph(id="trend-graph", figure=fig, style={"height": "100%", "width": "100%"})

# Function to create the footer
def create_footer():
    return html.Footer(
        dbc.Container(
            dbc.Row(
                dbc.Col([
                    html.Hr(), 
                    html.P("Vessel Vision, extract and process AIS data for maritime traffic analysis.", className="text-center", style={"fontWeight": "bold","margin-bottom": "2px"}),
                    html.P("Developed by [DSCI-532-group5]: Azin Piran, Stephanie Wu, Yasmin Hassan, Zoe Ren", className="text-center",style={"margin-bottom": "2px"}),
                    html.P([
                        "GitHub Repository: ",
                        html.A("Vessel Vision", href="https://github.com/UBC-MDS/DSCI-532_2025_5_vessel-vision", target="_blank")
                    ], className="text-center",style={"margin-bottom": "2px"}),
                    html.P(f"Last updated: 2025-03-01", className="text-center",style={"margin-bottom": "2px"}),
                ])
            )
        ),
        style={
            "position": "relative",  
            "bottom": "0",
            "width": "100%",
            "padding": "0px",
            "backgroundColor": "#e9ecef",
            "textAlign": "center"
            #"borderTop": "1px solid #ccc"
        }
    )