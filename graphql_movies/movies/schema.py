import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from . models import CreateList

class CreateListType(DjangoObjectType):
    class Meta:
        model = CreateList


# Create a Query type
class Query(ObjectType):
    createlist = graphene.Field(CreateListType, id=graphene.Int())
    createlists = graphene.List(CreateListType)

    def resolve_createlist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return CreateList.objects.get(pk=id)

        return None

    def resolve_createlist(self, info, **kwargs):
        return CreateList.objects.all()




schema = graphene.Schema(query=Query)