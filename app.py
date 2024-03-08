from fastapi import FastAPI,Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Jinja2 template
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("home.html", {"request": dict()})

@app.get("/project", response_class=HTMLResponse)
async def get_project_form(request: Request):
    return templates.TemplateResponse("project_info.html", {"request": request})


@app.post("/submit_project_info", response_class=HTMLResponse)
async def process_form_data(request: Request, form_data: dict = Form(...)):
    # Convert form data to a dictionary (if not already)
    data_dict = await request.form()
    data_dict = dict(data_dict)
    # Render the template with the form data
    return templates.TemplateResponse("sections.html", {"request": request, "form_data": data_dict})




