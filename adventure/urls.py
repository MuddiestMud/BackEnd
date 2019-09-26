from django.conf.urls import url
from . import api
'''
from rest_framework import routers

router = routers.DefaultRouter()
router.register('room', api.getroom, 'room')
router.register('rooms', api.getallrooms, 'allrooms')
router.register('init', api.initialize, "initialize")
router.register('move', api.move, "move")
router.register('say', api.say, "say")

urlpatterns = router.urls
'''
urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('getroom', api.getroom),
    url('getallrooms', api.getallrooms)
]
