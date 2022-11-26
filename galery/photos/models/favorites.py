from django.contrib.auth.models import User
from django.db import models

from photos.models.photos import Photo


class Favorite(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='favorite_photos',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_users',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Избранная запись'
        verbose_name_plural = 'Избранные записи'

