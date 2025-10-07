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


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/odh-login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get('/more-about', response_class=HTMLResponse)
async def moreabout(request:Request):
    return templates.TemplateResponse("moreabout.html",{"request": request})

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
async def agencies(request: Request):
    return templates.TemplateResponse("agencies.html", {"request": request})

@app.get("/agencies-details", response_class=HTMLResponse)
async def agencies(request: Request):
    return templates.TemplateResponse("agenciesDetails.html", {"request": request})

@app.get("/odh-blogs", response_class=HTMLResponse)
async def blogs(request: Request):
    return templates.TemplateResponse("/blog.html", {"request": request})

@app.get("/odh-details-blog", response_class=HTMLResponse)
async def blogs(request: Request):
    return templates.TemplateResponse("blogDetails.html", {"request": request})

@app.get("/odh-contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contactus.html", {"request": request})

@app.get("/odh-team",response_class=HTMLResponse)
async def team(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})

@app.get("/career-with-odh", response_class=HTMLResponse)
async def career(request: Request):
    return templates.TemplateResponse("career.html", {"request": request})

@app.get("/odh-developers-gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request})

@app.get("/odh-faq", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})



@app.get('/odh-terms-conditions', response_class=HTMLResponse)
async def conditions(request:Request):
    return templates.TemplateResponse("terms.html",{"request": request})

@app.get('/odh-privacy-policy', response_class=HTMLResponse)
async def privacy(request:Request):
    return templates.TemplateResponse("privacy.html",{"request": request})


@app.get("/disclaimer", response_class=HTMLResponse)
async def disclaimer(request: Request):
    return templates.TemplateResponse("disclaimer.html", {"request": request})

