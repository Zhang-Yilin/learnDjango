# Generated by Django 2.2.6 on 2019-10-09 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time', '-last_update_time']},
        ),
    ]
