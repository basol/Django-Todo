# Generated by Django 2.2 on 2019-05-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190505_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['id', '-created_time']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
