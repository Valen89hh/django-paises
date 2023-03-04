# Generated by Django 4.1.7 on 2023-03-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_habitantes', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('alcalde', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geografia.pais')),
            ],
            options={
                'db_table': 'ciudad',
            },
        ),
    ]
