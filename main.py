from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from routes import auth, blog, single_blog, personal_blog
from routes.update import router as update_router
from routes.delete import router as delete_router
from database import engine
import models, database

app = FastAPI()

templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )

@app.get("/auth")
def auth_page(request: Request):
    return templates.TemplateResponse(
        "auth.html",
        {"request": request}
    )

@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": "Gmail not found!"
        }
    )

@app.get("/admin")
def admin(request: Request, db: Session = Depends(database.get_db)):
    articles = db.query(models.Blogs).all()

    return templates.TemplateResponse(
        "admin.html",   
        {
            "request": request,
            "articles": articles
        }
    )

@app.post("/all")
def all_articles(request: Request, db: Session = Depends(database.get_db), title: str = Form(...), content: str = Form(...)):
    new_blog = models.Blogs(
        title=title,
        content=content
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return templates.TemplateResponse(
        "add.html",
        {
            "request": request
        }
    )

@app.get("/update")
def update(request: Request):

    return templates.TemplateResponse(
        "update.html",
        {
            "request": request
        }
    )

@app.get("/delete")
def delete(request: Request):

    return templates.TemplateResponse(
        "delete.html",
        {
            "request": request
        }
    )



app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(single_blog.router)
app.include_router(personal_blog.router)
app.include_router(update_router)
app.include_router(delete_router)