from fastapi import FastAPI
from f_blog import models
from f_blog.database import engine
from f_blog.f_route import route_blog, route_user, authentication
 
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(route_blog.router)
app.include_router(route_user.router)
