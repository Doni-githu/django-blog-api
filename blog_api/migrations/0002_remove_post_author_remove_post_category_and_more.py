# Generated by Django 4.1.9 on 2023-08-17 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]