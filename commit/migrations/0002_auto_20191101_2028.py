# Generated by Django 2.2.6 on 2019-11-02 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commit',
            options={'ordering': ['-commit_time']},
        ),
        migrations.AddField(
            model_name='commit',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
