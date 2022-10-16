from django.shortcuts import render

from core.models import Recipe
from .serializers import RecipeSerializer
from .permissions import UpdateMyRecipesPermissions

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class RecipeApiViewset(ModelViewSet):
    """
    Handles All Recipe API requests.
    User has to be authenticated to create update and delete.
    User can only update and delete the recipes they have created.
    """
    queryset = Recipe.objects.all()#Users can GET all recipes
    serializer_class = RecipeSerializer

    #User has to be authenticated to create. They can only update their own recipes
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateMyRecipesPermissions]

    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = [
        'recipe_title',
        'cuisine'
        ]

    def perform_create(self, serializer):
        """
        Creates a recipe instance with 'user'= the user that makes the request.
        Automatically GETS the token authenticated user.
        """
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        """
        Updates a recipe instance with 'user'= the user that makes the request.
        Automatically GETS the token authenticated user.
        """
        instance = serializer.save(user=self.request.user)
        return instance


class MyRecipesApiViewset(ModelViewSet):
    """
    Handles My Recipe API requests.
    User has to be authenticated and can only GET their own recipes.
    User has to be authenticated to create update and delete.
    User can only update and delete the recipes they have created.
    """

    serializer_class = RecipeSerializer
    permission_classes = [UpdateMyRecipesPermissions]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]

    search_fields = [
        'recipe_title',
        'cuisine'
        ]

    def get_queryset(self):
        """
        The queryset is modified to only look for the recipes
        the user has created
        """
        query = Recipe.objects.filter(user=self.request.user)
        return query

    def perform_create(self, serializer):
        """
        Creates a recipe instance with 'user'= the user that makes the request.
        Automatically GETS the token authenticated user.
        """
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        """
        Updates a recipe instance with 'user'= the user that makes the request.
        Automatically GETS the token authenticated user.
        """
        instance = serializer.save(user=self.request.user)
        return instance