# Generated by Django 2.2 on 2020-03-11 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20200311_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='no value'),
            preserve_default=False,
        ),
    ]