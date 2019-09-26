from mud.models import User, Room
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, RoomSerializer

# Client Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all().order_by('id')
