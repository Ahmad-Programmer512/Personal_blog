from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database
import models

router = APIRouter(
    prefix="/update"
)

templates = Jinja2Templates(directory="templates")


# GET → show the update form
@router.get("/{id}")
def update_page(
    request: Request,
    id: int,
    db: Session = Depends(database.get_db)
):
    blog = db.query(models.Blogs).filter(
        models.Blogs.id == id
    ).first()

    if blog is None:
        return {"message": "Blog not found"}

    return templates.TemplateResponse(
        "update.html",
        {
            "request": request,
            "blog": blog
        }
    )


@router.post("/{id}")
def update_blog(request: Request, id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(database.get_db)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()

    if blog is None:
        return {"message": "Blog not found"}

    blog.title = title
    blog.content = content

    db.commit()
    db.refresh(blog)

    return templates.TemplateResponse(
        "update.html",
        {
            "request": request,
            "blog": blog
        }
    )