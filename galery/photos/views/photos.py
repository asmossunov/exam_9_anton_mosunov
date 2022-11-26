from django.views.generic import CreateView, View, FormView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,  PermissionRequiredMixin, UserPassesTestMixin



from photos.forms import PhotoForm
from photos.models import Photo

from photos.models import Favorite


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_photo.html'
    form_class = PhotoForm
    model = Photo

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_id = self.kwargs['pk']
            post = form.save()
            return redirect('profile', pk=self.kwargs['pk'])
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class PhotoView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    permission_required = 'photos.change_photo'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_superuser


    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = '/'
    permission_required = 'photos.delete_photo'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_superuser

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user.username


class FavoriteView(View):

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user = request.user
        favorite, created = Favorite.objects.get_or_create(photo=photo, user=user)
        if created:
            return redirect('profile', pk=user.pk)
        else:
            favorite.delete()
            return redirect('profile', pk=user.pk)

