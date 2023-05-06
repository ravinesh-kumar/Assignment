# Generated by Django 4.1 on 2022-11-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('category_name', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('detail', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='product_upload/images')),
            ],
        ),
    ]
