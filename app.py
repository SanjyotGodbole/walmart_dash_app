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
                        # html.Div(
                        #     children=[
                        #         dcc.Graph(
                        #             id = "ssd21",
                        #             figure = chartMaker.plot_ssd21()
                        #         )
                        #     ],
                        #     style={
                        #         'font-size': '20px',
                        #         'font-family': 'Ariel',
                        #         'color': 'black',
                        #         'background-color': 'LightGray',
                        #         'text-align': 'center',
                        #         'display': 'inline-block',
                        #         'border-style': 'solid',
                        #         'border-color': 'white',
                        #         'width': '50%',
                        #         'height': '40%'
                        #     }
                        # ),
                        # html.Div(
                        #     children=[
                        #         dcc.Graph(
                        #             id = "ssd22",
                        #             figure = chartMaker.plot_ssd22()
                        #         )
                        #     ],
                        #     style={
                        #         'font-size': '20px',
                        #         'font-family': 'Ariel',
                        #         'color': 'black',
                        #         'background-color': 'LightGray',
                        #         'text-align': 'center',
                        #         'display': 'inline-block',
                        #         'border-style': 'solid',
                        #         'border-color': 'white',
                        #         'width': '50%',
                        #         'height': '40%'
                        #     }
                        # ),                    
                    ]
                )    
            ])
        )
    ]
)
#         html.Div(
#             children=[
#                 html.Button(
#                     'Summary',
#                     id='summary_button',
#                     style={
#                         'font-size': '20px',
#                         'font-family': 'Ariel',
#                         'color': 'black',
#                         'background-color': 'LightGray',
#                         'text-align': 'center',
#                         'display': 'inline-block',
#                         'border-style': 'solid',
#                         'border-color': 'white',
#                         'width': '30%',
#                         'height': '10%'
#                     }
#                 )
#             ],
            
#         ),
#         html.Div(
#             children=[
#                 html.Button(
#                     'Store Sales Details',
#                     id='ssd_button',
#                     style={
#                         'font-size': '20px',
#                         'font-family': 'Ariel',
#                         'color': 'black',
#                         'background-color': 'LightGray',
#                         'text-align': 'center',
#                         'display': 'inline-block',
#                         'border-style': 'solid',
#                         'border-color': 'white',
#                         'width': '30%',
#                         'height': '10%'
#                     }
#                 )
#             ],
            
#         ),
#         html.Div(
#             children=[
#                 html.Button(
#                     'Event Sales Detail',
#                     id='psd_button',
#                     style={
#                         'font-size': '20px',
#                         'font-family': 'Ariel',
#                         'color': 'black',
#                         'background-color': 'LightGray',
#                         'text-align': 'center',
#                         'display': 'inline-block',
#                         'border-style': 'solid',
#                         'border-color': 'white',
#                         'width': '30%',
#                         'height': '10%'
#                     }
#                 )
#             ]    
#         ),
#         html.Div(
#             children=[
#                 dcc.Graph(
#                     id = "summary11",
#                     figure = chartMaker.plot_summary11()
#                 )
#             ],
#             style={
#                 'font-size': '20px',
#                 'font-family': 'Ariel',
#                 'color': 'black',
#                 'background-color': 'LightGray',
#                 'text-align': 'center',
#                 'display': 'inline-block',
#                 'border-style': 'solid',
#                 'border-color': 'white',
#                 'width': '50%',
#                 'height': '40%'
#             }
#         ),
#         html.Div(
#             children=[
#                 dcc.Graph(
#                     id = "summary12",
#                     figure = chartMaker.plot_summary12()
#                 )
#             ],
#             style={
#                 'font-size': '20px',
#                 'font-family': 'Ariel',
#                 'color': 'black',
#                 'background-color': 'LightGray',
#                 'text-align': 'center',
#                 'display': 'inline-block',
#                 'border-style': 'solid',
#                 'border-color': 'white',
#                 'width': '50%',
#                 'height': '40%'
#             }
#         ),
#         html.Div(
#             children=[
#                 dcc.Graph(
#                     id = "summary21",
#                     figure = chartMaker.plot_summary21()
#                 )
#             ],
#             style={
#                 'font-size': '20px',
#                 'font-family': 'Ariel',
#                 'color': 'black',
#                 'background-color': 'LightGray',
#                 'text-align': 'center',
#                 'display': 'inline-block',
#                 'border-style': 'solid',
#                 'border-color': 'white',
#                 'width': '50%',
#                 'height': '40%'
#             }
#         ),
#         html.Div(
#             children=[
#                 dcc.Graph(
#                     id = "summary22",
#                     figure = chartMaker.plot_summary22()
#                 )
#             ],
#             style={
#                 'font-size': '20px',
#                 'font-family': 'Ariel',
#                 'color': 'black',
#                 'background-color': 'LightGray',
#                 'text-align': 'center',
#                 'display': 'inline-block',
#                 'border-style': 'solid',
#                 'border-color': 'white',
#                 'width': '50%',
#                 'height': '40%'
#             }
#         ),
#         html.Div(
#             id='output-state'
#         ),

#     ]
# )


# Creating callback buttons
@app.callback(
    Output("output-state", 'children'),
    Input('summary_button', 'n_click'),
    State('summary11', 'figure'),
    State('summary12', 'figure'),
    State('summary21', 'figure'),
    State('summary22', 'figure'),
)

def update_output(n_clicks,summary11input, summary12input, summary21input, summary22input):
    return 'figure', 'figure', 'figure', 'figure'


if __name__ == "__main__":
    app.run_server()