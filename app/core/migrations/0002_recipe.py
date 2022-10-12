# Generated by Django 4.1 on 2022-10-12 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=100)),
                ('recipe_description', models.TextField()),
                ('cuisine', models.CharField(max_length=100)),
                ('vegan', models.BooleanField()),
                ('vegeterian', models.BooleanField()),
                ('suitable_for_diabetics', models.BooleanField()),
                ('recipe_instructions', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
