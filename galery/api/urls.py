from django.urls import path, include
from rest_framework import routers
from api.views import PhotoView

from api.views import FavoriteView

router = routers.DefaultRouter()
router.register('photos', PhotoView)
router.register('favorites', FavoriteView)
urlpatterns = [
    path('', include(router.urls)),
    path('image/<int:pk>/tofav/', FavoriteView.as_view({'get': 'add_to_favorite'})),
    path('image/<int:pk>/removefav/', FavoriteView.as_view({'get': 'delete_from_favorite'})),
]
