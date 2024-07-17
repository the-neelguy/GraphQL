import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Students as StudentModel, session

class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel

class Query(graphene.ObjectType):
    all_students = SQLAlchemyConnectionField(Students.connection)
    student = graphene.Field(Students, id=graphene.Int())
    
    def resolve_all_students(self, info):
        query = Students.get_query(info)
        return query.all()
    
    def resolve_user(self, info, id):
        query = Students.get_query(info)
        return query.get(id)

class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        emailid = graphene.String()
        contact = graphene.Int()
    
    student = graphene.Field(lambda: Students)
    
    def mutate(self, info, name, age, emailid, contact):
        student = StudentModel(name=name, age=age, emailid=emailid, contact=contact)
        session.add(student)
        session.commit()
        return CreateStudent(student=student)
    
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
