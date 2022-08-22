# Generated by Django 3.2.7 on 2022-04-27 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('specialist', models.CharField(choices=[('Physiatrist', 'Physiatrist'), ('Dermatologist', 'Dermatologist'), ('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), ('Nephrologist', 'Nephrologist'), ('Gynecologist', 'Gynecologist'), ('Pathologist', 'Pathologist'), ('Podiatrist', 'Podiatrist'), ('Family Physician', 'Family Physicians')], max_length=200)),
                ('about', models.CharField(default=None, max_length=600)),
                ('contact', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media/image')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
