#%%
#### highly experimental at this point
#### dropping all custom functions and name == __main__ stuff
#### just wanna see if it works

import sqlite3
import pandas as pd 

conn = sqlite3.connect('teste_sqlite_pandas.db')
#%%
### parte 1: adicionando tabelas via pandas - via preferencial
import pandas as pd 
import numpy as np 

df = pd.DataFrame({'lala':np.random.choice([pd.NA, pd.NA, 2],10),
                    'lele': np.random.choice([pd.NA, 'fafa','fefe','fifi'],10)})

#%%
df.to_sql(name = 'pandas_created_table', con = conn, if_exists = 'replace')

# %%

### parte 2: adicionando tabelas via query - via secundária

cursor = conn.cursor()
cursor.execute('CREATE TABLE sql_created_table (id integer PRIMARY_KEY)')
# %%
