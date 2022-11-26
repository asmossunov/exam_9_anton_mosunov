from django.urls import path
from photos.views.photos import PhotoCreateView, PhotoView, PhotoUpdateView, PhotoDeleteView, FavoriteView
from photos.views.base import PhotosIndexView


urlpatterns = [
    path('photos/<int:pk>/create/', PhotoCreateView.as_view(), name='create_photo'),
    path('', PhotosIndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoView.as_view(), name='photo_detail'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photos/<int:pk>/confirm-delete/', PhotoDeleteView.as_view(), name='confirm_delete'),
    path('photos/<int:pk>/to-favorite/', FavoriteView.as_view(), name='to_favorite')

]
