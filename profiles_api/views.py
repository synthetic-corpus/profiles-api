from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # For HTTP status codes
from rest_framework import viewsets

from profiles_api import serializers


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
        """ create a new hello message """
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
        """ Retrieves an object """
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """ Handles updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Deletes an Object """
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Handle removing an object """
        return Response({'http_method': 'DELETE'})
