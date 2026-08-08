from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from routes.blog import get_article
import database, models

router = APIRouter(
    prefix="/blogs"
)

templates = Jinja2Templates(directory="templates")

@router.get("/{id}")
def single(request: Request, id: int, db: Session = Depends(database.get_db)):
    query = db.query(models.Blogs).get(id)

    if query is None:
        return {"message": "query not found."}

    return templates.TemplateResponse(
        "single_blog.html",
        {
            "request": request,
            "article": query
        }
    )   

    return query