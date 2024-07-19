import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Students as StudentModel

class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_students = SQLAlchemyConnectionField(Students.connection)
    student = graphene.Field(Students, id=graphene.Int())

    def resolve_all_students(self, info, **args):
        query = Students.get_query(info)
        return query.all()
    
    def resolve_student(self, info, id):
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
        session = info.context['session']
        session.add(student)
        session.commit()
        return CreateStudent(student=student)
    
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
