# Generated by Django 3.2.16 on 2024-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tallas',
            name='camisa',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tallas',
            name='estatura',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tallas',
            name='pantalon',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tallas',
            name='peso',
            field=models.CharField(max_length=10),
        ),
    ]
