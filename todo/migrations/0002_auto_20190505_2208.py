# Generated by Django 2.2 on 2019-05-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-user', '-created_time']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default='False', verbose_name='Status'),
            preserve_default=False,
        ),
    ]
