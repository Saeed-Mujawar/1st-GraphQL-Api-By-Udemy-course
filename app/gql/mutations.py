from graphene import ObjectType 
from app.gql.job.mutation import AddJob, DeleteJob, UpdateJob
from app.gql.employer.mutation import AddEmployer, UpdateEmployer, DeleteEmployer
from app.gql.user.mutation import LoginUser,AddUser,ApplyToJob


# By adding these mutation fields to the Mutation class, you're effectively exposing them 
#     in your GraphQL schema, making them accessible to clients through GraphQL queries.
class Mutation(ObjectType):
    add_job = AddJob.Field()
    update_job = UpdateJob.Field()
    delete_job = DeleteJob.Field()
    add_employer = AddEmployer.Field()
    update_employer = UpdateEmployer.Field()
    delete_employer = DeleteEmployer.Field()
    login_user = LoginUser.Field()
    add_user = AddUser.Field()
    apply_to_job = ApplyToJob.Field()

