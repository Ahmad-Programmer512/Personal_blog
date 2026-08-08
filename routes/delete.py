from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, database


router = APIRouter(
    prefix="/delete"
)

templates = Jinja2Templates(directory="templates")

@router.get("/{id}")
def delete(request: Request, id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()

    if blog is None:
        return {"message": "Blog not found"}

    db.delete(blog)
    db.commit()
    
    return templates.TemplateResponse(
        "delete.html",
        {
            "request": request
        }
    )