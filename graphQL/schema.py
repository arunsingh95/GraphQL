import graphene
from graphene_django import DjangoObjectType
from graphQL.models import UserDetails, Location


class UserDetailType(DjangoObjectType):
    class Meta:
        model = UserDetails


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class Query(graphene.ObjectType):
    user_details = graphene.List(UserDetailType)
    location = graphene.List(LocationType)

    def resolve_user_details(self, info, **kwargs):
        return UserDetails.objects.all()

    def resolve_location(self, info, **kwargs):
        return Location.objects.select_related('userDetails').all()
