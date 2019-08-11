import graphene

import django_graphql.core.schema


class Query(django_graphql.core.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
