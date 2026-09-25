import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('../outputs/cleaned_flights.csv')

app = dash.Dash(__name__)
app.title = "Airline Delay Dashboard"

carriers = sorted(df['AIRLINE'].dropna().unique())

app.layout = html.Div(className='dashboard-container', children=[
    html.H1("✈️ Airline Delay & Operations Dashboard"),

    html.Div(className='filters', children=[
        dcc.Dropdown(id='carrier-filter', options=[{'label': c, 'value': c} for c in carriers],
                     multi=True, placeholder="Filter by Carrier"),
        dcc.RangeSlider(id='month-filter', min=1, max=12, step=1, value=[1, 12],
                         marks={i: str(i) for i in range(1, 13)}),
    ]),

    html.Div(className='kpi-row', id='kpi-cards'),

    html.Div(className='chart-row', children=[
        dcc.Graph(id='delay-cause-chart'),
        dcc.Graph(id='seasonal-chart'),
    ]),
    html.Div(className='chart-row', children=[
        dcc.Graph(id='carrier-chart'),
        dcc.Graph(id='route-chart'),
    ]),
])


@app.callback(
    [Output('kpi-cards', 'children'),
     Output('delay-cause-chart', 'figure'),
     Output('seasonal-chart', 'figure'),
     Output('carrier-chart', 'figure'),
     Output('route-chart', 'figure')],
    [Input('carrier-filter', 'value'),
     Input('month-filter', 'value')]
)
def update_dashboard(selected_carriers, month_range):
    dff = df[(df['MONTH'] >= month_range[0]) & (df['MONTH'] <= month_range[1])]
    if selected_carriers:
        dff = dff[dff['AIRLINE_NAME'].isin(selected_carriers)]

    total_flights = len(dff)
    on_time_pct = (dff['ARR_DELAY'] <= 15).mean() * 100
    avg_delay = dff['ARR_DELAY'].mean()

    kpis = [
        html.Div(className='kpi-card', children=[html.H3(f"{total_flights:,}"), html.P("Total Flights")]),
        html.Div(className='kpi-card', children=[html.H3(f"{on_time_pct:.1f}%"), html.P("On-Time %")]),
        html.Div(className='kpi-card', children=[html.H3(f"{avg_delay:.1f} min"), html.P("Avg Delay")]),
    ]

    delay_cols = ['DELAY_DUE_CARRIER', 'DELAY_DUE_WEATHER', 'DELAY_DUE_NAS', 'DELAY_DUE_SECURITY', 'DELAY_DUE_LATE_AIRCRAFT']
    delay_fig = px.bar(x=dff[delay_cols].sum().values, y=delay_cols, orientation='h',
                        title='Delay by Cause', template='plotly_dark')

    seasonal_fig = px.line(dff.groupby('MONTH')['ARR_DELAY'].mean().reset_index(),
                            x='MONTH', y='ARR_DELAY', title='Avg Delay by Month', template='plotly_dark')

    carrier_fig = px.bar(dff.groupby('AIRLINE')['ARR_DELAY'].mean().sort_values().reset_index(),
                          x='ARR_DELAY', y='AIRLINE', orientation='h',
                          title='Avg Delay by Carrier', template='plotly_dark')

    dff = dff.copy()
    dff['ROUTE'] = dff['ORIGIN'] + ' → ' + dff['DEST']
    top_routes = dff.groupby('ROUTE')['ARR_DELAY'].mean().sort_values(ascending=False).head(10).reset_index()
    route_fig = px.bar(top_routes, x='ARR_DELAY', y='ROUTE', orientation='h',
                        title='Top 10 Delayed Routes', template='plotly_dark')

    return kpis, delay_fig, seasonal_fig, carrier_fig, route_fig


if __name__ == '__main__':
    app.run(debug=True)
