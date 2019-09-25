from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, "mud_user")

urlpatterns = router.urls
