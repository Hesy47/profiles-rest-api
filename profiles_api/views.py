from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test ApiView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            "Uses HTTP methods as function: (get, post ,put, patch, delete).",
            "Is similar to a traditional Django view.",
            "Gives you the most control over your application logic",
            "IS mapped manually to your urls",
        ]
        return Response({"message": "welcome back Amir", "the_api": an_api_view})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello Mr {name}, welcome to your shopping panel"
            return Response({"message": message}, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handel updating an object"""
        return Response({"methods": "put"}, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        """Handel a partial update of an object"""
        return Response({"methods": "patch"}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"methods": "delete"}, status=status.HTTP_200_OK)
