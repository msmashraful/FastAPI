from fastapi import FastAPI

app = FastAPI()

@app.get('/')

async def root():
    return{
        "message": "<h1>Helloo world</h1>"
    }

@app.get('/user')

async def user():
    return{
        "id": 1,
        "name": "ashraf",
        "email": "msmashraful@gmail.com"
        
    }