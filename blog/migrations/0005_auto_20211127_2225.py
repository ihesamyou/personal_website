# Generated by Django 3.2.7 on 2021-11-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211127_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
