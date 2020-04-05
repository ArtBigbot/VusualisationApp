import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import random
from collections import deque
from dash.dependencies import Output, Input
import plotly
import plotly.graph_objs as go
import dash_daq as daq
import psycopg2
import sys, os
import numpy as np
import pandas.io.sql as psql
import matplotlib.pyplot as plt
from matplotlib import units

conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel", password="ruuvisel")
cursor = conn.cursor()
query = "SELECT * FROM vw_sensorsdata ORDER BY date_time DESC LIMIT 20"


def create_pandas_table(query, database=conn):
    table = pd.read_sql_query(query, database)
    return table


df = create_pandas_table(query)
available_indicators = df['valuetype'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

query = "SELECT * FROM vw_sensorsdata WHERE valuetype='T' ORDER BY date_time DESC LIMIT 10000"
data = create_pandas_table(query)
data1 = data.loc[:, ['date_time', 'data']]
import datetime

data1['date_time'] = pd.to_datetime(data1['date_time'])
data1['kuupaev'] = data1['date_time'].dt.date
data2 = data1.groupby(['kuupaev']).mean()
tepeture = data1['data']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app1 = dash.Dash(__name__, assets_folder='assets', include_assets_files=True)
server = app.server
theme = {
    'dark': True,
    'detail': '007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}
app.layout = html.Div([

    html.H4('dbhitsa2019'),
    dcc.Interval(
        id='update',
        interval=1 * 60000),
dcc.Tabs([
    dcc.Tab(label='Tab one', children=[
        html.Div([
            # 'gauges',
            html.Div([

                daq.Gauge(
                    showCurrentValue=True,
                    id='temptureGauge',
                    color="#9B51E0",
                    value=3,
                    label='temperatuur',
                    min=0,
                    max=50,
                    size=170,
                    theme='dark',
                    style={'display': 'block'}
                ),
            ], style={'position': 'absolute', 'top': '20%', 'width': '200px',  'height': '250px', 'border': '3px solid #73AD21'}),
            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='humidityGauge',
                          units="MPH",
                          value=5,
                          color="#9B51E0",
                          label='niiskus',
                          max=70,
                          min=0,
                          size=170,
                          style={'display': 'block'})
            ], style={'position': 'absolute', 'top': '52.5%', 'width': '200px', 'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='lumenGauge',
                          units="MPH",
                          color="#9B51E0",
                          value=5,
                          label='Lumen',
                          max=1000,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '20%', 'left': '12.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='ultravioletGauge',
                          units="MPH",
                          color="#9B51E0",
                          value=5,
                          label='Ultraviolet index',
                          max=1,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '52.5%', 'left': '12.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='IlluminanceGauge',
                          units="MPH",
                          color="#9B51E0",

                          label='Illuminance',
                          max=100,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '85%', 'left': '12.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='TotalVoletileOrganicCompoundsGauge',
                          units="MPH",
                          color="#9B51E0",

                          label='TotalVoletileOrganicCompounds',
                          max=10,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '20%', 'left': '24.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='detsibellGauge',
                          units="MPH",
                          color="#9B51E0",

                          label='Detsibell',
                          max=200,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '52.5%', 'left': '24.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='CarbonDioxideEquivalentCO2Gauge',
                          units="MPH",
                          color="#9B51E0",

                          label='CO2',
                          max=1,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '85%', 'left': '24.5%', 'rigth': '80%', 'width': '200px',
                      'height': '250px', 'border': '3px solid #73AD21'}),

            html.Div([
                daq.Gauge(showCurrentValue=True,
                          id='PirOn',
                          units="MPH",
                          color="#9B51E0",
                          value=0.2,
                          label='PIR on',
                          max=1,
                          min=0,
                          size=170)
            ], style={'position': 'absolute', 'top': '85%', 'width': '200px',  'height': '250px', 'border': '3px solid #73AD21'}),

        ]),
    ]),


    #html.Div([
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
                ], style={'display': 'inline-block', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%'}),  # animate=True
                #],
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
            ], style={'display': 'inline-block', 'height': '15%', 'width': '30%', 'top': '700%', 'left': '330%', 'right': '20%', 'border': '3px solid #73AD21'}),
            #], style={'padding': '120px 20px 20px 20px', })
        ])
    ])
])


@app.callback(dash.dependencies.Output('graphTempeture', 'figure'),
                [dash.dependencies.Input('graph_type_tempeture', 'value'),])
def update_graph_tempeture(graph_type_tempeture):


    if graph_type_tempeture == 'Aegsel':
            return draw_graphScetter('Temperatuur','T')
    elif graph_type_tempeture == 'Päevakeskmine':
            return draw_graphBar('Temperatuur','T')


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
        return draw_graphScetter('Niiskus','Humidity')
    elif graph_type_tvoc == 'Päevakeskmine':
        return draw_graphBar('Niiskus','Humidity')

@app.callback(dash.dependencies.Output('graphUltraVioletIndex', 'figure'),
             [dash.dependencies.Input('graph_type_ultra_violetindex', 'value'), ])
def update_graph_humidity(graph_type_ultra_violetindex):
    if graph_type_ultra_violetindex == 'Aegsel':
        return draw_graphScetter('Ultraviolet indeks','Ultraviolet index')
    elif graph_type_ultra_violetindex == 'Päevakeskmine':
        return draw_graphBar('Ultraviolet indeks','Ultraviolet index')

@app.callback(dash.dependencies.Output('graphDetsibel', 'figure'),
             [dash.dependencies.Input('graph_type_detsibel', 'value'), ])
def update_graph_detsibell(graph_type_detsibel):
    if graph_type_detsibel == 'Aegsel':
        return draw_graphScetter('Destibell','Detsibell')
    elif graph_type_detsibel == 'Päevakeskmine':
        return draw_graphBar('Destibell','Detsibell')

@app.callback(dash.dependencies.Output('graphIlluminance', 'figure'),
             [dash.dependencies.Input('graph_type_illuminance', 'value'), ])
def update_graph_detsibell(graph_type_illuminance):
    if graph_type_illuminance == 'Aegsel':
        return draw_graphScetter('Illuminatsioon', 'Illuminance')
    elif graph_type_illuminance == 'Päevakeskmine':
        return draw_graphBar('Illuminatsioon', 'Illuminance')

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


def update_table(input_data):
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()
    query = "SELECT * FROM vw_sensorsdata ORDER BY date_time DESC LIMIT 20"

    def create_pandas_table(query, database=conn):
        table = pd.read_sql_query(query, database)
        return table

    df = create_pandas_table(query)
    return df.to_dict('records')


@app.callback(
   dash.dependencies.Output('temptureGauge', 'value'),
    [dash.dependencies.Input('update', 'n_intervals')]
 )
def update_GaugeTemp(value):
    # return value
        dataSQL = []
        conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                                password="ruuvisel")
        cursor = conn.cursor()
        cursor.execute("SELECT  data FROM vw_sensorsdata WHERE valuetype ='T' AND room = '208' ORDER BY date_time DESC LIMIT 1")
        row = cursor.fetchone()

        dataSQL.append(list(row))
        labels = ['data']
        dff = pd.DataFrame.from_records(dataSQL, columns=labels)

        tempeture = dff.iat[0,0]
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
        cursor.execute("SELECT  data FROM vw_sensorsdata WHERE valuetype ='Humidity' AND room = '208' ORDER BY date_time DESC LIMIT 1")
        row = cursor.fetchone()

        dataSQL.append(list(row))
        labels = ['data']
        dff = pd.DataFrame.from_records(dataSQL, columns=labels)

        tempeture = dff.iat[0,0]
        conn.close()
        return tempeture


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
        cursor.execute("SELECT  data FROM vw_sensorsdata WHERE valuetype ='Lumen' AND room = '208' ORDER BY date_time DESC LIMIT 1")
        row = cursor.fetchone()

        dataSQL.append(list(row))
        labels = ['data']
        dff = pd.DataFrame.from_records(dataSQL, columns=labels)

        tempeture = dff.iat[0,0]
        conn.close()
        return tempeture


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

        tempeture = dff.iat[0,0]
        conn.close()
        return tempeture

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

        piron = dff.iat[0,0]
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
                       "WHERE valuetype='Illuminance' AND room = '208'  ORDER BY date_time  DESC LIMIT 1")
        row = cursor.fetchone()

        dataSQL.append(list(row))
        labels = ['data']
        dff = pd.DataFrame.from_records(dataSQL, columns=labels)

        illuminance = dff.iat[0,0]
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

        co2 = dff.iat[0,0]
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

        detsibell = dff.iat[0,0]
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

        tvoc = dff.iat[0,0]
        conn.close()
        return tvoc

def draw_graphScetter(name, parameter):
    dataSQL = []  # set an empty list
    X = deque(maxlen=20)
    Y = deque(maxlen=20)

    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()

    cursor.execute("SELECT date_time,  valuetype, data, dimension FROM vw_sensorsdata WHERE valuetype = '%s' AND room = '208'  ORDER BY date_time DESC LIMIT 20" % parameter)
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


def draw_graphBar(name,parameter):
    query = "SELECT date_time,  data, dimension FROM vw_sensorsdata WHERE valuetype= '%s' AND room = '208' ORDER BY date_time DESC LIMIT 5000" % parameter
    conn = psycopg2.connect(host="dev.vk.edu.ee", port=5432, database="dbhitsa2019", user="ruuvi_sel",
                            password="ruuvisel")
    cursor = conn.cursor()

    dff = create_pandas_table(query)

    dim = dff['dimension'].unique()
    dff1 = dff.loc[:, ['date_time', 'data']]
    dff1['date_time'] = pd.to_datetime(dff1['date_time'])
    dff1['date'] = dff1['date_time'].dt.date
    data2 = dff1.groupby(['date']).mean()
    data = go.Bar(x=data2.index.map(str), y=list(data2['data']))
    return {'data': [data],
            'layout': go.Layout(title=go.layout.Title(text='Päevakeskmised: {}, {}'.format(name, dim)))}



if __name__ == '__main__':
    app.run_server(debug=True)

