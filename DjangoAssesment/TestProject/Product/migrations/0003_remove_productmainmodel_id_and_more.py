# Generated by Django 4.0 on 2023-03-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_productmainmodel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmainmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='productmainmodel',
            name='unique_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]