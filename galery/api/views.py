from django.http.response import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from api.serializers import PhotoSerializer
from photos.models import Photo

from photos.models import Favorite

from api.serializers import FavoriteSerializer


class PhotoView(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()


class FavoriteView(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user = request.user
        favorite, created = Favorite.objects.get_or_create(photo=photo, user=user)
        if created:
            return JsonResponse({'key': 'Добавлено в избранные'})
        else:
            favorite.delete()
            return JsonResponse({'key': 'Удалено из избранных'})
