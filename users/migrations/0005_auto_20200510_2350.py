# Generated by Django 3.0.6 on 2020-05-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'пользователя', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'профиль', 'verbose_name_plural': 'профили'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='user_pics/default_pic.png', upload_to='user_pics/%Y/', verbose_name='Фотография'),
        ),
    ]