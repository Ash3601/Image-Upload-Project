# Generated by Django 4.1.5 on 2023-01-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.CharField(default='abbasiashin0@gmail.com', max_length=255),
        ),
    ]
