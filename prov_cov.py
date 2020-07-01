import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('/home/arisw/Documents/covidDA/data_prov.csv')

fig=make_subplots(rows=2,cols=2,shared_xaxes=True,vertical_spacing=0.02,horizontal_spacing=0.05,y_title="Jumlah Kasus" )

fig.add_trace(go.Bar(
            x=df.provinsi,
            y=df.total_kasus,
            name='total kasus'),row=1,col=1)

fig.add_trace(go.Bar(
            x=df.provinsi,
            y=df.sembuh,
            name='total sembuh'),row=1,col=2)

fig.add_trace(go.Bar(
            x=df.provinsi,
            y=df.meninggal,
            name='total meninggal'),row=2,col=1)

fig.add_trace(go.Bar(
            x=df.provinsi,
            y=df.kasus_aktif,
            name='total kasus aktif'),row=2,col=2)

fig.update_layout(title='Data Covid-19 Provinsi di Indonesia',title_x=0.5,showlegend=True)


fig.show()