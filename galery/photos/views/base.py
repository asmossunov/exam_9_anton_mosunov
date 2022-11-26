from django.views.generic import ListView
from photos.models import Photo


class PhotosIndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhotosIndexView, self).get_context_data(object_list=object_list, **kwargs)
        user = self.request.user
        photos = Photo.objects.filter(is_deleted=False).order_by('-created_at')
        print(photos)
        context['photos'] = photos
        return context



