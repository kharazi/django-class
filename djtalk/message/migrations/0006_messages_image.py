# Generated by Django 2.2.6 on 2019-11-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20191120_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]