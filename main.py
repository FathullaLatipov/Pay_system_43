from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/home')
async def home():
    return {'message': 'hello this is home'}
