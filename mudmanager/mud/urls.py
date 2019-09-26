from rest_framework import routers
from .api import UserViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, "mud_user")
router.register('api/room', RoomViewSet, "mud_room")

urlpatterns = router.urls
