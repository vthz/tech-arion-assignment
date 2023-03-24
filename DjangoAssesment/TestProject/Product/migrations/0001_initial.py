# Generated by Django 4.0 on 2023-03-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('unique_id', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
