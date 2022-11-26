# Generated by Django 4.1.3 on 2022-11-26 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads', verbose_name='Фото')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_users', to='photos.photo', verbose_name='Избранное')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_photos', to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Избранная запись',
                'verbose_name_plural': 'Избранные записи',
            },
        ),
    ]