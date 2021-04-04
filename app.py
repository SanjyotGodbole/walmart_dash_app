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
            "Walmart Data Analysis",
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
            dcc.Tabs([
                dcc.Tab(
                    label='Summary',
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id = "summary11",
                                    figure = chartMaker.plot_summary11()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "summary12",
                                    figure = chartMaker.plot_summary12()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "summary21",
                                    figure = chartMaker.plot_summary21()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "summary22",
                                    figure = chartMaker.plot_summary22()
                                )
                            ],
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
                ),
                dcc.Tab(
                    label='Store Sales Details',
                    children=[
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id='ssd_state_dropdown',
                                    options=[
                                        {'label':'California','value':'CA'},
                                        {'label':'Texas','value':'TX'},
                                        {'label':'Wisconsin','value':'WI'}
                                    ],
                                    value='CA' 
                                ),
                                html.Div(id='st-dd-output-container')
                            ],
                            style={
                                'font-size': '20px',
                                'font-family': 'Ariel',
                                'color': 'black',
                                'background-color': 'white',
                                'text-align': 'center',
                                # 'display': 'inline-block',
                                'border-style': 'solid',
                                'border-color': 'white',
                                'width': '25%',
                                # 'height': '40%'
                            }
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id = "ssd11",
                                    figure = chartMaker.plot_ssd11()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "ssd12",
                                    figure = chartMaker.plot_ssd12()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "ssd21",
                                    figure = chartMaker.plot_ssd21()
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "ssd22",
                                    figure = chartMaker.plot_ssd22()
                                )
                            ],
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
                ),
                dcc.Tab(
                    label='Event Sales Details',
                    children=[
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id='esd_state_dropdown',
                                    options=[
                                        {'label':'California','value':'CA'},
                                        {'label':'Texas','value':'TX'},
                                        {'label':'Wisconsin','value':'WI'}
                                    ],
                                    value='CA' 
                                ),
                                html.Div(id='esd-st-dd-output-container')
                            ],
                            style={
                                'font-size': '20px',
                                'font-family': 'Ariel',
                                'color': 'black',
                                'background-color': 'white',
                                'text-align': 'center',
                                # 'display': 'inline-block',
                                'border-style': 'solid',
                                'border-color': 'white',
                                'width': '25%',
                                # 'height': '40%'
                            }
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id = "esd11",
                                    figure = chartMaker.plot_esd('Religious_event')
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "esd12",
                                    figure = chartMaker.plot_esd('Cultural_event')
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "esd21",
                                    figure = chartMaker.plot_esd('National_event')
                                )
                            ],
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
                            children=[
                                dcc.Graph(
                                    id = "esd22",
                                    figure = chartMaker.plot_esd('Sporting_event')
                                )
                            ],
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
    
            ])
        )
    ]
)


# Creating callback buttons
@app.callback(
    Output('st-dd-output-container', 'children'),
    [Input('ssd_state_dropdown', 'value')]
)
def update_output(value):
    return 'showing results for "{}"'.format(value)

@app.callback(
    Output('ssd11', 'figure'),
    [Input('ssd_state_dropdown', 'value')]
)
def update_output(value):
    figure_ssd11 = chartMaker.plot_ssd11(value)
    return figure_ssd11

@app.callback(
    Output('ssd12', 'figure'), 
    [Input('ssd_state_dropdown', 'value')]
)
def update_output(value):
    figure_ssd12 = chartMaker.plot_ssd12(value)
    return figure_ssd12

@app.callback(
    Output('ssd21', 'figure'),
    [Input('ssd_state_dropdown', 'value')]
)
def update_output(value):
    figure_ssd21 = chartMaker.plot_ssd21(value)
    return figure_ssd21

@app.callback(
    Output('ssd22', 'figure'),
    [Input('ssd_state_dropdown', 'value')]
)
def update_output(value):
    figure_ssd22 = chartMaker.plot_ssd22(value)
    return figure_ssd22

@app.callback(
    Output('esd-st-dd-output-container', 'children'),
    [Input('esd_state_dropdown', 'value')]
)
def update_output(value):
    return 'showing results for "{}"'.format(value)

@app.callback(
    Output('esd11', 'figure'),
    [Input('esd_state_dropdown', 'value')]
)
def update_output(value):
    figure_esd11 = chartMaker.plot_esd('Religious_event', st=value)
    return figure_esd11

@app.callback(
    Output('esd12', 'figure'),
    [Input('esd_state_dropdown', 'value')]
)
def update_output(value):
    figure_esd12 = chartMaker.plot_esd('Cultural_event', st=value)
    return figure_esd12

@app.callback(
    Output('esd21', 'figure'),
    [Input('esd_state_dropdown', 'value')]
)
def update_output(value):
    figure_esd21 = chartMaker.plot_esd('National_event', st=value)
    return figure_esd21

@app.callback(
    Output('esd22', 'figure'),
    [Input('esd_state_dropdown', 'value')]
)
def update_output(value):
    figure_esd22 = chartMaker.plot_esd('Sporting_event', st=value)
    return figure_esd22


if __name__ == "__main__":
    app.run_server()