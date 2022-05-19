# Generated by Django 4.0.4 on 2022-05-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudMarque', '0003_alter_marque_chevaux'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couleur', models.CharField(max_length=100)),
                ('pack', models.CharField(max_length=50)),
                ('prix', models.CharField(max_length=100)),
                ('quantite', models.IntegerField(blank=True)),
            ],
        ),
    ]
