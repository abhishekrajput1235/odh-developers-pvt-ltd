from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Custom error handler
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "status_code": exc.status_code, "detail": exc.detail},
        status_code=exc.status_code,
    )

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/services", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

@app.get("/service-details",response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("servicesDetails.html",{"request": request})


@app.get("/odh-properties", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("/property.html", {"request": request})


@app.get("/properties-details", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("propertyDetails.html", {"request": request})

@app.get("/odh-agencies", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("agencies.html", {"request": request})

@app.get("/agencies-details", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("agenciesDetails.html", {"request": request})

@app.get("/odh-blogs", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("/blog.html", {"request": request})

@app.get("/odh-details-blog", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("blogDetails.html", {"request": request})

@app.get("/odh-contact", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("contactus.html", {"request": request})

@app.get("/odh-team",response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})

@app.get("/career-with-odh", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})