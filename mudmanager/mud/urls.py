from rest_framework import routers
from .api import UserViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, "mud_user")
router.register('room', RoomViewSet, "mud_room")

urlpatterns = router.urls
