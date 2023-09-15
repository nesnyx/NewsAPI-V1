from fastapi import FastAPI, Request, Form,HTTPException
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests


app = FastAPI(title='News')
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

apiKey = 'YOUR API KEY'

def get_api(apiKey):
    base_url = f"https://newsapi.org/v2/everything?q=Apple&apiKey={apiKey}"
    response = requests.get(base_url)
    data = response.json()
    return data
    

@app.get('/')
async def index(request : Request):
    data = get_api(apiKey)
    return templates.TemplateResponse('index.html', {
        'request' :request,
        'data' : data,
        'title' : 'NewsAPI'
    })

@app.post('/hasil')
async def read_item(request : Request, news:str= Form(...)):
    base_url = f"https://newsapi.org/v2/everything?q={news}&apiKey={apiKey}"
    response = requests.get(base_url)
    data = response.json()['articles']
    
    return templates.TemplateResponse('hasil.html', {
        'request': request,
        'data' : data
    })

@app.get('/about')
async def about(request:Request):
    return templates.TemplateResponse("about.html", {
        'request':request
    })