# Generated by Django 4.0.4 on 2022-04-21 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ficha', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Fichas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ficha', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
