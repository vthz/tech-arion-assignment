# Generated by Django 4.0 on 2023-03-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_logintopmodel_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
