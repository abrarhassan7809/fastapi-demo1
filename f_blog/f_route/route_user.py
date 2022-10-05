from fastapi import APIRouter, Depends
from f_blog import database, schemas
from sqlalchemy.orm import Session
from f_blog.repository import reposit_user

router = APIRouter(prefix='/user', tags=["Users"])

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):

    return reposit_user.create_all(db, request)

@router.get('/', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):

    return reposit_user.show(id, db)
