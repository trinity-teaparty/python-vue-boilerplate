# main.py

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config.settings import settings
from proxy.vue_proxy_middleware import VueProxyMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

templates.env.globals.update(settings=settings)

if settings.USE_BUNDLE_PROXY:
    app.add_middleware(VueProxyMiddleware, upstream=settings.FRONTEND_BUNDLE_PROXY_URL)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.jinja")

if __name__ == '__main__':
     uvicorn.run(
                "main:app",
                host='0.0.0.0',
                port=8000,
                workers=1,
                log_level='info',
                reload=True,
            )