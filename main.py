import os
from typing import Annotated
from fastapi import FastAPI, File, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_URL = os.getenv("BASE_URL") or "http://localhost:8000"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    param_list = [
        "nu0407001-medios-de-pago-conteo-de-archivos",
        "nu0407001-medios-de-pago-validaciones",
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"param_list": param_list, "base_url": BASE_URL},
    )


@app.post("/params", name="params", response_class=HTMLResponse)
async def params(request: Request):
    print(request)
    return RedirectResponse(url="/")


@app.post("/uploadfile", name="upload-file")
async def upload_file(file: Annotated[bytes, File()]):
    file_content = file.decode("utf-8")
    return {"data": file_content}
