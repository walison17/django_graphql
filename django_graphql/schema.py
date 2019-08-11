import graphene

import django_graphql.core.schema


class Query(django_graphql.core.schema.Query, graphene.ObjectType):
    pass


class Mutation(django_graphql.core.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
