# Generated by Django 3.2 on 2021-04-20 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('character', '0004_auto_20210420_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritecharacter',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favoritecharacter',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character'),
        ),
    ]
