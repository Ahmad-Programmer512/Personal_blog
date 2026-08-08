from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database
import models

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/auth")
def personal_blog(request: Request, db: Session = Depends(database.get_db)):
    articles = db.query(models.Blogs).all()

    return templates.TemplateResponse(
        "blogs.html",
        {
            "request": request,
            "articles": articles
        }
    )