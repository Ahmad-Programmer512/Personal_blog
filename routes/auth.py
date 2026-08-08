from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Blogs

router = APIRouter(prefix="/auth")
templates = Jinja2Templates(directory="templates")

@router.post("/")
def auth(request: Request, gmail: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):

    if gmail != "admin@gmail.com":
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Gmail not found!"
            }
        )

    if password != "admin":
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Wrong password!"
            }
        )

    articles = db.query(Blogs).order_by(Blogs.id).all()

    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "articles": articles
        }
    )