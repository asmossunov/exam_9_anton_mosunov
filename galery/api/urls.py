from django.urls import path, include
from rest_framework import routers
from api.views import PhotoView

from api.views import FavoriteView

router = routers.DefaultRouter()
router.register('photos', PhotoView)
router.register('favorites', FavoriteView)
urlpatterns = [
    path('', include(router.urls)),
]
