from mud.models import User
from rest_framework import viewsets, permissions
from .serializers import MudSerializer

# Client Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MudSerializer
