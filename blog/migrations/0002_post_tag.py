# Generated by Django 3.0.7 on 2020-10-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.SlugField(default='test_debug', max_length=200, unique=True),
        ),
    ]