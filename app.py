from flask import Flask, request
from flask_graphql import GraphQLView
from models import session
from schema import schema

app = Flask(__name__)

class CustomGraphQLView(GraphQLView):
    def get_context(self):
        # You can override this method to provide a custom context
        return {'session': session}

app.add_url_rule(
    '/graphql',
    view_func=CustomGraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

if __name__ == '__main__':
    app.run(debug=True)
