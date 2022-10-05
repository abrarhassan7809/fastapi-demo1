from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get('/f_blog')
def create_blog(blog: Blog):
    return {'data': f'f_blog is create with title as {blog.title}'}
