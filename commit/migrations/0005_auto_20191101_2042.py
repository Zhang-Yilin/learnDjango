# Generated by Django 2.2.6 on 2019-11-02 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commit', '0004_auto_20191101_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rootc', to='commit.Commit'),
        ),
        migrations.AlterField(
            model_name='commit',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parentc', to='commit.Commit'),
        ),
    ]
