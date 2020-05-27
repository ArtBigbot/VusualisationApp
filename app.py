

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import random
from collections import deque
from dash.dependencies import Output, Input, State
import plotly
import dash_daq as daq
import psycopg2
import datetime as dt
import plotly.graph_objects as go
import sys, os
import numpy as np
import pandas.io.sql as psql
import matplotlib.pyplot as plt
from matplotlib import units

conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel", password="ruuvisel")
cursor = conn.cursor()
query = "SELECT * FROM vw_sensorsdata WHERE room ='208' ORDER BY date_time DESC LIMIT 20"


def create_pandas_table(query, database=conn):
    table = pd.read_sql_query(query, database)
    return table


dataFrame = create_pandas_table(query)
available_indicators = dataFrame['valuetype'].unique()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app1 = dash.Dash(__name__, assets_folder='assets', include_assets_files=True)
server = app.server

app.layout = html.Div([

    html.H4('dbhitsa2019'),

    dcc.Interval(
        id='update',
        interval=300000),

    dcc.Tabs([
        dcc.Tab(label='Tab one', children=[
            html.Div([
                # 'gauges',
                html.Div([

                    daq.Gauge(
                        showCurrentValue=True,
                        id='gaugeTemperatureAndHumiditySensor',
                        color="#9B51E0",
                        label={
                            'label': 'Temperature',
                            'style': {
                                'fontSize': 19
                            }
                        },
                        min=0,
                        units='C ',
                        max=50,
                        size=200,
                        theme='dark',
                        style={'display': 'block'},

                    ),
                ], style={'position': 'absolute', 'top': '20%', 'width': '200px', 'height': '250px', 'left': '5%'}),
                html.Label('Temperature and Humidity Sensor',
                           style={'position': 'absolute', 'top': '47%', 'left': '2%', 'fontSize': 19}),
                html.Div((

                    daq.Gauge(
                        showCurrentValue=True,
                        id='gaugeHighAccuracySensor',
                        color="#9B51E0",

                        label={
                            'label': 'Temperature',
                            'style': {
                                'fontSize': 19
                            }
                        },

                        min=0,
                        units='C'
                        ,
                        max=50,
                        size=200,
                        theme='dark',
                        style={'display': 'block'}
                    ),
                ), style={'position': 'absolute', 'top': '20%', 'left': '25%', 'width': '200px', 'height': '250px', }),
                html.Label('High Accuracy Sensor',
                           style={'position': 'absolute', 'top': '47%', 'left': '25%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='humidityGauge',
                              units="%",

                              color="#9B51E0",

                              label={
                                  'label': 'Humidity',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=70,
                              min=0,
                              size=200,

                              style={'display': 'block', 'stroke-width': '20px'})
                ], style={'position': 'absolute', 'top': '60%', 'left': '5%', 'width': '200px', 'height': '250px', }),
                html.Label('Temperature and Humidity sensor',
                           style={'position': 'absolute', 'top': '87%', 'left': '2%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='lumenGauge',
                              units="lm",
                              color="#9B51E0",
                              label={
                                  'label': 'Lumen',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },

                              max=1000,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '20%', 'left': '45%', 'rigth': '80%', 'width': '200px',
                          'height': '250px'}),
                html.Label('Sunlight Sensor',
                           style={'position': 'absolute', 'top': '47%', 'left': '47%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='ultravioletGauge',
                              units="Uv",
                              color="#9B51E0",
                              label={
                                  'label': 'Ultraviolet index',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=1,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '60%', 'left': '25%', 'rigth': '80%', 'width': '200px',
                          'height': '250px'}),
                html.Label('Sunlight Sensor',
                           style={'position': 'absolute', 'top': '87%', 'left': '27%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='IlluminanceGauge',
                              units="Lux",
                              color="#9B51E0",

                              label={
                                  'label': 'Illuminance',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=100,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '60%', 'left': '68%', 'rigth': '35%', 'width': '200px',
                          'height': '250px'}),
                html.Label('Light Sensor',
                           style={'position': 'absolute', 'top': '87%', 'left': '71%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='TotalVoletileOrganicCompoundsGauge',
                              units='PPB',
                              color="#9B51E0",
                              label={
                                  'label': 'TVOC',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=10,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '20%', 'left': '68%', 'rigth': '35%', 'width': '200px',
                          'height': '590px'}),
                html.Label('Grove VOC and eCO2 Gas Sensor',
                           style={'position': 'absolute', 'top': '47%', 'left': '66%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='detsibellGauge',
                              units="DB",
                              color="#9B51E0",
                              label={
                                  'label': 'Detsibell',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=200,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '60%', 'left': '45%', 'rigth': '80%', 'width': '200px',
                          'height': '250px'}),
                html.Label('Loudness Sensor',
                           style={'position': 'absolute', 'top': '87%', 'left': '47%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='CarbonDioxideEquivalentCO2Gauge',
                              units='PPM',

                              # style={'font-size': '30px'},
                              color="#9B51E0",

                              label={
                                  'label': 'CO2',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              # label={},
                              max=1,
                              min=0,
                              size=200,
                              style={'fontSize': '30%'}
                              ),

                ], style={'position': 'absolute', 'top': '60%', 'left': '83%', 'rigth': '5%', 'width': '300px',
                          'height': '500px'}),
                html.Label('CarbonDioxideEquivalent Sensor CO2',
                           style={'position': 'absolute', 'top': '87%', 'left': '85%', 'fontSize': 19}),

                html.Div([
                    daq.Gauge(showCurrentValue=True,
                              id='PirOn',

                              color="#9B51E0",
                              units='BITT',
                              label={
                                  'label': 'The existance of movement',
                                  'style': {
                                      'fontSize': 19
                                  }
                              },
                              max=1,
                              min=0,
                              size=200)
                ], style={'position': 'absolute', 'top': '20%', 'left': '85%', 'rigth': '5%', 'width': '200px',
                          'height': '250px'}),
                html.Label('PIR motion Sensor PIR on',
                           style={'position': 'absolute', 'top': '49%', 'left': '85%', 'fontSize': 19}),

            ]),
        ]),

        # html.Div([
        dcc.Tab(label='Tab two', children=[
            html.Div([

                dcc.RadioItems(
                    id='graph_type_tempeture',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphTempeture')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),
            # animate=True
            # ],
            html.Div([

                dcc.RadioItems(
                    id='graph_type_lumens',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphLumens')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_tvoc',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphTVOC')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_humidity',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphHumidity')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_ultra_violetindex',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphUltraVioletIndex')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_detsibel',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphDetsibel')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_illuminance',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphIlluminance')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_co2',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphCO2')
            ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),

            html.Div([

                dcc.RadioItems(
                    id='graph_type_piron',
                    options=[{'label': i, 'value': i} for i in ['Päevakeskmine', 'Aegsel']],
                    value='Päevakeskmine',
                    labelStyle={'display': 'inline-block'}
                ),

                dcc.Graph(
                    id='graphPIRon')
            ], style={'display': 'inline-block', 'height': '15%', 'width': '30%', 'top': '700%', 'left': '330%',
                      'right': '20%'}),
            # ], style={'padding': '120px 20px 20px 20px', })
        ]),

        dcc.Tab(label='Tab three', children=[
            html.Div([
                dcc.Dropdown(
                    id='indicator',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='T'),

                dcc.DatePickerRange(
                    id="datePickerId",
                    # start_date=""
                    start_date_placeholder_text="Start Period",
                    start_date_id="startDateId",
                    end_date_id="endDateId",
                    start_date='2020-05-06',
                    end_date='2020-05-21',
                    display_format='MMM Do, YY',
                    end_date_placeholder_text="End Period",

                )

            ], style={'width': '15%'}, ),
            html.Div([dash_table.DataTable(
                id='data_table',
                # page_sice=5,
                # data=dataFrame.to_dict('records'),
                columns=[{'id': c, 'name': c, 'hideable': True} for c in dataFrame.columns],
                # fixed_rows={'headers': True, 'data': 0},
                export_format='xlsx',
                export_headers='display',
                style_table={
                    'maxHeight': '700px',
                    'maxWidth': '1700px',
                    'overflowY': 'scroll',
                    'overflowX': 'scroll'
                },
                style_cell={
                    'width': '190px',
                    'height': '60px',
                    'font-size': '20px',
                    'textAlign': 'center'
                }
            )], style={'position': 'absolute', 'top': '18%', 'left': '15%', 'rigth': '80%', 'width': '1700px',
                       'height': '700px', 'border': '9B51E0'}),

            html.Div([
                dcc.Dropdown(
                    id='dropDownList',
                    options=[
                        {'label': 'Hour average', 'value': 'Hour average'},
                        {'label': 'Day average', 'value': 'Day average'},
                        {'label': 'Week average', 'value': 'Week average'},
                        {'label': 'Mounth average', 'value': 'Mounth average'}
                    ],
                    placeholder="Select a parameter",
                ),

                dcc.Graph(
                    id='graph'
                )], style={'position': 'absolute', 'top': '110%', 'left': '15%', 'width': '1700px'})

        ]),
        dcc.Tab(label='Tab four', children=[
            html.Div([
                dcc.Dropdown(
                    id='firstParameter',
                    options=[{'label': i, 'value': i} for i in available_indicators], style={'width': '50%'},
                    value='T'
                ),
                dcc.Dropdown(
                    id='secondParameter',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    style={'top': '10%', 'left': '60%', 'width': '50%'},
                    value='Humidity'
                ),
                dcc.DatePickerRange(
                    id="datePickerRangeId",
                    # start_date=""
                    start_date_placeholder_text="Start Period",
                    start_date_id="startDateId",
                    end_date_id="endDateId",
                    start_date='2020-04-01',
                    end_date='2020-04-10',
                    display_format='MMM Do, YY',
                    end_date_placeholder_text="End Period",

                ),
                dcc.Graph(
                    id='crossfilterParameterGraph',
                    hoverData={'points': [{'customdata': ''}]}
                )
            ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})

        ])
    ])
])


@app.callback(dash.dependencies.Output('graphTempeture', 'figure'),
              [dash.dependencies.Input('graph_type_tempeture', 'value'), ])
def update_graph_tempeture(graph_type_tempeture):
    if graph_type_tempeture == 'Aegsel':
        return draw_graphScetter('Temperatuur', 'T')
    elif graph_type_tempeture == 'Päevakeskmine':
        return draw_graphBar('Temperatuur', 'T')


@app.callback(dash.dependencies.Output('graphLumens', 'figure'),
              [dash.dependencies.Input('graph_type_lumens', 'value'), ])
def update_graph_lumens(graph_type_lumens):
    if graph_type_lumens == 'Aegsel':
        return draw_graphScetter('Lumens', 'Lumen')
    elif graph_type_lumens == 'Päevakeskmine':
        return draw_graphBar('Lumens', 'Lumen')


@app.callback(dash.dependencies.Output('graphTVOC', 'figure'),
              [dash.dependencies.Input('graph_type_tvoc', 'value'), ])
def update_graph_tvoc(graph_type_tvoc):
    if graph_type_tvoc == 'Aegsel':
        return draw_graphScetter('Total Volatile Organic Compunds', 'Total Volatile Organic Compounds')
    elif graph_type_tvoc == 'Päevakeskmine':
        return draw_graphBar('Total Volatile Organic Compunds', 'Total Volatile Organic Compounds')


@app.callback(dash.dependencies.Output('graphHumidity', 'figure'),
              [dash.dependencies.Input('graph_type_humidity', 'value'), ])
def update_graph_humidity(graph_type_tvoc):
    if graph_type_tvoc == 'Aegsel':
        return draw_graphScetter('Niiskus', 'Humidity')
    elif graph_type_tvoc == 'Päevakeskmine':
        return draw_graphBar('Niiskus', 'Humidity')


@app.callback(dash.dependencies.Output('graphUltraVioletIndex', 'figure'),
              [dash.dependencies.Input('graph_type_ultra_violetindex', 'value'), ])
def update_graph_humidity(graph_type_ultra_violetindex):
    if graph_type_ultra_violetindex == 'Aegsel':
        return draw_graphScetter('Ultraviolet indeks', 'Ultraviolet index')
    elif graph_type_ultra_violetindex == 'Päevakeskmine':
        return draw_graphBar('Ultraviolet indeks', 'Ultraviolet index')


@app.callback(dash.dependencies.Output('graphDetsibel', 'figure'),
              [dash.dependencies.Input('graph_type_detsibel', 'value'), ])
def update_graph_detsibell(graph_type_detsibel):
    if graph_type_detsibel == 'Aegsel':
        return draw_graphScetter('Destibell', 'Detsibell')
    elif graph_type_detsibel == 'Päevakeskmine':
        return draw_graphBar('Destibell', 'Detsibell')


@app.callback(dash.dependencies.Output('graphIlluminance', 'figure'),
              [dash.dependencies.Input('graph_type_illuminance', 'value'), ])
def update_graph_detsibell(graph_type_illuminance):
    if graph_type_illuminance == 'Aegsel':
        return draw_graphScetter('Illuminatsioon', 'Illuminance (IR)')
    elif graph_type_illuminance == 'Päevakeskmine':
        return draw_graphBar('Illuminatsioon', 'Illuminance (IR)')


@app.callback(dash.dependencies.Output('graphCO2', 'figure'),
              [dash.dependencies.Input('graph_type_co2', 'value'), ])
def update_graph_detsibell(graph_type_co2):
    if graph_type_co2 == 'Aegsel':
        return draw_graphScetter('Carbon dioxide equivalent CO2eq', 'Carbon dioxide equivalent CO2eq')
    elif graph_type_co2 == 'Päevakeskmine':
        return draw_graphBar('Carbon dioxide equivalent CO2eq', 'Carbon dioxide equivalent CO2eq')


@app.callback(dash.dependencies.Output('graphPIRon', 'figure'),
              [dash.dependencies.Input('graph_type_piron', 'value'), ])
def update_graph_detsibell(graph_type_piron):
    if graph_type_piron == 'Aegsel':
        return draw_graphScetter('PIR on', 'PIR on')
    elif graph_type_piron == 'Päevakeskmine':
        return draw_graphBar('PIR on', 'PIR on')


@app.callback(
    Output(component_id='data_table', component_property='data'),
    [Input(component_id='indicator', component_property='value'),
     Input(component_id='datePickerId', component_property='start_date'),
     Input(component_id='datePickerId', component_property='end_date')
     ]
)
def update_table(parameter, start_date, end_date):
    query = "SELECT * FROM vw_sensorsdata WHERE room= '208' AND valuetype ='%s' AND date_time BETWEEN '%s' AND " \
            "'%s' ORDER BY date_time DESC " % (parameter, start_date, end_date)
    table = pd.read_sql_query(query, conn)
    return table.to_dict('records')


@app.callback(
    dash.dependencies.Output('gaugeTemperatureAndHumiditySensor', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_GaugeTempFromTemperatureAndHumiditySensor(value):
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT  data FROM vw_sensorsdata WHERE valuetype ='T' AND room = '208' AND" +
                   " sensor ='Temperature and Humidity Sensor Pro' ORDER BY date_time DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    tempeture = dff.iat[0, 0]
    conn.close()
    return tempeture


@app.callback(
    dash.dependencies.Output('gaugeHighAccuracySensor', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_GaugeTempFromHighAccuracyTemperature(value):
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  data FROM vw_sensorsdata WHERE valuetype ='T' AND room = '208' AND sensor ='High Accuracy Temperature' ORDER BY date_time DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    tempeture = dff.iat[0, 0]
    conn.close()
    return tempeture


@app.callback(
    dash.dependencies.Output('humidityGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_GaugeHumidity(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  data FROM vw_sensorsdata WHERE valuetype ='Humidity' AND room = '208' ORDER BY date_time DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    humidity = dff.iat[0, 0]
    conn.close()
    return humidity


@app.callback(
    dash.dependencies.Output('lumenGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_LumenGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  data FROM vw_sensorsdata WHERE valuetype ='Lumen' AND room = '208' ORDER BY date_time DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    lumens = dff.iat[0, 0]
    conn.close()
    return lumens


@app.callback(
    dash.dependencies.Output('ultravioletGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_ultravioletGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='Ultraviolet index' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    uvIndex = dff.iat[0, 0]
    conn.close()
    return uvIndex


@app.callback(
    dash.dependencies.Output('PirOn', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_PirOnGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='PIR on' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    piron = dff.iat[0, 0]
    conn.close()
    return piron


@app.callback(
    dash.dependencies.Output('IlluminanceGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_IlluminanceGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='Illuminance (IR)' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    illuminance = dff.iat[0, 0]
    conn.close()
    return illuminance


@app.callback(
    dash.dependencies.Output('CarbonDioxideEquivalentCO2Gauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_CO2Gauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='Carbon dioxide equivalent CO2eq' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    co2 = dff.iat[0, 0]
    conn.close()
    return co2


@app.callback(
    dash.dependencies.Output('detsibellGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_detsibellGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='Detsibell' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    detsibell = dff.iat[0, 0]
    conn.close()
    return detsibell


@app.callback(
    dash.dependencies.Output('TotalVoletileOrganicCompoundsGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
)
def update_TVOCGauge(value):
    # return value
    dataSQL = []
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM vw_sensorsdata "
                   "WHERE valuetype='Total Volatile Organic Compounds' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
    row = cursor.fetchone()

    dataSQL.append(list(row))
    labels = ['data']
    dff = pd.DataFrame.from_records(dataSQL, columns=labels)

    tvoc = dff.iat[0, 0]
    conn.close()
    return tvoc


def draw_graphScetter(name, parameter):
    dataSQL = []  # set an empty list
    X = deque(maxlen=20)
    Y = deque(maxlen=20)
    cursor.execute(
        "SELECT date_time,  valuetype, data, dimension FROM vw_sensorsdata WHERE valuetype = '%s' AND room = '208'  ORDER BY date_time DESC LIMIT 20" % parameter)
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['date_time', 'valuetype', 'data', 'dimension']
        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        dff = df[df['valuetype'] == parameter]
        X = dff['date_time']
        Y = dff['data']
        dim = dff['dimension'].unique()

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(title=go.layout.Title(text='{}, {}'.format(name, dim)),
                                                xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y) - 1, max(Y) + 1]))}


def draw_graphBar(name, parameter):
    query = "SELECT date_time,  data, dimension FROM vw_sensorsdata WHERE valuetype= '%s' AND room = '208' ORDER BY date_time DESC LIMIT 5000" % parameter
    dff = create_pandas_table(query)
    dim = dff['dimension'].unique()
    dff1 = dff.loc[:, ['date_time', 'data']]
    dff1['date_time'] = pd.to_datetime(dff1['date_time'])
    dff1['date'] = dff1['date_time'].dt.date
    data2 = dff1.groupby(['date']).mean()
    data = go.Bar(x=data2.index.map(str), y=list(data2['data']))
    return {'data': [data],
            'layout': go.Layout(title=go.layout.Title(text='Päevakeskmised: {}, {}'.format(name, dim)))}


@app.callback(dash.dependencies.Output('graph', 'figure'),
              [Input(component_id='indicator', component_property='value'),
               Input(component_id='dropDownList', component_property='value'),
               Input(component_id='datePickerId', component_property='start_date'),
               Input(component_id='datePickerId', component_property='end_date')])
def drawGraphBarAverage(parameter, dropDownList, startDate, endDate):
    query = "SELECT * FROM vw_sensorsdata WHERE room= '208' AND valuetype ='%s' AND date_time BETWEEN '%s' AND '%s' ORDER BY date_time DESC " % (
    parameter, startDate, endDate)
    # conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
    #               password="ruuvisel")
    cursor = conn.cursor()

    dataFrame = create_pandas_table(query)

    dim = dataFrame['dimension'].unique()
    dff2 = dataFrame.loc[:, ['date_time', 'data']]
    dff2['date_time'] = pd.to_datetime(dff2['date_time'])
    if dropDownList == 'Hour average':
        dff2['hours'] = dff2['date_time'].dt.hour
        dff2['dates'] = dff2['date_time'].dt.date
        data4 = dff2.groupby(['dates', 'hours'], as_index=False).mean()
        data4['dateAndHours'] = data4['dates'].astype(str).apply(
            lambda x: dt.datetime.strptime(x, '%Y-%m-%d')) + pd.to_timedelta(data4['hours'],
                                                                             unit='h')  # .astype(str)#.apply(lambda x: dt.datetime.strptime(x , '%H')).time()
        # dt.datetime.combine(dt.datetime.strptime(data4['dates'].astype(str), '%Y-%m-%d'), dt.time(data4['hours'], 0))
        # dt.datetime.strptime
        # data2Hours = data2['hours'].mean()
        data = go.Bar(x=list(data4['dateAndHours']), y=list(data4['data']))
    elif dropDownList == 'Day average':
        dff2['hours'] = dff2['date_time'].dt.hour
        dff2['dates'] = dff2['date_time'].dt.date
        data4 = dff2.groupby(['dates']).mean()
        data = go.Bar(x=data4.index.map(str), y=list(data4['data']))
        # data2Hours = data2['hours'].mean()
    elif dropDownList == 'Week average':
        dff2['weeks'] = dff2['date_time'].dt.week
        data4 = dff2.groupby(['weeks']).mean()
        # data4 = dff2.groupby(['dates']).mean()
        # data2Hours = data2['hours'].mean()
        data = go.Bar(x=data4.index.map(str), y=list(data4['data']))
    else:

        dff2['mounth'] = dff2['date_time'].dt.month
        data4 = dff2.groupby(['mounth']).mean()
        # data2Hours = data2['hours'].mean()
        data = go.Bar(x=data4.index.map(str), y=list(data4['data']))

    return {'data': [data],
            'layout': go.Layout(title=go.layout.Title(text=': {}, {}'.format(parameter, dim)))}


# @app.callback(Output(component_id='crossfilterParameterGraph', component_property='figure')
# [Input(component_id='firstParameter', component_property='value'),
# Input(component_id='secondParameter', component_property='value'),
# Input(component_id='startDateId', component_property='start_date'),
# Input(component_id='endDateId', component_property='end_date')]
#  )
# def updateGraphRatio(firstParameter, secondParameter, startDatePeriod, endDatePeriod)
# query = "SELECT date_time,  data, dimension FROM vw_sensorsdata WHERE valuetype= '%s' AND valuetype = '%s' AND date_time BETWEEN '%s' AND '%s' ORDER BY date_time DESC LIMIT 5000" % (firstParameter, secondParameter,startDatePeriod,endDatePeriod)

# dataFrame = create_pandas_table(query)

# return{
# 'data' :[go.Scatter()]
# }


if __name__ == '__main__':
    app.run_server(debug=True)

