from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

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

        return Response({'message':'Hello!', 'an_apiview': an_apiview}) # Becomse a Json Object.