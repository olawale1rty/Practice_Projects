# Generated by Django 3.0.3 on 2020-03-11 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(),
        ),
    ]
