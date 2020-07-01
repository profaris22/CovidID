import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('/home/arisw/Documents/covidDA/datacovid.csv')

fig=make_subplots(rows=3,cols=2,specs=[[{},{"rowspan":3}],[{},None],[{},None]],shared_xaxes=True,vertical_spacing=0.02,horizontal_spacing=0.05,y_title="Jumlah Kasus" )

fig.add_trace(go.Scatter(x=df['tanggal'],y=df['total_kasus'], name='Total Kasus',line=dict(color='blue')),row=1,col=2)
fig.add_trace(go.Scatter(x=df['tanggal'],y=df['total_sembuh'], name='Total Sembuh',line=dict(color='green')),row=1,col=2)
fig.add_trace(go.Scatter(x=df['tanggal'],y=df['total_kematian'], name='Total Meninggal',line=dict(color='red')),row=1,col=2)
fig.add_trace(go.Scatter(x=df['tanggal'],y=df['kasus_aktif'], name='Total Kasus Aktif ',line=dict(color='orange')),row=1,col=2)

fig.add_trace(go.Scatter(x=df['tanggal'],y=df['kasus_baru'], name='Kasus Baru ',fill='tozeroy'),row=3,col=1)
fig.add_trace(go.Scatter(x=df['tanggal'],y=df['kematian_baru'], name='Kematian Baru',fill='tonexty'),row=2,col=1)
fig.add_trace(go.Scatter(x=df['tanggal'],y=df['sembuh_baru'], name='Sembuh Baru',fill='tozeroy'),row=1,col=1)


fig.update_xaxes(title="Tanggal",row=1,col=2)
fig.update_xaxes(title="Tanggal",row=3,col=1)

fig.update_layout(title='Data Perkembangan Covid-19 di Indonesia',title_x=0.5,showlegend=True)

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(
    [dcc.Graph(figure=fig)]
)

app.run_server(debug=True)


