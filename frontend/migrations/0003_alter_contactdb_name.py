# Generated by Django 4.1 on 2022-11-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_contactdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]