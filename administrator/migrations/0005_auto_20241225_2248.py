# Generated by Django 3.2 on 2024-12-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('hide_book', 'Can make book hidden')]},
        ),
        migrations.AddField(
            model_name='book',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]