from rest_framework import serializers

from photos.models import Photo

from photos.models import Favorite


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'description', 'author', 'is_deleted', 'changed_at', 'created_at',)
        read_only_fields = ('id', 'created_at', 'changed_at', 'is_deleted')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'photo', 'is_deleted', 'changed_at', 'created_at',)
        read_only_fields = ('id', 'created_at', 'changed_at', 'is_deleted')


