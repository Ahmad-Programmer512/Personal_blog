from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database, models

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/new_blog")
def new_blog(request: Request):
    return templates.TemplateResponse(
        "new_blog.html",
        {"request": request}
    )

@router.post("/blog")
def create_blog(request: Request, title: str = Form(...), content: str = Form(...), db: Session = Depends(database.get_db) ):
    new_article = models.Blogs(
        title=title,
        content=content
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return templates.TemplateResponse(
        "new_blog.html",
        {
            "request": request,
            "message": "Blog published successfully!"
        }
    )

@router.get("/blogs")
def get_article(request: Request, db: Session = Depends(database.get_db)):

    articles = db.query(models.Blogs).all()


    return templates.TemplateResponse(
        "blogs.html",
        {
            "request": request,
            "articles": articles
        }
    )