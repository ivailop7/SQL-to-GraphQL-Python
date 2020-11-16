import graphene
from graph_ql.query import Query
from graph_ql.mutation import Mutation
from graph_ql.typedefs import Students, Classes, Teachers, Grades


schema = graphene.Schema(
    query=Query, mutation=Mutation, types=[Students, Teachers, Classes, Grades]
)
