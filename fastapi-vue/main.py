# main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from proxy.vue_proxy_middleware import VueProxyMiddleware

app = FastAPI()

USE_VUE_BUNDLE = False


# product mode
if USE_VUE_BUNDLE:
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="templates")

    @app.get("/")
    async def home(request: Request):
        return templates.TemplateResponse("home.jinja", {"request": request})
    
# dev mode
else:
    app.add_middleware(VueProxyMiddleware, upstream="http://localhost:3000")

    @app.get("/")
    async def redirect_dev():
        return {"message": "Dev mode: frontend served by Vue dev server"}



if __name__ == '__main__':
     uvicorn.run(
                "main:app",
                host='0.0.0.0',
                port=8000,
                workers=1,
                log_level='info',
                reload=True,
            )