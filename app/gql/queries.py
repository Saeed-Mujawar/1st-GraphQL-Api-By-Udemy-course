
from graphene import ObjectType, List, Field, Int

from app.gql.types import JobObject, EmployerObject, UserObject, JobApplicationObject
from app.db.database import Session
from app.db.models import Job, Employer, User,JobApplication
from sqlalchemy.orm import joinedload

class Query(ObjectType):
    jobs = List(JobObject)
    job = Field(JobObject, id = Int(required = True))
    employers = List(EmployerObject)
    employer = Field(EmployerObject, id = Int(required = True))
    users = List(UserObject)
    job_applications = List(JobApplicationObject)

    @staticmethod
    def resolve_job_applications(root, info):
        return Session().query(JobApplication).all()

    @staticmethod
    def resolve_users(root, info):
        return Session().query(User).all()

    @staticmethod
    def resolve_job(root, info, id):
        # session = Session()
        # job = session.query(Job).filter(Job.id == id).first()
        # session.close()
        # return job
        # same code below
        return Session().query(Job).filter(Job.id == id).first()
    
    @staticmethod
    def resolve_jobs(root, info):
        return Session().query(Job). all()
        # return Session().query(Job).options(joinedload(Job.employer)).all()

    @staticmethod
    def resolve_employer(root, info, id):
        return Session().query(Employer).filter(Employer.id == id).first()


    @staticmethod
    def resolve_employers(root, info):
        return Session().query(Employer). all()