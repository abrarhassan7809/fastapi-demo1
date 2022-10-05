from fastapi import APIRouter, Depends, status
from f_blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from f_blog.repository import reposit_blog

router = APIRouter(prefix='/f_blog', tags=["Blogs"])

@router.get('/', response_model=list[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    return reposit_blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    return reposit_blog.create(db, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    return reposit_blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    return reposit_blog.update(id, db, request)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    return reposit_blog.show(id, db)
