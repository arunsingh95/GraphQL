import graphene
from graphene_django import DjangoObjectType
from graphQL.models import UserDetails


class UserDetailType(DjangoObjectType):
    class Meta:
        model = UserDetails


class Query(graphene.ObjectType):
    user_details = graphene.List(UserDetailType)

    def resolve_user_details(self, info, **kwargs):
        return UserDetails.objects.all()
