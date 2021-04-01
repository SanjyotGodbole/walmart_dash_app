import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import app_charts as ap
import data_reader as dr

data_dict = dr.charts_data()

chartMaker = ap.CHART_MAKER(data_dict)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

### defining the HTML component 
app.layout = html.Div(
    children=[
        html.Div(
            "Wallmart Data Analysis",
            style={
                'font-size': '40px',
                'font-family': 'Ariel',
                'color': 'white',
                'background-color': 'MediumSeaGreen',
                'text-align': 'center',
                'width':"100%"
                # 'display': 'inline-block'  
            }
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id = "Section11",
                    figure = chartMaker.plot_summary11()
                )
            ],
            # "Section 11",
            style={
                'font-size': '20px',
                'font-family': 'Ariel',
                'color': 'black',
                'background-color': 'LightGray',
                'text-align': 'center',
                'display': 'inline-block',
                'border-style': 'solid',
                'border-color': 'white',
                'width': '50%',
                'height': '40%'
            }
        ),
        html.Div(
            "Section 12",
            style={
                'font-size': '20px',
                'font-family': 'Ariel',
                'color': 'black',
                'background-color': 'LightGray',
                'text-align': 'center',
                'display': 'inline-block',
                'border-style': 'solid',
                'border-color': 'white',
                'width': '50%',
                'height': '40%'
            }
        ),
        html.Div(
            "Section 21",
            style={
                'font-size': '20px',
                'font-family': 'Ariel',
                'color': 'black',
                'background-color': 'LightGray',
                'text-align': 'center',
                'display': 'inline-block',
                'border-style': 'solid',
                'border-color': 'white',
                'width': '50%',
                'height': '40%'
            }
        ),
        html.Div(
            "Section 22",
            style={
                'font-size': '20px',
                'font-family': 'Ariel',
                'color': 'black',
                'background-color': 'LightGray',
                'text-align': 'center',
                'display': 'inline-block',
                'border-style': 'solid',
                'border-color': 'white',
                'width': '50%',
                'height': '40%'
            }
        ),

    ]
)


# Creating callback buttons
# @app.callback(
#     [
#         output("Section11")
#         # input=()
#     ]
# )

if __name__ == "__main__":
    app.run_server()