# Generated by Django 2.2.6 on 2019-11-20 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20191120_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
