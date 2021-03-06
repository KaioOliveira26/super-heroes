# Generated by Django 3.2 on 2021-04-20 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('character', '0003_alter_character_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='photo',
            field=models.ImageField(upload_to='static'),
        ),
        migrations.CreateModel(
            name='FavoriteCharacter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
