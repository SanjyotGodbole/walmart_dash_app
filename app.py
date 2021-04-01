import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
# import data_preprocess as pp
# import app_charts as ap
# # import main

# df = pp.preprocess()

# data = ap.CHART_MAKER(df)

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
            "Section 11",
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

if __name__ == "__main__":
    app.run_server()