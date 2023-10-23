#https://fastapi.tiangolo.com/tutorial/first-steps/
# pip install fastapi
#%%
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'message':'hello world!'}
# %%
