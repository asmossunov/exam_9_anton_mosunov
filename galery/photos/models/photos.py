from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='uploads')
    description = models.CharField(verbose_name='Описание', null=False, blank=False, max_length=200)

    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE)
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
