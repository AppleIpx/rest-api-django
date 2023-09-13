# Generated by Django 4.2.5 on 2023-09-11 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Вин')),
                ('color', models.CharField(max_length=64, verbose_name='Цвет')),
                ('brand', models.CharField(max_length=64, verbose_name='Бренд')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэчбек'), (3, 'Универсал'), (4, 'Купе')], verbose_name='Тип автомобиля')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
