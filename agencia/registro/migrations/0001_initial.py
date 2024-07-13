# Generated by Django 5.0.6 on 2024-06-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('CheckIn', models.DateTimeField()),
                ('CheckOut', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Noches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais_destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fechaLLegada', models.DateTimeField()),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=50)),
            ],
        ),
    ]
