# Generated by Django 2.2.7 on 2020-01-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20191211_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_detail',
            field=models.CharField(db_index=True, max_length=300),
        ),
    ]
