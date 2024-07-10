from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models


class HelloApiView(APIView):
    """Test ApiView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            "Uses HTTP methods as function: (get, post, put, patch, delete).",
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


class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_view_set = [
            "Uses actions: (list, create, retrieve, update, partial_update, destroy).",
            "Automatically maps to URLs by using routers",
            "Provides more functionality with less code",
        ]
        return Response({"message": "Hello Amir", "the_view_set": a_view_set})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello Mr {name}, welcome to your Admin panel"
            return Response({"message": message}, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handel getting a object by it id"""
        return Response({"http_method": "GET"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Handel updating a object by it id"""
        return Response({"http_method": "PUT"}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """Handel updating a part of the object by it id"""
        return Response({"http_method": "PATCH"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        """Handel removing a object by it id"""
        return Response({"http_method": "DELETE"}, status=status.HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    """Handel creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
