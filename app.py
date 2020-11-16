from flask import Flask
from flask_graphql import GraphQLView as View
from database import db_session
from graph_ql.schema import schema


app = Flask(__name__)
app.debug = True
app.add_url_rule("/", view_func=View.as_view("graphql", graphiql=True, schema=schema))


@app.teardown_appcontext
def shutdown_session():
    db_session.remove()


def main():
    app.run()


if __name__ == "__main__":
    main()