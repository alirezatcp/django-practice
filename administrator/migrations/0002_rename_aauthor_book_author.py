# Generated by Django 3.2 on 2024-12-24 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='aauthor',
            new_name='author',
        ),
    ]