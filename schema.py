import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import User as UserModel, session

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    all_users = SQLAlchemyConnectionField(User.connection)
    user = graphene.Field(User, id=graphene.Int())

    def resolve_all_users(self, info):
        query = User.get_query(info)
        return query.all()
 
    def resolve_user(self, info, id):
        query = User.get_query(info)
        return query.get(id)

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(self, info, name, age, email):
        user = UserModel(name=name, age=age, email=email)
        session.add(user)
        session.commit()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
