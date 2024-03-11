from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/jokes/")
async def root(id=None):
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
        
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        jokes = data['data']
        return jokes
    else:
        return "Failed to fetch joke"

@app.get("/jokes/{id}/")
async def root(id=None):
    url = f"https://api.freeapi.app/api/v1/public/randomjokes/{int(id)}/"
        
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        joke = data['data']
        return joke
    else:
        return "Failed to fetch joke"