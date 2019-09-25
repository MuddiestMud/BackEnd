from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/mud', UserViewSet, "mud")

urlpatterns = router.urls
