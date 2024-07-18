from flask import Flask, request
from flask_graphql import GraphQLView
from schema import schema
from models import session

app = Flask(__name__)
app.debug=True

def context_factory():
    return {'session': session}

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,  # Enable the GraphiQL UI
        context_value = context_factory,
    )
)

if __name__ == '__main__':
    app.run()
