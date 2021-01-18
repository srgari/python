#%%
#### highly experimental at this point
#### dropping all custom functions and name == __main__ stuff
#### just wanna see if it works

import sqlite3
import pandas as pd 

conn = sqlite3.connect('teste_sqlite_pandas.db')
cursor = conn.cursor()
#%%
import pandas as pd 
import numpy as np 

df = pd.DataFrame({'lala':np.random.choice([pd.NA, pd.NA, 2],10),
                    'lele': np.random.choice([pd.NA, 'fafa','fefe','fifi'],10)})

#%%
df.to_sql(name = 'lala', con = conn, if_exists = 'replace')

# %%
