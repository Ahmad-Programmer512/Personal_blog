from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)