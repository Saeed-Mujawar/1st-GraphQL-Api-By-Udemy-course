from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler 
from app.db. models import Base, Employer, Job
from app.db.database import engine,prepare_database, Session
from app. gql.queries import Query
from app.gql.mutations import Mutation


schema = Schema(query=Query, mutation= Mutation)

app = FastAPI()

Base.metadata.create_all(engine)

@app.on_event("startup")
def startup_event():
    prepare_database()
    
# @app.on_event("/employer")
# def get_employer():
#     session = Session()
#     employers = session.query(Employer).all()
#     session.close()
#     return employers

# @app.get("/jobs")
# def get_jobs():
#     with Session() as session:
#         return session.query(Job).all()    

app.mount("/", GraphQLApp(
    schema=schema,
    on_get = make_playground_handler()
    ))


