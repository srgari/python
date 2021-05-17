#%%
import requests
import pandas as pd 
from plotly import graph_objs as go
import io 
# %%
#%%

req = requests.get('https://data.brasil.io/dataset/covid19/caso.csv.gz')

with open('lala.csv.gz', 'wb') as x:
    x.write(req.content)

#%%
df = pd.read_csv('lala.csv.gz')#[['date','state','confirmed','deaths']]
df2 = df.groupby(['date','state'])['confirmed','deaths'].sum()
df2
# %%
df_sp = df2.query("state == 'SP'")
df_sp.reset_index(inplace = True)
df_sp
# %%
fig = go.Figure(data = go.Bar(y = df_sp.deaths.values,
                    text =  [f'dia: {x}; mortes: {y}' for x,y in zip(df_sp.date.values,df_sp.deaths.values)],
                    hoverinfo = 'text'
                   ))
                   

fig.update_layout(
    title = 'Mortes em sp',
    xaxis = dict(
        tickmode = 'array',
        tickvals = list(range(1,len(df_sp),10)),
        ticktext = df_sp.date.values[1:len(df_sp):10]  ))


    
#%%
fig.write_html('covid_sp_deaths.html', auto_open=True)
# %%
df_sp


# %%

# %%
