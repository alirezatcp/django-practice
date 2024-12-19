# Generated by Django 3.2 on 2024-12-18 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('signing_date', models.DateTimeField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10)),
                ('account_type', models.CharField(choices=[('R', 'Regular'), ('P', 'Premium')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.SET, related_name='posts', to='app.user')),
            ],
        ),
    ]
