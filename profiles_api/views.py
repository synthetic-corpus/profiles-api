from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # For HTTP status codes

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