# Generated by Django 3.2.7 on 2021-12-19 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=250)),
                ('metatags', models.TextField(blank=True, default=None, max_length=450)),
                ('image_1', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_1', models.TextField(blank=True, default=None)),
                ('image_2', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_2', models.TextField(blank=True, default=None)),
                ('image_3', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_3', models.TextField(blank=True, default=None)),
                ('image_4', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_4', models.TextField(blank=True, default=None)),
                ('image_5', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_5', models.TextField(blank=True, default=None)),
                ('image_6', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_6', models.TextField(blank=True, default=None)),
                ('image_7', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_7', models.TextField(blank=True, default=None)),
                ('image_8', models.ImageField(blank=True, default=None, upload_to='article_images/')),
                ('paragraph_8', models.TextField(blank=True, default=None)),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('quote', models.TextField()),
                ('identifier', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1500, verbose_name='دیدگاه شما')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(blank=True, default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
