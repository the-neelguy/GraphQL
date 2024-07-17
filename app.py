from flask import Flask, request
from graphene import Schema
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable the GraphiQL UI
    )
)

if __name__ == '__main__':
    app.run(debug=True)
