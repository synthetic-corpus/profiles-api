from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # For HTTP status codes
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of API features """
        an_apiview = [
            "User HTTP methods to scud",
            "S is for select",
            "C is for create",
            'U is for update',
            'D is for delete',
        ]

        """ Django expects a Responce object, imported above """

        return Response({'message':'Hello!', 'an_apiview': an_apiview}) # Becomes a Json Object.
    
    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        """ How do you validate a serializer? use the is_valid() method """
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello (name)'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """ Updates an object """
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Partially Updates an object, by individul attribute """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Deletes an Object """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Returns a Hello message """
        """ What does a typical viewset do that APIview does not?"""

        a_viewset = [
            'Users Actions (list, create, retreivew, update, partail update',
            'Automatically maps to URLs via Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'Message':'hello','a_viewset':a_viewset})

    def create(self, request):
        """ create a new hello message. post request """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Retrieves an object. Get crequest. """
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """ Handles updating an object. Put request. """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ A Patch Request. """
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Handle removing an object a delete request. """
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfilesSerializer
    """ Query set here has List, Create, Update, Patch etc already set up """
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    """ Renderer classes allows the login to render on the default django page. """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading, and updating profile feed items! """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
